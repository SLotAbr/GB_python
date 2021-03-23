from stores import Store


st_1 = Store('Main store')
st_2 = Store('Development department')
st_1.store_item(['Printer',12, 'HHY'])
st_1.store_item(['Printer',12, 'HHY'])
st_1.store_item(['Printer',23, 'HH1212'])
st_1.store_item(['Copier',18, 'chemical'])
st_1.contain
st_2.contain

st_2.store_item(st_1.get_item(['Printer',4, 'HH1212']))
st_2.store_item(st_1.get_item(['Printer',16, 'HH1212']))
st_2.store_item(st_1.get_item(['Copier',18, 'chemical']))
st_1.contain
st_2.contain
