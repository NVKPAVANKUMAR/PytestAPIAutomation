from api.client import APIClient
from helper.helper import FileClass

BRANDS_END = FileClass.get_property_from_file('BRANDS')


def test_get_all_brands_list():
    response = APIClient().get(BRANDS_END)
    assert response.status_code == 200
    assert len(response.json()["brands"]) > 0, 'List of brands is empty.'


def test_put_all_brands_list():
    response = APIClient().post(BRANDS_END)
    assert response.status_code == 200
    assert response.json()["message"] == 'This request method is not supported.', 'Error message does not match.'
