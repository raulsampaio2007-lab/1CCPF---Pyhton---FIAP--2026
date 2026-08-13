''''endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]


def valida_erro(numero):
    if numero >= 200 and numero <= 299:
        return True
    else:
        return False


def identificador(numero, guarda):
    erro1 = 0
    erro2 = 0
    erro3 = 0

    for i in numero[0]:
        if i > 299 or i < 200:
            erro1 += 1
    for i in numero[1]:
        if i > 299 or i < 200:
            erro2 += 1
    for i in numero[2]:
        if i > 299 or i < 200:
            erro3 += 1

    guarda = erro1, erro2, erro3

    return numero, guarda


print(identificador(status, endpoints))'''''
def calcular_porcentagem_sucesso(requisicoes):
    total = len(requisicoes)
    sucessos = 0
    for codigo in requisicoes:
        if codigo >= 200 and codigo < 300:
            sucessos = sucessos + 1
    return (sucessos / total) * 100


def contar_erros(requisicoes):
    erros = 0
    for codigo in requisicoes:
        if codigo < 200 or codigo >= 300:
            erros = erros + 1
    return erros


def tem_erros_consecutivos(requisicoes):
    for i in range(len(requisicoes) - 1):
        atual = requisicoes[i]
        proximo = requisicoes[i + 1]
        atual_e_erro = atual < 200 or atual >= 300
        proximo_e_erro = proximo < 200 or proximo >= 300
        if atual_e_erro and proximo_e_erro:
            return True
    return False


def classificar_endpoint(porcentagem, consecutivos):
    if consecutivos == True:
        return "CRÍTICO"
    elif porcentagem >= 80:
        return "ESTÁVEL"
    else:
        return "INSTÁVEL"


def main():
    endpoints = ["/login", "/produtos", "/pedidos"]
    status = [
        [200, 200, 401, 200, 500],
        [200, 200, 200, 200, 200],
        [201, 500, 502, 201, 500]
    ]

    endpoint_mais_erros = ""
    maior_qtd_erros = -1

    for i in range(len(endpoints)):
        nome = endpoints[i]
        requisicoes = status[i]

        porcentagem = calcular_porcentagem_sucesso(requisicoes)
        qtd_erros = contar_erros(requisicoes)
        consecutivos = tem_erros_consecutivos(requisicoes)
        classificacao = classificar_endpoint(porcentagem, consecutivos)

        print(f"Endpoint: {nome}")
        print(f"  Sucesso: {porcentagem:.1f}%")
        print(f"  Erros: {qtd_erros}")
        print(f"  Erros consecutivos: {consecutivos}")
        print(f"  Classificação: {classificacao}")
        print()

        if qtd_erros > maior_qtd_erros:
            maior_qtd_erros = qtd_erros
            endpoint_mais_erros = nome

    print(f"Endpoint com mais erros: {endpoint_mais_erros} ({maior_qtd_erros} erros)")


main()









