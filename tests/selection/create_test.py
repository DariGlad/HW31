import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_selection_create(client, user, access_token):
    ads = AdFactory.create_batch(5)
    data = {
        "name": "test",
        "owner": user.pk,
        "items": [ad.pk for ad in ads]
    }
    expected_data = {
        "id": 1,
        "name": "test",
        "owner": user.pk,
        "items": [ad.pk for ad in ads]
    }
    response = client.post(
        "/selection/",
        data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + access_token
    )
    assert response.status_code == 201
    assert response.data == expected_data
