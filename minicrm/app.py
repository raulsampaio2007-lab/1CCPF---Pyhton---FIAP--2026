



from model import model_lead

import control
def list_lead():
    leads = control.read_leads()
    if not leads :
        print("nenhum lead ainda")
        return

    print(leads)
def add_lead():

    name = input("Informe o nome do usuario: ")
    email = input("Informe o email do usuario: ")
    company = input("Informe a empresa do usuario: ")
    step = input("Informe a etapa de vendas:  ")

    #validar as entradas do usuario
    #depois de validar vamos modelar os dados
    print(model_lead(name,email,company,step))
    #depois de validar... vamos enviar esse dict (leads) para o leads.json
    #para salvar, vamos usar o modulo control


    control.create_lead(model_lead(name,email,company,step))
    print("lead adicionado(func)")
def main():
    while True:
        print("\nMini CRM de leads")
        print("[1] Adicionar lead")
        print("[2] listar lead")
        print("[0] Sair do programs")

        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_lead()
        elif opt == "0":
            print("Até mais")
            break
        else:
            print("Opção invalida")
if __name__ == "__main__":
    main()