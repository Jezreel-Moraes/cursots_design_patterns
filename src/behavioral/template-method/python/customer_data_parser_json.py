from typing import List
from customer_data_parser import CustomerDataParser
from customer_data import CustomerData
import json

class CustomerDataParserJson(CustomerDataParser):
   
   async def _read_file(self) -> List[str]:
      with open(self._file_path, 'r') as file:
         data = json.load(file)
         return data
      
   async def _parse_data(self) -> List[CustomerData]:
      raw_data = await self._read_file() 
      for customer in raw_data:
         name, age, cpf = customer.values()
         self.customer_data.append(CustomerData(name, age, cpf))
         
   
      
       



