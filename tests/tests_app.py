from time import time

from fastapi import status
from fastapi.testclient import TestClient

from main import api

client = TestClient(api)
time_from = int(time())


def test_create_data():
    data = {"links": ["vk.ru", "yandex.ru", "vk.ru"]}
    response = client.post('/urls/visited_links', json=data)
    assert response.status_code == status.HTTP_200_OK
    print(response.json())
    assert response.json() == {"status": "ok"}


def test_bad_value_request():
    response = client.post('/urls/visited_links', json={"link": ["vk.ru"]})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_get_data():
    response = client.get('/urls/visited_domains')
    assert response.status_code == 200
    assert response.json() == {
        "domains": ["vk.ru", "yandex.ru"],
        "status": "ok",
    }


def test_get_data_with_params():
    response = client.get(
        f'/urls/visited_domains?from={time_from}&to={int(time())}'
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "domains": ["vk.ru", "yandex.ru"],
        "status": "ok",
    }


def test_get_response_with_error():
    response = client.get('/urls/visited_domains?from=hello&to=sber')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['status'] != "ok"


def test_post_response_with_error():
    response = client.post(
        '/urls/visited_links', json={"links": ["vk.ru", []]}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['status'] != "ok"
