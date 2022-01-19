import math
import sys


# Section 1. Recursion, call stack
def factorial_rec(x):
    if x == 0:
        return 1
    return x * factorial_rec(x - 1)


print(factorial_rec(30))

# 1.2 - Calculate 3000! Solve the problem you face without rewriting
sys.setrecursionlimit(350)
print('300!', factorial_rec(300))


# 1.3 What about 30000! calculation? Provide a non-recursive function
# #and compare the answer with math.factorial one
def factorial_non_recursion(x):
    if x == 0 or x == 1:
        return 1
    res = 1

    for i1 in range(1, x + 1):
        res = res * i1
    return res


result = factorial_non_recursion(30000)
result2 = math.factorial(30000)
print('compare  result:', result == result2)

age_spans = [
    {'age': '< 5', 'percent': 1.09}, {'age': '5 - 10', 'percent': 14.08},
    {'age': '11 - 17', 'percent': 53.06}, {'age': '18 - 24', 'percent': 24.1},
    {'age': '25 - 34', 'percent': 5.04}, {'age': '35 - 44', 'percent': 1.58},
    {'age': '45 - 54', 'percent': 0.65}, {'age': '55 - 64', 'percent': 0.29},
    {'age': '64 <', 'percent': 0.1}
]

# 2.1 - Section 2 solution
max_percent = 0
max_age = 0
for i in age_spans:
    if max_percent < i['percent']:
        max_percent = i['percent']
        max_age = i['age']
print(max_age)

# Section 3. "operator" module
# 3.1 - Section 3 solution
input_str = '3/2'
print(eval(input_str))

# Section 5. Programming paradigms
# 5.1 - Solve it in declarative style: provide solution based on loops *

rows, cols = 1, 4
array = [[0 for x in range(cols)] for y in range(rows)]
for i_row in range(rows):
    for i_cols in range(cols):
        array[i_row][i_cols] = (i_row + 1) * (i_cols + 1)
print(array)

# 5.2 - Solve it in functional style: one-string
# solution (excluding input reading) *
array2 = [[(i_rows + 1) * (i_cols + 1) for i_cols in range(cols)] for i_rows
          in range(rows)]
print(array2)

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
