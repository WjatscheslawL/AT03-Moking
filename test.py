import pytest
from main import get_cat_image


def test_get_cat_image(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "id": "MTUwMjU0OQ",
        "url": "https://cdn2.thecatapi.com/images/MTUwMjU0OQ.jpg",
        "width": 500,
        "height": 332
    }
    cat_data = get_cat_image()

    assert cat_data == {
        "id": "MTUwMjU0OQ",
        "url": "https://cdn2.thecatapi.com/images/MTUwMjU0OQ.jpg",
        "width": 500,
        "height": 332
    }


def test_get_cat_image_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    cat_data = get_cat_image()
    assert cat_data == None
