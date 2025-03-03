from pymongo import MongoClient
import datetime

uri = 'mongodb://root:nagro@localhost:27017'

client = MongoClient(uri)
database = client['transparent-db']
collection = database['contracts']

def insert_company(name, cnpj, data):
  return collection.insert_one({'name': name, 'cnpj' : cnpj, 'contracts': data, 'updated_at':  datetime.datetime.now()})

def insert_contract(id, cnpj, data):
  return collection.insert_one({'id': id, 'contractOwner' : cnpj, 'contract-data': data, 'updated_at':  datetime.datetime.now()})

def search_company(cnpj):
  return collection.find_one({'cnpj': cnpj})

def search_contract(id):
  return collection.find_one({'id': id})

def get_contracts(cnpj):
  return collection.find({'cnpj': cnpj})