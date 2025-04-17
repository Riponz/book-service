import pytest
from user_service.app.schemas.user import UserCreateSchema, UserUpdateSchema
from user_service.app.controllers.users.add import add_user
from user_service.app.controllers.users.get import all_users
from user_service.app.controllers.users.update import update_user
from user_service.app.controllers.users.delete import delete_user
from user_service.app.controllers.users.rent import rent_book
from unittest.mock import AsyncMock, patch
from fastapi import HTTPException
from user_service.app.exception_handlers import UserNotFoundException




@pytest.mark.asyncio
async def test_get_users_db(db_test_env):
    _, db = await anext(db_test_env)
    data = await all_users(db)
    assert data.data[0].name == "Diganta"
    assert data.data[0].username == "dig"



@pytest.mark.asyncio
async def test_add_user_db(db_test_env):
    _, db = await anext(db_test_env)
    json = {
        "name" : "Pal",
        "email" : "A@gmail.com",
        "username" : "romantic",
        "password" : "12345"
    }
    data = await add_user(UserCreateSchema(**json), db)

    assert data.status_code == 201

@pytest.mark.asyncio
async def test_update_book_db(db_test_env):
    user, db = await anext(db_test_env)
    data = await update_user(UserUpdateSchema(**{"name": "diganta"}), user.__dict__['id'], db)

    data = data.data.__dict__
    assert data['name'] == "diganta"

@pytest.mark.asyncio
async def test_delete_book_db(db_test_env):
    user, db = await anext(db_test_env)
    data = await delete_user(user.__dict__['id'],db)

    data = data.__dict__
    assert data['status_code'] == 204


@pytest.mark.asyncio
async def test_rent_book_success(test_env, client):
    new_user, db = await anext(test_env)
    user_id = new_user.__dict__['id']

    with patch("user_service.app.controllers.users.rent.httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
        with patch("user_service.app.controllers.users.rent.httpx.AsyncClient.patch", new_callable=AsyncMock) as mock_patch:
            mock_get.return_value.status_code = 200
            mock_patch.return_value.status_code = 200

            result = await rent_book(user_id, "book1", db)

            assert result.status_code == 200
            assert result.message == "rent successfull"
            assert result.book == "book1"

@pytest.mark.asyncio
async def test_rent_book_user_not_found(test_env, client):
    new_user, db = await anext(test_env)

    with pytest.raises(UserNotFoundException):
        await rent_book("invalid_user", "book1", db)
#
@pytest.mark.asyncio
async def test_rent_book_book_not_found(test_env, client):
    new_user, db = await anext(test_env)
    user_id = new_user.__dict__['id']

    with patch("user_service.app.controllers.users.rent.httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value.status_code = 404

        with pytest.raises(HTTPException) as exc:
            await rent_book(user_id, "invalid_book", db)
            assert exc.value.status_code == 404
#
@pytest.mark.asyncio
async def test_rent_book_not_available(test_env):
    new_user, db = await anext(test_env)
    user_id = new_user.__dict__['id']

    with patch("user_service.app.controllers.users.rent.httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
        with patch("user_service.app.controllers.users.rent.httpx.AsyncClient.patch", new_callable=AsyncMock) as mock_patch:
            mock_get.return_value.status_code = 200
            mock_patch.return_value.status_code = 404

            with pytest.raises(HTTPException) as exc:
                await rent_book(user_id, "book1", db)

            assert exc.value.status_code == 404