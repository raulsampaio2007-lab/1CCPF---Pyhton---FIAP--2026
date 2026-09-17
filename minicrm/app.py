



from model import model_lead

import control
def list_lead():
    leads = control.read_leads()
    if not leads :
        print("nenhum lead ainda")
        return

    print(f'# |{"nome:<15"}|{"email":<15}| empresa|')

    for i, lead in enumerate(leads):
        print(f"{i:02d}| {lead["name"]:<10} | {lead["email"]:<10} | {lead["company"]}")

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

def search_leads():
       querry = input("buscando por : ").strip().lower()
       if not querry:
           print("consulta vazia")
           return
       # enviar querry para o control realizar a busca no lead.json
        leads_found = control.read_leads_search(querry)
       print(f"##| {"nome":<10}| {"email":<10}| empresa")
       for i, lead in leads_found:
            print  (f"{i:02d}{lead["name"]} {lead["email"]} {lead["company"]}".lower())
def export_leads():
    path_csv = control.exporrt_csv()
    if path_csv is None:
        print("não foi possivel exportar os leads")
    else:
        print(f"exportado para {path_csv}")
        return
def main():
    while True:
        print("\nMini CRM de leads")
        print("[1] Adicionar lead")
        print("[2] listar lead")
        print("[3] Buscar nome/email/empresa")
        print("[4] Exportar CSV")
        print("[0] Sair do programs")

        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_lead()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Até mais")
            break
        else:
            print("Opção invalida")
if __name__ == "__main__":
    main()