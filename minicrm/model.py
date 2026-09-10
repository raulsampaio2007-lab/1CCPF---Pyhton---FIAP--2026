from datetime import date

def model_lead(name,email,company,step):
    """""Estrutura um lead como dicionario"""""
    return{
        "name":name,
        "email":email,
        "company":company,
        "step":step,
        "created":date.today().isoformat()





    }