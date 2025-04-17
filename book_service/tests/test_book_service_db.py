import pytest
from book_service.app.schemas.book import BookCreateSchema, BookUpdateSchema
from book_service.app.controllers.add import db_add_book
from book_service.app.controllers.get import db_get_book_by_id, db_get_all
from book_service.app.controllers.update import db_update_book
from book_service.app.controllers.delete import db_delete_book
from book_service.app.controllers.rent import db_rent_book




@pytest.mark.asyncio
async def test_get_books_db(db_test_env):
    _, db = await anext(db_test_env)
    data = await db_get_all(db)
    assert data.data[0].title == "Tum Hi Ho"
    assert data.data[0].author == "Arijit Singh"
    assert data.data[0].genre == "romantic"

@pytest.mark.asyncio
async def test_get_book_by_title_db(db_test_env):
    book, db = await anext(db_test_env)
    book_id = book.__dict__['id']
    data = await db_get_book_by_id(f"{book_id}", db)
    assert data.status_code == 200

@pytest.mark.asyncio
async def test_add_book_db(db_test_env):
    _, db = await anext(db_test_env)
    json = {
        "title" : "Pal",
        "author" : "Arijit Singh",
        "genre" : "romantic",
        "availability" : 7
    }
    data = await db_add_book(BookCreateSchema(**json), db)

    assert data.status_code == 201

@pytest.mark.asyncio
async def test_update_book_db(db_test_env):
    book, db = await anext(db_test_env)
    data = await db_update_book(BookUpdateSchema(**{"title":"string"}),book.__dict__['id'],db)

    data = data.data.__dict__
    assert data['title'] == "string"

@pytest.mark.asyncio
async def test_delete_book_db(db_test_env):
    book, db = await anext(db_test_env)
    data = await db_delete_book(book.__dict__['id'],db)

    data = data.__dict__
    assert data['message'] == "Deleted Successfully"


@pytest.mark.asyncio
async def test_borrow_book_db(db_test_env):
    book, db = await anext(db_test_env)

    book_id = book.__dict__['id']

    data = await db_rent_book(book_id,db)

    available = data.data.__dict__['availability']

    assert available == 10