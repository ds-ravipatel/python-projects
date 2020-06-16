stores = [
    {
        'name': 'DMart',
        'items': [{'name': 'Chair', 'price': 900}]
    },
    {
        'name': 'Reliance Mart',
        'items': [{'name': 'Chair', 'price': 1000}]
    }
]



new_item = {'name': 'Towel', 'price': 500}


def searchstore(store_name):
    for store in stores:
        if store['name'] == store_name:
            #print(store)
            #print(store['items'])
            store['items'].append(new_item)
            #print(store['items'])
            for item in store['items']:
                if item['name'] == new_item['name']:
                    print(item)
    #print('Store not found in records.')

searchstore('DMart')

