import fastapi 
import uvicorn
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
      print(data)
      return JSONResponse(data['name'])
    raise fastapi.HTTPException(status_code=404, detail='Not found.')

if __name__ == "__main__":
  print('olá')
  uvicorn.run("contracts:app", port=5000, log_level="info", reload=True)