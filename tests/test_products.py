from api.client import APIClient
from helper.helper import FileClass

PRODUCT_LIST = FileClass.get_property_from_file('PRODUCTS_LIST')
SEARCH_PRODUCT = FileClass.get_property_from_file('SEARCH')


def test_get_all_products_list():
    response = APIClient().get(PRODUCT_LIST)
    assert response.status_code == 200


def test_send_post_in_product_list():
    response = APIClient().post(PRODUCT_LIST)
    assert response.status_code == 200
    assert response.json()["message"] == 'This request method is not supported.', 'Error message does not match.'


def test_post_search_product_without_param():
    response = APIClient().post(SEARCH_PRODUCT)
    assert response.status_code == 200
    assert response.json()["message"] == 'Bad request, search_product parameter is missing in POST request.'
