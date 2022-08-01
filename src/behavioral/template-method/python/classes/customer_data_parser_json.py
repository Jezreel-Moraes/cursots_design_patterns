import json

from classes.interfaces.customer_data import CustomerData
from classes.interfaces.customer_data_parser_protocol import \
    CustomerDataParserProtocol


class CustomerDataParserJson(CustomerDataParserProtocol):

    async def _read_file(self) -> list[str]:
        with open(self._file_path, 'r') as file:
            data = json.load(file)
            return data

    async def _parse_data(self) -> None:
        raw_data: list[CustomerData] = await self._read_file()
        for customer in raw_data:
            name, age, cpf = customer.values()
            self.customer_data.append(CustomerData(name, age, cpf))
