import random

import pytest
import requests
import json
import Functions.cellPhoneStore
import Functions.randoms

ID = None
NAME = Functions.randoms.generate_random_string(5)  #random string
YEAR = Functions.randoms.random_year()
PRICE = Functions.randoms.random_price()
CPU_model = Functions.randoms.random_CPU()
Hard_disk_size =Functions.randoms.random_HD_size()

BODY_NEW_OBJECT = {
    "name": NAME,
    "data": {
        "year": YEAR,
        "price": PRICE,
        "CPU model": CPU_model,
        "Hard disk size": Hard_disk_size
    }
}

UPDATED_DATA = {
   "name": NAME,
   "data": {
      "year": 2019,
      "price": 2099.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "violet"
   }
}


# GET request
def write_all(endpoint):
    url = f"{Functions.cellPhoneStore.BASE_URL}/{endpoint}"
    response = requests.get(url)
    response_json = response.json()
    assert response.status_code == 200

    # assert "id" in str(response_json)
    assert "id" in response.text, "Expected string was not found in the response."

    print("Test passed: 'id' is in the response.")
    print(response.text)



# DU
# POST, GET ONE object, DELETE
# url ta ista len iny endpoint - ulozit URL
# POST vrati ID - urobit ID pristupne zo vsetkych funkcii
# v kazdom requeste skontrolovat telo: vsetky parametre - vyskladat
# rozdelit resources a testy - Functions = variables + random generovanie +
# skladanie json tu na zaciatku 
# asserts do kazdeho requestu


#POST new object
def post_new_object(endpoint, body):
    global ID
    global BODY_NEW_OBJECT
    url = f"{Functions.cellPhoneStore.BASE_URL}/{endpoint}"
    response = requests.post(url, json=body)

    assert response.status_code == 200
    if response.status_code == 200 or response.status_code == 201:
        response_data = response.json()

        ID = response_data.get("id")

        print(f'Id in response is {ID}')
    else:
        print(f"Error: {response.status_code}, message: {response.text}")

    assert "id" in response_data
    assert BODY_NEW_OBJECT["data"]["year"] == response_data["data"]["year"], f"Error! for YEAR, awaited response is: {BODY_NEW_OBJECT['data']['year']} , but response is: {response_data['data']['year']}"
    assert BODY_NEW_OBJECT["data"]["price"] == response_data["data"]["price"], f"Error! for PRICE, awaited response is: {BODY_NEW_OBJECT['data']['price']} , but response is: {response_data['data']['price']}"
    assert BODY_NEW_OBJECT["data"]["CPU model"] == response_data["data"]["CPU model"], f"Error! for CPU model, awaited response is: {BODY_NEW_OBJECT['data']['CPU model']} , but response is: {response_data['data']['CPU model']}"
    assert BODY_NEW_OBJECT["data"]["Hard disk size"] == response_data["data"]["Hard disk size"], f"Error! for Hard disk size, awaited response is: {BODY_NEW_OBJECT['data']['Hard disk size']} , but response is: {response_data['data']['Hard disk size']}"
    assert BODY_NEW_OBJECT["name"] == response_data["name"], f"Error! for Name, awaited response is: {BODY_NEW_OBJECT['name']} , but response is: response_data['name']"
    print(f"Test passed for POST")



 #  ******   DU - asserts na vsetko co sa vrati v response + ci sa id nachadza v response


#GET one object by ID
def get_id(endpoint, id):
    url = f"{Functions.cellPhoneStore.BASE_URL}/{endpoint}/{id}"
    response = requests.get(url)
    response_data = response.json()


    if response.status_code == 200:
        assert "id" in response_data
        assert id == response_data["id"], f"Error! for ID, awaited response is: {id} , but response is: {response_data['id']}"
        assert BODY_NEW_OBJECT["data"]["year"] == response_data["data"]["year"], f"Error! for YEAR, awaited response is: {BODY_NEW_OBJECT['data']['year']} , but response is: {response_data['data']['year']}"
        assert BODY_NEW_OBJECT["data"]["price"] == response_data["data"]["price"], f"Error! for PRICE, awaited response is: {BODY_NEW_OBJECT['data']['price']} , but response is: {response_data['data']['price']}"
        assert BODY_NEW_OBJECT["data"]["CPU model"] == response_data["data"]["CPU model"], f"Error! for CPU model, awaited response is: {BODY_NEW_OBJECT['data']['CPU model']} , but response is: {response_data['data']['CPU model']}"
        assert BODY_NEW_OBJECT["data"]["Hard disk size"] == response_data["data"]["Hard disk size"], f"Error! for Hard disk size, awaited response is: {BODY_NEW_OBJECT['data']['Hard disk size']} , but response is: {response_data['data']['Hard disk size']}"
        assert BODY_NEW_OBJECT["name"] == response_data["name"], f"Error! for Name, awaited response is: {BODY_NEW_OBJECT['name']} , but response is: response_data['name']"
        print(f"Test passed for GET")
    else:
        print(f"Response code is not 200 for GET")
    #print(response.text)

#PUT - change one parameter in a defined object
def put_color(endpoint, id, updated_data):
    url = f"{Functions.cellPhoneStore.BASE_URL}/{endpoint}/{id}"
    response = requests.put(url, json=updated_data)

    assert response.status_code == 200
    if response.status_code == 200 or response.status_code == 201:
        print(f"Update is succesfull: {response.json()}")

    else:
        print(f"Error: {response.status_code}, message: {response.text}")

#DELETE - delete object by ID
def delete_By_Id(endpoint, id):
    url = f"{Functions.cellPhoneStore.BASE_URL}/{endpoint}/{id}"
    response = requests.delete(url)

    if response.status_code == 200 or response.status_code == 201:
        print(f"Delete object with: {id} is succesfull: {response.json()}")

    else:
        print(f"Error: {response.status_code}, message: {response.text}")


def verify_deleted(endpoint, id):
    url = f"{Functions.cellPhoneStore.BASE_URL}/{endpoint}/{id}"
    response = requests.get(url)

    assert response.status_code == 400 or response.status_code == 404
    print(f"Test passed, id = {id} is not in list")
    print(response.text)


#******* RUN FUNCTIONS *******

#write_all(ENDPOINT_OBJECTS)


post_new_object(Functions.cellPhoneStore.ENDPOINT_OBJECTS,BODY_NEW_OBJECT)
get_id(Functions.cellPhoneStore.ENDPOINT_OBJECTS, ID)


# get_id(Functions.cellPhoneStore.ENDPOINT_OBJECTS, Functions.cellPhoneStore.ID)
# put_color(Functions.cellPhoneStore.ENDPOINT_OBJECTS, Functions.cellPhoneStore.ID, UPDATED_DATA)
# get_id(Functions.cellPhoneStore.ENDPOINT_OBJECTS, Functions.cellPhoneStore.ID)
# delete_By_Id(Functions.cellPhoneStore.ENDPOINT_OBJECTS, Functions.cellPhoneStore.ID)
# verify_deleted(Functions.cellPhoneStore.ENDPOINT_OBJECTS, Functions.cellPhoneStore.ID)