



# Section 6. Project part
# list  of available  goods  [goodName quantity, price]
vending_machine = {
    'goods': {
        'mars': [200, 10],
        'snickers': [200, 15],
        'snickersXXL': [300, 20],
        'bounty': [150, 20],
        'cookie': [100, 20],
        'dietCookie': [120, 20],
        'pythonBook': [250, 20]
    },
    'cashier': 100,
    'purchase_history': [],

}


def buy_something(good_name: str, money: int) -> None:
    #  skip a lot  of  checking ( if  such  good  exists,
    #  quantity  is  enough, ..)

    vending_machine['goods'][good_name][0] -= 1
    vending_machine['cashier'] += vending_machine['goods'][good_name][1]
    vending_machine['purchase_history'].append([good_name, 1])

    if money > vending_machine['goods'][good_name][1]:
        cash_back = money - vending_machine['goods'][good_name][1]
        print('cash back:', str(cash_back))


def add_goods(good_name: str, quantity: int, price: int = 10):
    if quantity <= 0:
        raise ValueError('Invalid  number quantity  for this  operation')
    if price <= 0:
        raise ValueError('Invalid  number quantity  for this  operation')

    if vending_machine['goods'].keys().__contains__(good_name):
        vending_machine['goods'][good_name][0] += quantity
    else:
        vending_machine['goods'][good_name] = [quantity, price]


def purchase_goods(good_name: str, quantity: int):
    if quantity <= 0:
        raise ValueError('Invalid  number quantity  for this  operation')
    if not vending_machine['goods'].keys().__contains__(good_name):
        raise ValueError('not  such  goods ', good_name)
    if vending_machine['goods'][good_name][0] < quantity:
        raise ValueError('There are  nor  enough ', good_name)

    vending_machine['goods'][good_name][0] -= quantity
    vending_machine['cashier'] += quantity * \
                                  vending_machine['goods'][good_name][1]
    vending_machine['purchase_history'].append([good_name, 1])


def add_cash(money: int) -> None:
    if money <= 0:
        raise ValueError('Incorrect  amount  of  money ' + str(money))
    vending_machine['cashier'] += money


def pick_cash(money: int) -> None:
    if money <= 0:
        raise ValueError('Incorrect  amount  of  money ' + str(money))
    vending_machine['cashier'] -= money


print(vending_machine)
# add_goods('mars',10, 10)
purchase_goods('snickers', 10)
# buy_something('mars', 20)
# buy_something('mars', 30)
# buy_something('pythonBook', 30)
print(vending_machine)
add_cash(200)
print(vending_machine)
