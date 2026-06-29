from conexao import criar_conexao, fechar_conexao


# =========================================================
# 1. CRUD: USUÁRIO
# =========================================================

def cadastrar_usuario():
    print("\n--- NOVO USUÁRIO ---")
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    senha = input("Digite a senha: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
            valores = (nome, email, senha)
            cursor.execute(sql, valores)
            conexao.commit()
            print(f"=> Sucesso! Usuário '{nome}' cadastrado.")
        except Exception as e:
            print(f"X Erro ao salvar usuário: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)


def listar_usuarios():
    print("\n--- LISTA DE USUÁRIOS ---")
    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT id_usuario, nome, email, data_cadastro FROM usuario")
            usuarios = cursor.fetchall()
            if not usuarios:
                print("Nenhum usuário encontrado.")
            else:
                for u in usuarios:
                    print(f"ID: {u[0]} | Nome: {u[1]} | E-mail: {u[2]} | Cadastro: {u[3]}")
        except Exception as e:
            print(f"X Erro ao buscar usuários: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)


def atualizar_usuario():
    print("\n--- ATUALIZAR USUÁRIO ---")
    id_usuario = input("Digite o ID do usuário que deseja atualizar: ")
    novo_nome = input("Digite o novo nome: ")
    novo_email = input("Digite o novo e-mail: ")
    nova_senha = input("Digite a nova senha: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "UPDATE usuario SET nome = %s, email = %s, senha = %s WHERE id_usuario = %s"
            valores = (novo_nome, novo_email, nova_senha, id_usuario)
            cursor.execute(sql, valores)
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"=> Sucesso! Usuário ID {id_usuario} atualizado.")
            else:
                print("X Nenhum usuário encontrado com esse ID.")
        except Exception as e:
            print(f"X Erro ao atualizar usuário: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)


def deletar_usuario():
    print("\n--- DELETAR USUÁRIO ---")
    id_usuario = input("Digite o ID do usuário que deseja deletar: ")
    certeza = input(f"Tem certeza que deseja apagar o ID {id_usuario}? (S/N): ")
    if certeza.upper() != 'S':
        print("Operação cancelada.")
        return

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "DELETE FROM usuario WHERE id_usuario = %s"
            cursor.execute(sql, (id_usuario,))
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"=> Sucesso! Usuário ID {id_usuario} deletado.")
            else:
                print("X Nenhum usuário encontrado com esse ID.")
        except Exception as e:
            print(f"X Erro ao deletar: {e}\nDica: Remova antes as dependências deste usuário.")
        finally:
            cursor.close()
            fechar_conexao(conexao)


# =========================================================
# 2. CRUD: CATEGORIA
# =========================================================

def cadastrar_categoria():
    print("\n--- NOVA CATEGORIA ---")
    nome = input("Nome da Categoria: ")
    descricao = input("Descrição: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "INSERT INTO categoria (nome, descricao) VALUES (%s, %s)"
            cursor.execute(sql, (nome, descricao))
            conexao.commit()
            print(f"=> Sucesso! Categoria '{nome}' criada.")
        except Exception as e:
            print(f"X Erro ao salvar categoria: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)


def listar_categorias():
    print("\n--- LISTA DE CATEGORIAS ---")
    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT id_categoria, nome, descricao FROM categoria")
            categorias = cursor.fetchall()
            if not categorias:
                print("Nenhuma categoria encontrada.")
            else:
                for c in categorias:
                    print(f"ID: {c[0]} | Nome: {c[1]} | Descrição: {c[2]}")
        except Exception as e:
            print(f"X Erro ao buscar categorias: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)


def atualizar_categoria():
    print("\n--- ATUALIZAR CATEGORIA ---")
    id_categoria = input("ID da categoria que deseja atualizar: ")
    novo_nome = input("Novo nome: ")
    nova_descricao = input("Nova descrição: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "UPDATE categoria SET nome = %s, descricao = %s WHERE id_categoria = %s"
            cursor.execute(sql, (novo_nome, nova_descricao, id_categoria))
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"=> Categoria ID {id_categoria} atualizada.")
            else:
                print("X Categoria não encontrada.")
        except Exception as e:
            print(f"X Erro ao atualizar categoria: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)


def deletar_categoria():
    print("\n--- DELETAR CATEGORIA ---")
    id_categoria = input("ID da categoria que deseja deletar: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "DELETE FROM categoria WHERE id_categoria = %s"
            cursor.execute(sql, (id_categoria,))
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"=> Categoria ID {id_categoria} removida.")
            else:
                print("X Categoria não encontrada.")
        except Exception as e:
            print(f"X Erro ao deletar categoria: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)


# =========================================================
# 3. CRUD: PASTA (BOARD)
# =========================================================

def cadastrar_pasta():
    print("\n--- NOVA PASTA ---")
    nome = input("Nome da Pasta: ")
    descricao = input("Descrição: ")
    id_usuario = input("ID do Usuário dono desta pasta: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "INSERT INTO pasta (nome, descricao, id_usuario) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nome, descricao, id_usuario))
            conexao.commit()
            print(f"=> Sucesso! Pasta '{nome}' vinculada ao Usuário ID {id_usuario}.")
        except Exception as e:
            print(f"X Erro ao criar pasta: {e}\nCertifique-se de que o ID do usuário existe.")
        finally:
            cursor.close()
            fechar_conexao(conexao)


def listar_pastas():
    print("\n--- LISTA DE PASTAS ---")
    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT id_pasta, nome, descricao, id_usuario FROM pasta")
            pastas = cursor.fetchall()
            if not pastas:
                print("Nenhuma pasta encontrada.")
            else:
                for p in pastas:
                    print(f"ID Pasta: {p[0]} | Nome: {p[1]} | Descrição: {p[2]} | Dono (ID Usuário): {p[3]}")
        except Exception as e:
            print(f"X Erro ao buscar pastas: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)


def atualizar_pasta():
    print("\n--- ATUALIZAR PASTA ---")
    id_pasta = input("ID da pasta que deseja atualizar: ")
    novo_nome = input("Novo nome da pasta: ")
    nova_descricao = input("Nova descrição: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "UPDATE pasta SET nome = %s, descricao = %s WHERE id_pasta = %s"
            cursor.execute(sql, (novo_nome, nova_descricao, id_pasta))
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"=> Pasta ID {id_pasta} atualizada com sucesso.")
            else:
                print("X Pasta não encontrada.")
        except Exception as e:
            print(f"X Erro ao atualizar pasta: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)


def deletar_pasta():
    print("\n--- DELETAR PASTA ---")
    id_pasta = input("ID da pasta que deseja remover: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "DELETE FROM pasta WHERE id_pasta = %s"
            cursor.execute(sql, (id_pasta,))
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"=> Pasta ID {id_pasta} deletada.")
            else:
                print("X Pasta não encontrada.")
        except Exception as e:
            print(f"X Erro ao deletar pasta: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)


# =========================================================
# 4. CRUD: PIN
# =========================================================

def cadastrar_pin():
    print("\n--- NOVO PIN ---")
    titulo = input("Título do Pin: ")
    descricao = input("Descrição textual: ")
    id_usuario = input("ID do Usuário criador do Pin: ")
    id_categoria = input("ID da Categoria do Pin: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "INSERT INTO pin (titulo, descricao, id_usuario, id_categoria) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (titulo, descricao, id_usuario, id_categoria))
            conexao.commit()
            print(f"=> Sucesso! Pin '{titulo}' postado.")
        except Exception as e:
            print(f"X Erro ao criar Pin: {e}\nVerifique se o ID do usuário e o ID da categoria existem.")
        finally:
            cursor.close()
            fechar_conexao(conexao)


def listar_pins():
    print("\n--- LISTA DE PINS ---")
    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT id_pin, titulo, descricao, id_usuario, id_categoria FROM pin")
            pins = cursor.fetchall()
            if not pins:
                print("Nenhum pin encontrado.")
            else:
                for p in pins:
                    print(f"ID Pin: {p[0]} | Título: {p[1]} | Desc: {p[2]} | Usuário: {p[3]} | Categoria: {p[4]}")
        except Exception as e:
            print(f"X Erro ao listar pins: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)


def atualizar_pin():
    print("\n--- ATUALIZAR PIN ---")
    id_pin = input("ID do pin que deseja alterar: ")
    novo_titulo = input("Novo título: ")
    nova_descricao = input("Nova descrição: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "UPDATE pin SET titulo = %s, descricao = %s WHERE id_pin = %s"
            cursor.execute(sql, (novo_titulo, nova_descricao, id_pin))
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"=> Pin ID {id_pin} modificado.")
            else:
                print("X Pin não encontrado.")
        except Exception as e:
            print(f"X Erro ao atualizar pin: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)


def deletar_pin():
    print("\n--- DELETAR PIN ---")
    id_pin = input("ID do pin que deseja apagar: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "DELETE FROM pin WHERE id_pin = %s"
            cursor.execute(sql, (id_pin,))
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"=> Pin ID {id_pin} excluído.")
            else:
                print("X Pin não encontrado.")
        except Exception as e:
            print(f"X Erro ao deletar pin: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)

# =========================================================
# 5. CRUD: COMENTÁRIO
# =========================================================

def cadastrar_comentario():
    print("\n--- NOVO COMENTÁRIO ---")
    texto = input("Digite o comentário: ")
    id_usuario = input("ID do Usuário que está comentando: ")
    id_pin = input("ID do Pin que receberá o comentário: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "INSERT INTO comentario (texto, id_usuario, id_pin) VALUES (%s, %s, %s)"
            cursor.execute(sql, (texto, id_usuario, id_pin))
            conexao.commit()
            print("=> Sucesso! Comentário adicionado.")
        except Exception as e:
            print(f"X Erro ao salvar comentário: {e}\nVerifique se o ID do usuário e o ID do pin existem.")
        finally:
            cursor.close()
            fechar_conexao(conexao)

def listar_comentarios():
    print("\n--- LISTA DE COMENTÁRIOS ---")
    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT id_comentario, texto, id_usuario, id_pin, data_comentario FROM comentario")
            comentarios = cursor.fetchall()
            if not comentarios:
                print("Nenhum comentário encontrado.")
            else:
                for c in comentarios:
                    print(f"ID: {c[0]} | Texto: {c[1]} | Usuário: {c[2]} | Pin: {c[3]} | Data: {c[4]}")
        except Exception as e:
            print(f"X Erro ao buscar comentários: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)

def atualizar_comentario():
    print("\n--- ATUALIZAR COMENTÁRIO ---")
    id_comentario = input("ID do comentário que deseja atualizar: ")
    novo_texto = input("Novo texto do comentário: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "UPDATE comentario SET texto = %s WHERE id_comentario = %s"
            cursor.execute(sql, (novo_texto, id_comentario))
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"=> Sucesso! Comentário ID {id_comentario} atualizado.")
            else:
                print("X Nenhum comentário encontrado com esse ID.")
        except Exception as e:
            print(f"X Erro ao atualizar comentário: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)

def deletar_comentario():
    print("\n--- DELETAR COMENTÁRIO ---")
    id_comentario = input("ID do comentário que deseja deletar: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "DELETE FROM comentario WHERE id_comentario = %s"
            cursor.execute(sql, (id_comentario,))
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"=> Sucesso! Comentário ID {id_comentario} deletado.")
            else:
                print("X Nenhum comentário encontrado com esse ID.")
        except Exception as e:
            print(f"X Erro ao deletar: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)


# =========================================================
# 6. CRUD: IMAGEM
# =========================================================

def cadastrar_imagem():
    print("\n--- NOVA IMAGEM ---")
    url_imagem = input("URL/Link da imagem: ")
    descricao = input("Descrição da imagem: ")
    id_pin = input("ID do Pin ao qual esta imagem pertence: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "INSERT INTO imagem (url_imagem, descricao, id_pin) VALUES (%s, %s, %s)"
            cursor.execute(sql, (url_imagem, descricao, id_pin))
            conexao.commit()
            print("=> Sucesso! Imagem vinculada ao Pin.")
        except Exception as e:
            print(f"X Erro ao salvar imagem: {e}\nVerifique se o ID do pin existe.")
        finally:
            cursor.close()
            fechar_conexao(conexao)

def listar_imagens():
    print("\n--- LISTA DE IMAGENS ---")
    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT id_imagem, url_imagem, descricao, id_pin FROM imagem")
            imagens = cursor.fetchall()
            if not imagens:
                print("Nenhuma imagem encontrada.")
            else:
                for i in imagens:
                    print(f"ID: {i[0]} | URL: {i[1]} | Desc: {i[2]} | Pin: {i[3]}")
        except Exception as e:
            print(f"X Erro ao buscar imagens: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)

def atualizar_imagem():
    print("\n--- ATUALIZAR IMAGEM ---")
    id_imagem = input("ID da imagem que deseja atualizar: ")
    nova_url = input("Nova URL da imagem: ")
    nova_descricao = input("Nova descrição: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "UPDATE imagem SET url_imagem = %s, descricao = %s WHERE id_imagem = %s"
            cursor.execute(sql, (nova_url, nova_descricao, id_imagem))
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"=> Sucesso! Imagem ID {id_imagem} atualizada.")
            else:
                print("X Nenhuma imagem encontrada com esse ID.")
        except Exception as e:
            print(f"X Erro ao atualizar imagem: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)

def deletar_imagem():
    print("\n--- DELETAR IMAGEM ---")
    id_imagem = input("ID da imagem que deseja deletar: ")

    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "DELETE FROM imagem WHERE id_imagem = %s"
            cursor.execute(sql, (id_imagem,))
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"=> Sucesso! Imagem ID {id_imagem} deletada.")
            else:
                print("X Nenhuma imagem encontrada com esse ID.")
        except Exception as e:
            print(f"X Erro ao deletar: {e}")
        finally:
            cursor.close()
            fechar_conexao(conexao)
# =========================================================
# MENUS SUBORDINADOS
# =========================================================

def menu_usuarios():
    while True:
        print("\n=== GERENCIAR USUÁRIOS ===")
        print("1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            atualizar_usuario()
        elif opcao == '4':
            deletar_usuario()
        elif opcao == '0':
            break


def menu_categorias():
    while True:
        print("\n=== GERENCIAR CATEGORIAS ===")
        print("1. Cadastrar Categoria")
        print("2. Listar Categorias")
        print("3. Atualizar Categoria")
        print("4. Deletar Categoria")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_categoria()
        elif opcao == '2':
            listar_categorias()
        elif opcao == '3':
            atualizar_categoria()
        elif opcao == '4':
            deletar_categoria()
        elif opcao == '0':
            break


def menu_pastas():
    while True:
        print("\n=== GERENCIAR PASTAS ===")
        print("1. Cadastrar Pasta")
        print("2. Listar Pastas")
        print("3. Atualizar Pasta")
        print("4. Deletar Pasta")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_pasta()
        elif opcao == '2':
            listar_pastas()
        elif opcao == '3':
            atualizar_pasta()
        elif opcao == '4':
            deletar_pasta()
        elif opcao == '0':
            break


def menu_pins():
    while True:
        print("\n=== GERENCIAR PINS ===")
        print("1. Cadastrar Pin")
        print("2. Listar Pins")
        print("3. Atualizar Pin")
        print("4. Deletar Pin")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_pin()
        elif opcao == '2':
            listar_pins()
        elif opcao == '3':
            atualizar_pin()
        elif opcao == '4':
            deletar_pin()
        elif opcao == '0':
            break

def menu_comentarios():
    while True:
        print("\n=== GERENCIAR COMENTÁRIOS ===")
        print("1. Adicionar Comentário")
        print("2. Listar Comentários")
        print("3. Atualizar Comentário")
        print("4. Deletar Comentário")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_comentario()
        elif opcao == '2':
            listar_comentarios()
        elif opcao == '3':
            atualizar_comentario()
        elif opcao == '4':
            deletar_comentario()
        elif opcao == '0':
            break

def menu_imagens():
    while True:
        print("\n=== GERENCIAR IMAGENS ===")
        print("1. Adicionar Imagem")
        print("2. Listar Imagens")
        print("3. Atualizar Imagem")
        print("4. Deletar Imagem")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_imagem()
        elif opcao == '2':
            listar_imagens()
        elif opcao == '3':
            atualizar_imagem()
        elif opcao == '4':
            deletar_imagem()
        elif opcao == '0':
            break
# =========================================================
# MENU PRINCIPAL
# =========================================================
def menu_principal():
    while True:
        print("\n" + "=" * 30)
        print("   PINTEREST CLONE - UNIVALI   ")
        print("=" * 30)
        print("1. Gerenciar Usuários")
        print("2. Gerenciar Pastas")
        print("3. Gerenciar Pins")
        print("4. Gerenciar Categorias")
        print("5. Gerenciar Comentários")
        print("6. Gerenciar Imagens")
        print("0. Sair do Sistema")
        print("=" * 30)

        opcao = input("Escolha o que deseja acessar: ")
        if opcao == '1':
            menu_usuarios()
        elif opcao == '2':
            menu_pastas()
        elif opcao == '3':
            menu_pins()
        elif opcao == '4':
            menu_categorias()
        elif opcao == '5':
            menu_comentarios()
        elif opcao == '6':
            menu_imagens()
        elif opcao == '0':
            print("Encerrando o sistema... Valeu!")
            break
        else:
            print("X Opção inválida!")


if __name__ == "__main__":
    menu_principal()
