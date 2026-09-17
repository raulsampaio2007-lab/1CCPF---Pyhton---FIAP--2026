from pathlib import Path
import json, csv


DATA_DIR = Path(__file__).resolve().parent / "data"
print(DATA_DIR)
DATA_DIR.mkdir( exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"
#CRUD
#CREATE
#READ
#UPDATE
#DELE0TE

#READ
def read_leads():
    if not DB_PATH.exists():
        return[]

    try:
        return json.loads(DB_PATH.read_text(encoding = "utf-8"))
    except json.JSONDecodeError:
        return[]
print(read_leads())


#CREATE
def create_lead(lead_dict):
    leads = read_leads() # lista de dicionarios de leads
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads,ensure_ascii= False, indent = 4), encoding = "utf-8")
    #EXPORT LEADS COMO CSV
def export_csv():
    """""Exporta os leads para CSV e retorna o  caminho do arquivo adicionado"""""
    path_csv = DATA_DIR / "leads.csv"
    leads = read_leads()

    try:
        with path_csv.open("w",newline= "",encoding = "utf-8") as file_csv:
            writer = csv.DictWriter(file_csv, fieldnames=leads[0].keys() )
            writer.writeheader()
            for row in leads:
                writer.writerow(row)
        return path_csv
    except PermissionError:
        return None
    #READ LEADS FROM QUERY/SEARCH
def read_leads_search(querry):
    leads = read_leads()
    results = []
    for i,lead in enumerate(leads):
        txt_lead = f"{lead["name"]} {lead["email"]} {lead["company"]}".lower()
        #print(txt_lead)

        if querry in txt_lead:
            results.append((i, lead)) #{0 , ({"name": "Alexandre"...})
    return results
print(read_leads_search("nike"))