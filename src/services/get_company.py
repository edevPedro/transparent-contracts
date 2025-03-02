import json
from src.repo.queries import insert_company, search_company
from src.spiders.crawler import track_company

def get_company(cnpj):
  print('init')
  company_data = {}
  try:
    company_data = search_company(cnpj)
    if company_data:
      print(f'type: {type(company_data)}')
      print(company_data["name"])
      return company_data
    if not company_data:
      print('initialing crawler')
      company_data = track_company(cnpj)
      print(f'crawler: {company_data["nomeFornecedor"]}')
      contracts = [] 
      for i in company_data:
        contracts.append(i['id'])
      insert_company(name=company_data['nomeFornecedor'], cnpj=cnpj, data=contracts)
      return company_data
  except:
    print('Error')
  return company_data

# get_company('81.076.390/0001-85 ')