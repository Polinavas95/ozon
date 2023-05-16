# -*- coding: utf-8 -*-
from datetime import datetime

import pandas
import requests

from config import settings

HELP_DICT = {
    '/v2/product/list': None,
    # Вписать нужные product_id через , между []
    '/v2/product/info/list': {'product_id': [326670334], 'offer_id': [], 'sku': []},
    # Вписать нужный product_id
    '/v1/product/info/description': {'product_id': 326670334, 'offer_id': ''}
}
HEADERS = {
    'Client-Id': settings.client_id,
    'Api-Key': settings.api_key,
    'Content-Type': 'application/json'
}

ITEMS_METHODS = ['/v2/product/list', '/v2/product/info/list', ]

if __name__ == '__main__':
    method = '/v2/product/list'
    body = HELP_DICT[method] if HELP_DICT[method] else None
    r = requests.post(f'https://{settings.host}{method}', headers=HEADERS, json=body)
    if method in ITEMS_METHODS:
        result = r.json()['result']['items']
    else:
        result = r.json()['result']
    # print(result)

    try:
        # Конвертация результата в Excel
        file_name = f'tables/{method.replace("/", "_")}_{datetime.today().strftime("%d_%m_%Y")}.xlsx'
        pandas.DataFrame.from_dict(result).to_excel(file_name, engine='xlsxwriter')
        print('Successful conversion')
    except Exception as err:
        print(f'Get an Error: {err}')

