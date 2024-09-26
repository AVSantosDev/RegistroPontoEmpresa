from datetime import datetime
from conexao import conectar


def registrar_ponto(id_funcionario, tipo):
    conexao = conectar()
    cursor = conexao.cursor()
    agora = datetime.now()

    if tipo == "entrada_manha":
        sql = "INSERT INTO registroponto (id_funcionario, entrada_manha) VALUES (%s, %s)"
        valores = (id_funcionario, agora)
    elif tipo == "saida_manha":
        sql = " UPDATE registroponto SET saida_manha = %s WHERE id_funcionario = %s and saida_manha IS NULL"
        valores = (agora, id_funcionario)
    elif tipo == "entrada_tarde":
        sql = " UPDATE registroponto SET entrada_tarde = %s WHERE id_funcionario = %s and entrada_tarde IS NULL"
        valores = (agora, id_funcionario)
    elif tipo == "saida_tarde":
        sql = " UPDATE registroponto SET saida_tarde = %s WHERE id_funcionario = %s and saida_tarde IS NULL"
        valores = (agora, id_funcionario)
    else:
        print("Tipo de registro invalido")
        return

    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
    print(f"Ponto Registrado: {tipo} as {agora} ")
