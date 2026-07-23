import json
from pathlib import Path

from app.models.transport import Transport


class TransportService:

    def __init__(self):
        data_path = Path(__file__).parent.parent / "data" / "transports.json"

        with open(data_path, "r") as file:
            self.transport_data = json.load(file)

    def get_transports(self, cr_number: str) -> list[Transport]:

        transports = self.transport_data.get(cr_number)

        if transports is None:
            return []

        return [Transport(**transport) for transport in transports]