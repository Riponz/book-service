import pytest

@pytest.mark.asyncio
async def test_get_books_api(test_env, client):
    response = client.get("/api/v1/books/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_book_by_title_api(test_env, client):
    book, db = await anext(test_env)
    book_id = book.__dict__['id']
    response = client.get(f"/api/v1/books/{book_id}")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_book_by_wrong_title_api(test_env, client):
    _, db = await anext(test_env)
    response = client.get(f"/api/v1/books/{"6e1b2f18-8c77-47a9-bc24-213f9c1b7e80"}")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_add_book_api(test_env, client):
    response = client.post("/api/v1/books", json={
        "title" : "Pal",
        "author" : "Arijit Singh",
        "genre" : "romantic",
        "availability" : 7
    })
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_add_book_incorrect_type_api(test_env, client):
    response = client.post("/api/v1/books", json={
        "title" : "Pal",
        "author" : 1,
        "genre" : "romantic",
        "availability" : 7
    })
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_update_book_api(test_env, client):
    book, db = await anext(test_env)
    book_id = book.__dict__['id']
    response = client.put(f"/api/v1/books/{book_id}/update", json={
        "title" : "Sudhu Tomari Jonne"
    })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_book_wrong_id_api(test_env, client):
    response = client.put(f"/api/v1/books/{"6e1b2f18-8c77-47a9-bc24-213f9c1b7e80"}/update", json={
        "title" : "Sudhu Tomari Jonne"
    })
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_update_book_incorrect_type_api(test_env, client):
    book, db = await anext(test_env)
    book_id = book.__dict__['id']
    response = client.put(f"/api/v1/books/{book_id}/update", json={
        "title" : 1
    })
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_delete_book_api(test_env, client):
    book, db = await anext(test_env)
    book_id = book.__dict__['id']
    response = client.delete(f"/api/v1/books/{book_id}/delete")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_delete_book_wrong_id_api(test_env, client):
    response = client.delete(f"/api/v1/books/{"invalid"}/delete")
    assert response.status_code == 404



@pytest.mark.asyncio
async def test_borrow_book_api(test_env, client):
    book, _ = await anext(test_env)
    book_id = book.__dict__['id']
    response = client.patch(f"/api/v1/books/{book_id}/rent")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_borrow_book_wrong_id_api(test_env, client):
    response = client.patch(f"/api/v1/books/{"6e1b2f18-8c77-47a9-bc24-213f9c1b7e80"}/rent")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_borrow_book_zero_aval_api(test_env_zero_aval, client):
    book, _ = await anext(test_env_zero_aval)
    book_id = book.__dict__['id']
    response = client.patch(f"/api/v1/books/{book_id}/rent")
    assert response.status_code == 400