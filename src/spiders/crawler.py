import requests

def getId(cnpj):
    url = f"https://portaldatransparencia.gov.br/criterios/contratos/fornecedor/autocomplete?q={cnpj}"
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    }

    res = requests.get(url, headers=headers)
    return res.json() 

def track_company(cnpj):
  company = getId(cnpj)
  companyId = company[0]['id']
  url = f"https://portaldatransparencia.gov.br/contratos/consulta/resultado?paginacaoSimples=true&tamanhoPagina=10&offset=0&direcaoOrdenacao=desc&colunaOrdenacao=dataFimVigencia&assinaturaDe=01%2F01%2F2025&assinaturaAte=28%2F02%2F2025&fornecedor={companyId}&colunasSelecionadas=linkDetalhamento%2CdataAssinatura%2CdataPublicacaoDOU%2CdataInicioVigencia%2CdataFimVigencia%2CorgaoSuperior%2CorgaoEntidadeVinculada%2CunidadeGestora%2CformaContratacao%2CgrupoObjetoContratacao%2CnumeroContrato%2CnomeFornecedor%2CcpfCnpjFornecedor%2Csituacao%2CvalorContratado&_=1740804160066"
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Host': 'portaldatransparencia.gov.br'
  }
  res = requests.get(url, headers=headers)
  return res.json()['data']


#getCompanyData('81.076.390/0001-85')
