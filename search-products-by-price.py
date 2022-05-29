PRODUCTS = [
    {'name': 'Sour cream', 'price': 2.5, 'shop': 'Producty', 'vendor': 'Slabkin'},
    {'name': 'Cheese', 'price': 2.5, 'shop': 'Producty', 'vendor': 'Baba Anya'},
    {'name': 'Cheese', 'price': 1.6, 'shop': '5ka', 'vendor': 'Slabkin'},
    {'name': 'Kefir', 'price': 1.5, 'shop': 'AsiaOpt', 'vendor': 'G&M'},
    {'name': 'Sour cream', 'price': 1.9, 'shop': 'Silpo', 'vendor': 'Lidskoe'},
    {'name': 'Kefir', 'price': 1.6, 'shop': 'Producty', 'vendor': 'G&M'},
    {'name': 'Cheese', 'price': 1.7, 'shop': 'AsiaOpt', 'vendor': 'G&M'},
    {'name': 'Cheese', 'price': 1.7, 'shop': 'AsiaOpt', 'vendor': 'Lidskoe'},
    {'name': 'Milk', 'price': 2.3, 'shop': 'AsiaOpt', 'vendor': 'Lidskoe'},
    {'name': 'Kefir', 'price': 1.5, 'shop': '5ka', 'vendor': 'Slabkin'},
    {'name': 'Kefir', 'price': 1.7, 'shop': 'Producty', 'vendor': 'Slabkin'},
    {'name': 'Milk', 'price': 2.1, 'shop': '5ka', 'vendor': 'Lidskoe'},
    {'name': 'Milk', 'price': 2.2, 'shop': '5ka', 'vendor': 'Lidskoe'},
    {'name': 'Milk', 'price': 2.2, 'shop': '5ka', 'vendor': 'G&M'},
]
name = ["Milk", "Cheese", 'Kefir']
vendor = ['Lidskoe', 'Slabkin']

shops_all = list(set([name_shop.get("shop") for name_shop in PRODUCTS if name_shop.get("shop")]))


def shops_filter(shops_all):
    return list(filter(lambda shop: shop.get("shop") == shops_all, PRODUCTS))


shops_filter_result = list(map(shops_filter, shops_all))


def selection(shops_filter_result):
    return list(filter(lambda name_product: name_product.get("name") in name,
                       (list(filter(lambda name_vendor: name_vendor.get("vendor") in vendor, shops_filter_result)))))


z = list(filter(None, map(selection, shops_filter_result)))
for i in z:
    print(i)


