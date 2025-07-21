from fastapi import APIRouter
from models.book_models import BookCreate
from controllers import book_controllers
router = APIRouter()

# Crear un libro 
@router.post('/', status_code=200)
async def create_book(book: BookCreate):
    return await book_controllers.create_book(book)