from typing import List
from customer_data_parser import CustomerDataParser
from customer_data import CustomerData


class CustomerDataParserTxt(CustomerDataParser):
   
   async def _read_file(self) -> List[str]:
      with open(self._file_path, 'r') as file:
         return file.readlines()
   
   async def _parse_data(self) -> List[CustomerData]:
      raw_data = await self._read_file() 
      for line in raw_data:
         name, age, cpf = line.split('\t')
         self.customer_data.append(CustomerData(name, age, cpf.replace('\n', '')))
         
   
      
       



