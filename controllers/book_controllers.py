from fastapi import HTTPException
# como vamos a conectarnos con base de datos tengo que importar la coneccion
from db.mongo import book_collection
from models.book_models import Book, BookCreate

# vamos a crear una funcion que nos permita convertir el tipo de mongo (objecto) en una clase Book de python. Vamos a crear una funcion book_helper que transforma los datos de python => mongo. Nestra propia funcion parseo
 
def book_helper(book: dict) -> Book:
    return Book(
        id= str(book["_id"]),
        title= book["title"],
        author= book["author"],
        year= book["year"],
        pages= book.get("pages")  
    )

# controlador post para crear un libro en mongo

async def create_book(book: BookCreate):
    try:
        new_book = book.model_dump()
        result = await book_collection.insert_one(new_book)
        book_created = await book_collection.find_one({"_id": result.inserted_id})
        return book_helper(book_created)
    except Exception as e:
        raise HTTPException(status_code=500, detail= f'Error: {str(e)}')


# controlador para obtener la lista de libros

async def get_book_list():
    try:
        books = []
        result = book_collection.find({})
        async for item in result:
            books.append(book_helper(item))
        return books
    except Exception as e:
        raise HTTPException(status_code= 500, detail=f"Error: {str(e)}")