import pytest
import requests
import json
id_zhora = 1


# GET request
def write_all():
    url = 'https://api.restful-api.dev/objects'
    response = requests.get(url)
    response_json = response.json()
    assert response.status_code == 200

    # assert "id" in str(response_json)
    assert "id" in response.text, "Expected string was not found in the response."

    print("Test passed: 'id' is in the response.")

# DU
# POST, GET ONE object, DELETE
# url ta ista len iny endpoint - ulozit URL
# POST vrati ID - urobit ID pristupne zo vsetkych funkcii

def get_one_object(id_pouzite_vo_funkcii):





write_all()
get_one_object(id_zhora)