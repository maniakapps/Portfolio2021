grocery_item = {}
grocery_history = []

quantity = int(1)
stop = 'go'
item_name = 'milk'

while stop!='q':
    grocery_item = {'name':'milk', 'number':int(1), 'price':float(2.99)}
    grocery_item['name'] = input()
    grocery_item['number'] = input()
    grocery_item['price'] = input()
    stop = input()
    grocery_history.append(grocery_item)

grand_total = 0

for grocery_item in range