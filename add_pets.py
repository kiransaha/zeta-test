# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

import requests
import json

from petslib import PetsLib


class TestAddPets:
  def test_add_pets(self,):
    try:
      #preconfig
      petadd=PetsLib()
      pet_id=petadd.add_pets()
      petadd.validate_added_pet(pet_id)

    finally:
      pass


