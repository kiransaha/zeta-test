import json

import requests


class PetsLib:
    def add_pets(self):
        headers = {"Content-Type": "application/json"}
        payload = {
            "id": 0,
            "category": {
                "id": "2",
                "name": "dog"
            },
            "name": "Jonny",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }

        resp = requests.post(url="https://petstore.swagger.io/v2/pet", data=json.dumps(payload), headers=headers)
        print(resp.content)
        print(resp.status_code)
        # validate

        if resp.status_code == 200:

            return json.loads(resp.content).get("id")
        else:
            raise Exception(f"status code {resp.status_code} content {resp.content}")

    def validate_added_pet(self, pet_id):
        url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.content
        else:
            raise Exception(f"status code {resp.status_code} content {resp.content}")
