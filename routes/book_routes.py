from fastapi import APIRouter
from models.book_models import BookCreate
from controllers import book_controllers
router = APIRouter()

# Crear un libro 
@router.post('/', status_code=201)
async def create_book(book: BookCreate):
    return await book_controllers.create_book(book)


# Obtener lista de libros
@router.get('/', status_code=200)
async def get_all():
    return await book_controllers.get_book_list()

# Obtener un libro por id
@router.get('/{book_id}', status_code=200)
async def get_book_by_id(book_id: str):
    return await book_controllers.get_book_by_id(book_id)

# Actualizar un libro por id
@router.put('/{book_id}')
async def update_book(book_id: str):
    return await book_controllers.update_book(book_id)