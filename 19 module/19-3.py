data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

print('1:')
for data_key in data:
    print(f'{data_key}: {data.get(data_key)}')

print('\n2:')
data['ETH']['total_diff'] = 100
print(f'ETH: {data["ETH"]}')

print('\n3:')
data['tokens'][0]['fst_token_info']['name'] = 'doge'
name = data['tokens'][0]['fst_token_info']['name']
print(f'fst_token_info-name: {name}')

print('\n4:')
total_out = 0
data['ETH']['total_out'] = total_out
for i_value in data['tokens']:
    i_value.pop('total_out')
print(data['ETH'])

print('\n5:')
data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')
print(data['tokens'][1]['sec_token_info']['total_price'])
