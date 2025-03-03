import fastapi 
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.services.get_company import get_company

app = fastapi.FastAPI()

class ContractReq(BaseModel):
  cnpj: str

@app.post("/contracts")
async def contracts(contract_req: ContractReq):
    data = get_company(contract_req.cnpj)
    if data:
      print('FORMATO', data)
      return JSONResponse(data[0]['nomeFornecedor'])
    raise fastapi.HTTPException(status_code=404, detail='Not found.')