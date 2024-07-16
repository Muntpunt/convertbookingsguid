from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import base64


class Item(BaseModel):
    name:str
    price:float
    guid:str

app = FastAPI()

@app.get("/")
async def read_item():
    return {"message":"Welcome to the GUID convert app"}

@app.get("/guidconvert/{guid}")
async def read_item(guid):
    selfServiceAppointmentID = uuid.UUID(guid)
    bytearray = selfServiceAppointmentID.bytes_le
    shortId = base64.urlsafe_b64encode(bytearray).decode('utf-8')
    shortIdclean = shortId.rsplit("==", 1)[0] + str(shortId.count("="))
    return {"ConvertedGUID": f"{shortIdclean}"}

@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"{item.name} is priced at €{item.price}"}
