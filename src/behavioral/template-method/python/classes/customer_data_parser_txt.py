from classes.interfaces.customer_data import CustomerData
from classes.interfaces.customer_data_parser_protocol import \
    CustomerDataParserProtocol


class CustomerDataParserTxt(CustomerDataParserProtocol):

    async def _read_file(self) -> list[str]:
        with open(self._file_path, 'r') as file:
            return file.readlines()

    async def _parse_data(self) -> None:
        raw_data = await self._read_file()
        for line in raw_data:
            name, age, cpf = line.split('\t')
            self.customer_data.append(CustomerData(
                name, age, cpf.replace('\n', '')))
