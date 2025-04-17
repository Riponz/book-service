import pytest
from unittest.mock import AsyncMock, patch

# health check
@pytest.mark.asyncio
async def test_health_check(test_env, client):
    response = client.get("/api/v1/users/health")
    assert response.json()['health'] == 'OK'
    # print(response.json())


# get all users
@pytest.mark.asyncio
async def test_get_users_api(test_env, client):
    response = client.get("/api/v1/users/")
    assert response.status_code == 200

# test add user
@pytest.mark.asyncio
async def test_add_user_api(test_env, client):
    response = client.post("/api/v1/users/add", json={
        "name": "Diganta",
        "username": "dig",
        "email": "dig@gmail.com",
        "password": "12345"
    })
    assert response.status_code == 201


# add same user
@pytest.mark.asyncio
async def test_add_same_user_api(test_env, client):
    client.post("/api/v1/users/add", json={
        "name": "Diganta",
        "username": "dig",
        "email": "dig@gmail.com",
        "password": "12345"
    })

    response = client.post("/api/v1/users/add", json={
        "name": "Diganta",
        "username": "dig",
        "email": "dig@gmail.com",
        "password": "12345"
    })

    assert response.status_code == 400



# update user
@pytest.mark.asyncio
async def test_update_user_api(test_env, client):
    client.post("/register", json={
        "name": "Diganta",
        "email": "dig@gmail.com",
        "username": "dig",
        "password": "12345"
    })

    response = client.post("/token", data={
        "username": "dig",
        "password": "12345"
    }, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    })

    token = response.json()["access_token"]
    print(token)

    response = client.get("/users/me", headers={
        "Authorization": f"Bearer {token}"
    })

    user_id = response.json()['id']

    update_response = client.patch(f"/api/v1/users/{user_id}/update", json={
        "name": "Lionel Messi"
    }, headers={
        "Authorization": f"Bearer {token}"
    })

    print(update_response.json())

    assert update_response.status_code == 200
    assert update_response.json()["data"]['name'] == "Lionel Messi"



# update user with wrong data type
@pytest.mark.asyncio
async def test_update_user_wrong_type_api(test_env, client):
    client.post("/register", json={
        "name": "Diganta",
        "email": "dig@gmail.com",
        "username": "dig",
        "password": "12345"
    })

    response = client.post("/token", data={
        "username": "dig",
        "password": "12345"
    }, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    })

    token = response.json()["access_token"]
    print(token)

    response = client.get("/users/me", headers={
        "Authorization": f"Bearer {token}"
    })

    user_id = response.json()['id']

    update_response = client.patch(f"/api/v1/users/{user_id}/update", json={
        "name": 123
    }, headers={
        "Authorization": f"Bearer {token}"
    })

    print(update_response.json())

    assert update_response.status_code == 400



# delete a user
@pytest.mark.asyncio
async def test_delete_user_api(test_env, client):
    client.post("/register", json={
        "name": "Diganta",
        "email": "dig@gmail.com",
        "username": "dig",
        "password": "12345"
    })

    response = client.post("/token", data={
        "username": "dig",
        "password": "12345"
    }, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    })

    token = response.json()["access_token"]
    print(token)

    response = client.get("/users/me", headers={
        "Authorization": f"Bearer {token}"
    })

    user_id = response.json()['id']

    update_response = client.delete(f"/api/v1/users/{user_id}/delete", headers={
        "Authorization": f"Bearer {token}"
    })


    assert update_response.status_code == 204




# rent book user not found
@pytest.mark.asyncio
async def test_rent_book_api_user_not_found(test_env, client):
    new_user, db = await anext(test_env)
    user_id = new_user.__dict__['id']

    response = client.post(f"/{user_id}/rent/book1")
    assert response.status_code == 404
