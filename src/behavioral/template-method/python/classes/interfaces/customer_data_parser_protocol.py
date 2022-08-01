from abc import ABC, abstractmethod

from classes.interfaces.customer_data import CustomerData


class CustomerDataParserProtocol(ABC):
    def __init__(self, file_path: str) -> None:
        self.customer_data: list[CustomerData] = []
        self._file_path = file_path

    async def fix_customer_data(self) -> None:
        await self._parse_data()
        self._fix_cpf()

    def _fix_cpf(self) -> None:
        self.customer_data = \
            list(map(lambda customer_data: CustomerData(
                name=customer_data.name,
                age=customer_data.age,
                cpf=customer_data.cpf.replace('.', '').replace('-', '')
            ), self.customer_data))

    @abstractmethod
    async def _parse_data(self) -> list[CustomerData]:
        pass
