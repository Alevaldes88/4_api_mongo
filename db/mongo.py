import motor.motor_asyncio
import os
from dotenv import load_dotenv

# cargamos los varibles de entorno

load_dotenv()

MONGO_URL= os.getenv('MONGO_URL')
MONGO_DB_NAME= os.getenv('MONGO_DB_NAME')

# cargamos el cliente mongoDB asincrono

client= motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client['MONGO_DB_NAME']

# cargar la collecion de libros de BBDD books

book_collection = db['books']