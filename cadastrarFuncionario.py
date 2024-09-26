from conexao import conectar


def cadatrar_funcionario(nome, cargo, cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO funcionarios (nome, cargo, cpf) VALUES (%s, %s, %s)"
    valores = (nome, cargo, cpf)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
    print(f"Funcionario {nome} cadastrado com sucesso!")

    