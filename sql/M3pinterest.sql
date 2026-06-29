-- =====================================================
-- BANCO DE DADOS
-- =====================================================

DROP SCHEMA IF EXISTS pinterest_db;
CREATE SCHEMA pinterest_db;
USE pinterest_db;

-- =====================================================
-- USUÁRIO
-- =====================================================

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- CATEGORIA
-- =====================================================

CREATE TABLE categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(255)
);

-- =====================================================
-- PIN (POST PRINCIPAL DO SISTEMA)
-- =====================================================

CREATE TABLE pin (
    id_pin INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,

    id_usuario INT NOT NULL,
    id_categoria INT NOT NULL,

    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria) ON DELETE CASCADE
);

-- =====================================================
-- IMAGEM (MÍDIA DO PIN)
-- =====================================================

CREATE TABLE imagem (
    id_imagem INT AUTO_INCREMENT PRIMARY KEY,
    url_imagem VARCHAR(255) NOT NULL,
    descricao VARCHAR(255),

    id_pin INT NOT NULL,

    FOREIGN KEY (id_pin) REFERENCES pin(id_pin) ON DELETE CASCADE
);

-- =====================================================
-- PASTA / BOARD
-- =====================================================

CREATE TABLE pasta (
    id_pasta INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,

    id_usuario INT NOT NULL,

    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE
);

-- =====================================================
-- RELAÇÃO N:N (PASTA salva PIN)
-- =====================================================

CREATE TABLE pasta_pin (
    id_pasta INT NOT NULL,
    id_pin INT NOT NULL,

    PRIMARY KEY (id_pasta, id_pin),

    FOREIGN KEY (id_pasta) REFERENCES pasta(id_pasta) ON DELETE CASCADE,
    FOREIGN KEY (id_pin) REFERENCES pin(id_pin) ON DELETE CASCADE
);

-- =====================================================
-- COMENTÁRIO
-- =====================================================

CREATE TABLE comentario (
    id_comentario INT AUTO_INCREMENT PRIMARY KEY,
    texto TEXT NOT NULL,
    data_comentario DATETIME DEFAULT CURRENT_TIMESTAMP,

    id_usuario INT NOT NULL,
    id_pin INT NOT NULL,

    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_pin) REFERENCES pin(id_pin) ON DELETE CASCADE
);

-- =====================================================
-- INSERÇÃO DE USUÁRIOS
-- =====================================================

INSERT INTO usuario (nome, email, senha) VALUES
('Pedro Leonel Pereira', 'pedroleonelpereira@gmail.com', '123456'),
('Andrey Felsky', 'andreyfelsky@edu.univali.br', '123456'),
('Samuel Douglas Rodrigues Rosa Filho', 'samuel.8227900@edu.univali.br', '123456'),
('Maria Silva', 'maria@gmail.com', '123456'),
('Joao Santos', 'joao@gmail.com', '123456');

-- =====================================================
-- INSERÇÃO DE CATEGORIAS
-- =====================================================

INSERT INTO categoria (nome, descricao) VALUES
('Arquitetura', 'Projetos arquitetônicos e decoração'),
('Moda', 'Tendências de moda e estilo'),
('Tecnologia', 'Inovação e computação'),
('Culinária', 'Receitas e gastronomia'),
('Design', 'Design gráfico e visual');

-- =====================================================
-- INSERÇÃO DE PASTAS (BOARD)
-- =====================================================

INSERT INTO pasta (nome, descricao, id_usuario) VALUES
('Casas Modernas', 'Referências de arquitetura moderna', 1),
('Looks Masculinos', 'Inspirações de moda masculina', 2),
('Projetos Tech', 'Ideias de tecnologia', 3),
('Receitas Favoritas', 'Pratos e receitas salvas', 4),
('Design Criativo', 'Inspirações de design', 5);

-- =====================================================
-- INSERÇÃO DE PINS
-- =====================================================

INSERT INTO pin (titulo,descricao,id_usuario,id_categoria) VALUES
('Casa Minimalista','Projeto residencial moderno e clean',1,1),
('Jaqueta de Couro','Moda casual masculina estilosa',2,2),
('Setup Gamer','Computador gamer completo',3,3),
('Lasanha Artesanal','Receita italiana tradicional',4,4),
('Logo Moderno','Design gráfico minimalista',5,5);

-- =====================================================
-- INSERÇÃO DE IMAGENS (DETALHE DO PIN)
-- =====================================================

INSERT INTO imagem (url_imagem, descricao, id_pin) VALUES
('https://site.com/img1.jpg', 'Imagem principal da casa minimalista', 1),
('https://site.com/img2.jpg', 'Detalhe da jaqueta de couro', 2),
('https://site.com/img3.jpg', 'Setup com RGB gamer', 3),
('https://site.com/img4.jpg', 'Lasanha pronta servida', 4),
('https://site.com/img5.jpg', 'Logo em fundo escuro', 5);

-- =====================================================
-- INSERÇÃO DE COMENTÁRIOS
-- =====================================================

INSERT INTO comentario (texto, id_usuario, id_pin) VALUES
('Projeto muito bonito!', 2, 1),
('Excelente inspiração!', 3, 1),
('Gostei bastante desse estilo.', 1, 2),
('Vou salvar esse pin!', 4, 3),
('Muito criativo!', 5, 5);

-- Listar Pins com autor e categoria

SELECT
    p.id_pin,
    p.titulo,
    p.descricao,
    u.nome AS usuario,
    c.nome AS categoria
FROM pin p
INNER JOIN usuario u
    ON p.id_usuario = u.id_usuario
INNER JOIN categoria c
    ON p.id_categoria = c.id_categoria;
    
-- Listar imagens de cada Pin

SELECT
    p.titulo,
    i.url_imagem,
    i.descricao
FROM imagem i
INNER JOIN pin p
    ON i.id_pin = p.id_pin;
    
-- Listar comentários

SELECT
    c.id_comentario,
    u.nome AS usuario,
    p.titulo AS pin,
    c.texto
FROM comentario c
INNER JOIN usuario u
    ON c.id_usuario = u.id_usuario
INNER JOIN pin p
    ON c.id_pin = p.id_pin;
    
-- Listar pastas e seus donos

SELECT
    p.id_pasta,
    p.nome,
    u.nome AS usuario
FROM pasta p
INNER JOIN usuario u
    ON p.id_usuario = u.id_usuario;
