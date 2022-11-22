import pytest

from ads.serializers import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ads_list(client):
    ads = AdFactory.create_batch(5)
    expected_data = {
        "count": 5,
        "next": None,
        "previous": None,
        "results": AdListSerializer(ads, many=True).data
    }
    response = client.get("/ad/")
    assert response.status_code == 200
    assert response.data == expected_data
