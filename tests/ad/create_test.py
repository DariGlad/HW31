import pytest


@pytest.mark.django_db
def test_ad_creat(client, user, category, access_token):
    data = {
        "author": user.pk,
        "category": category.pk,
        "name": "test_ad_name",
        "price": 2500,
        "description": "",
        "is_published": False
    }
    expected_data = {
        "id": 1,
        "name": "test_ad_name",
        "price": 2500,
        "description": "",
        "is_published": False,
        "image": None,
        "author": 1,
        "category": 1
    }

    response = client.post(
        "/ad/",
        data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + access_token
    )
    assert response.status_code == 201
    assert response.data == expected_data
