import json
from re import error
from src.repo.queries import get_contracts, insert_company, insert_contract, search_company, search_contract
from src.spiders.crawler import track_company

def get_company(cnpj):
  print('init')
  company_data = {}
  contracts = [] 
  try:
    company_data = search_company(cnpj)
    if company_data:
      print('EMPRESA: ', company_data)
      contracts_cursor= get_contracts(cnpj)
      contracts = list(contracts_cursor)
      print(len(contracts), 'CONTRATOS: ', contracts  )
    if not company_data:
      print('initialing crawler')
      company_data = track_company(cnpj)
      print(f'crawler: {company_data}')
      for i in company_data:
        print(i)
        print(f'appending: {i["id"]}')
        contracts.append(i['id'])
        insert_contract(id=i['id'], cnpj=cnpj, data=i)
      print('contracts: ', contracts)
      insert_company(name=company_data[0]['nomeFornecedor'], cnpj=cnpj, data=contracts)
      print('inserted')
  except Exception as err:
    print('Error: ', err)
  contracts_data = [] 
  print('searching contracts...')
  search_contracts = get_contracts(cnpj)
  print('found!')
  for contract in search_contracts:
    contracts_data.append(contract)
  print('CONTRACT_DATA: ', contracts_data)
  return contracts_data
