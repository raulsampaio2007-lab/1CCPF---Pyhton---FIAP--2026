#def boas_vindas (nome):
   # print(f"olá {nome}! seja bem vindo!")


#nome_digitado= input("digite seu nome")
#boas_vindas(nome_digitado)

#Função com parametro com retorno
#def soma(num_a,num_b):
   # soma=num_a + num_b
   # return soma
#soma(4,3)
#print(type(nome_digitado))

#idade = int(input("digite sua idade"))






# exercicios python
valor_1 = int(input (f"digite o valor 1"))
valor_2 = int(input (f"digite o valor 2"))
op = str(input ("Digite um sinal de operação"))
if op == "+" :
    print(f"o valor da soma é {valor_1 + valor_2}")
elif op == "-" :
    print(f"o valor da subtração é {valor_1 - valor_2}")
elif op == "/" :
    print(f"o valor da divisão é {valor_1 / valor_2}")
elif op == "*":
    print(f"o valor da multiplicação é {valor_1 * valor_2}")