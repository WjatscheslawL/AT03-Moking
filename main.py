import requests


def get_cat_image():
    url = f'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    if response.status_code == 200:
        cat_info = response.json()
        print(cat_info)
        return response.json()
    else:
        return None


get_cat_image()
