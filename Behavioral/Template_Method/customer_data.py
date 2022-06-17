from dataclasses import dataclass


@dataclass(frozen=True)
class CustomerData:
   name: str
   age: int
   cpf: str
   