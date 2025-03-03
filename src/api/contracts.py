import fastapi
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel
from src.services.get_company import get_company
from bson import ObjectId

app = fastapi.FastAPI()

class ContractReq(BaseModel):
    cnpj: str

def serialize_object_id(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, ObjectId):
                obj[key] = str(value)
        return obj
    elif isinstance(obj, list):
        return [serialize_object_id(item) for item in obj]
    elif isinstance(obj, ObjectId):
        return str(obj)
    else:
        return obj

@app.post("/contracts", response_class=ORJSONResponse)
async def contracts(contract_req: ContractReq):
    data = get_company(contract_req.cnpj)
    serialized_data = serialize_object_id(data)
    return serialized_data