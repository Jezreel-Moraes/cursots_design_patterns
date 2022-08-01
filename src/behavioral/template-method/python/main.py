from asyncio import run
from os import path

from classes.customer_data_parser_json import CustomerDataParserJson
from classes.customer_data_parser_txt import CustomerDataParserTxt


async def main():
    print('[TXT - Data Parser]:')
    file_path = path.join(path.dirname(__file__), 'files', 'customer.txt')
    customer_data_parser_txt = CustomerDataParserTxt(file_path)
    await customer_data_parser_txt.fix_customer_data()
    for customer in customer_data_parser_txt.customer_data:
        print(customer)

    print('')

    print('[JSON - Data Parser]:')
    file_path = path.join(path.dirname(__file__), 'files', 'customer.json')
    customer_data_parser_txt = CustomerDataParserJson(file_path)
    await customer_data_parser_txt.fix_customer_data()
    for customer in customer_data_parser_txt.customer_data:
        print(customer)

if __name__ == '__main__':
    run(main())
