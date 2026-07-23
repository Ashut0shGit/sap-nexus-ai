import json

from pathlib import Path

from app.models.sap_object import SAPObject

class ObjectService:

    def __init__(self):
        
        data_path = Path(__file__).parent.parent / "data" / "objects.json"

        with open(data_path, "r") as file:
            self.object_data = json.load(file)

    def get_objects(self, transport_number: str) -> list[SAPObject]:

        objects = self.object_data.get(transport_number)

        if objects is None:
            return []

        return [
            SAPObject(**obj) 
            for obj in objects
            ]