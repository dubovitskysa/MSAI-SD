# list  of available  goods  [goodName quantity, price]


class VendingMachine:

    def __init__(self):
        self.vm_inventory = {
            "goods": {
                # goods:  quantity , price
                'mars': [201, 10],
                'snickers': [202, 15],
                'snickersXXL': [303, 20],
                'bounty': [150, 20],
                'cookie': [101, 20],
                'dietCookie': [122, 20],
                'pythonBook': [250, 20]
            },
            'cashier': 100,
            'purshase_history': []
        }

    def clear_inventory(self):
        for good in self.vm_inventory['goods']:
            self.vm_inventory['goods'][good][0] = 0

    def add_good(self, good_name, qnt):
        goods = self.vm_inventory['goods']
        if good_name in goods:
            good = goods[good_name]
            good[0] += qnt
        else:
            print('The  good ', good_name, 'is  not  in inventory, skipped')

    def sub_good(self, good_name, qnt):
        goods = self.vm_inventory['goods']
        if good_name in goods:
            good = goods[good_name]

            if good[0] >= qnt:
                good[0] -= qnt
            else:
                raise ValueError('There  are  not enough amount of', good_name, ' to extract ', qnt,
                                 'Skipped')
        else:
            raise ValueError('The  good ', good_name, 'is  not  in inventory, skipped ')

    def __sub__(self, vm_other):

        result_vm = VendingMachine()
        result_vm.clear_inventory()

        goods = self.vm_inventory['goods']
        goods_other = vm_other.vm_inventory['goods']
        result_goods = result_vm.vm_inventory['goods']

        cashier = self.vm_inventory['cashier']
        cashier_other = vm_other.vm_inventory['cashier']
        cashier_result = result_vm.vm_inventory['cashier']

        for good_name_other in goods_other.keys():
            if good_name_other in goods.keys():
                if goods[good_name_other][0] >= goods_other[good_name_other][0]:
                    result_goods[good_name_other] = goods[good_name_other][0] - \
                                                    goods_other[good_name_other][0]
                else:
                    print('The quantity  of ', \
                          good_name_other, \
                          'in source inventory is less then subtracted  value. Set  results to 0 ', \
                          goods[good_name_other][0], 'and ', [good_name_other][0])
                    result_goods[good_name_other] = 0
            else:
                print('This vending machine does not contain', good_name_other, 'Skipped')

        if cashier >= cashier_other:
            result_vm.vm_inventory['cashier'] = cashier - cashier_other
        else:
            print('The  amount  of  money in source cashier is  less  that ' + \
                  ' subtracted  value. Set  result  to 0',
                  cashier, 'and', cashier_other)
            result_vm.vm_inventory['cashier'] = 0

        return result_vm

    def __add__(self, vm_other):

        result_vm = VendingMachine()
        result_vm.clear_inventory()

        goods = self.vm_inventory['goods']
        goods_other = vm_other.vm_inventory['goods']
        result_goods = result_vm.vm_inventory['goods']

        cashier = self.vm_inventory['cashier']
        cashier_other = vm_other.vm_inventory['cashier']
        cashier_result = result_vm.vm_inventory['cashier']

        for good_name_other in goods_other.keys():
            if good_name_other in goods.keys():
                result_goods[good_name_other] = goods[good_name_other][0] + \
                                                goods_other[good_name_other][0]
            else:
                print('Good ', good_name_other, ' is  not  is inventory,'
                                                ' of  source, skipping add operation')
        result_vm.vm_inventory['cashier'] = cashier + cashier_other

        return result_vm

    def union(self, vm_other):

        result_vm = VendingMachine()
        result_vm.clear_inventory()

        goods = self.vm_inventory['goods']
        goods_other = vm_other.vm_inventory['goods']
        result_goods = result_vm.vm_inventory['goods']

        cashier = self.vm_inventory['cashier']
        cashier_other = vm_other.vm_inventory['cashier']
        cashier_result = result_vm.vm_inventory['cashier']

        for good_name_other in goods_other.keys():
            if good_name_other in goods.keys():
                result_goods[good_name_other] = goods[good_name_other][0] + \
                                                goods_other[good_name_other][0]
            else:
                result_goods[good_name_other] = goods_other[good_name_other][0]

        result_vm.vm_inventory['cashier'] = cashier + cashier_other

        return result_vm

    def intersection(self, vm_other):

        result_vm = VendingMachine()
        result_vm.clear_inventory()

        goods = self.vm_inventory['goods']
        goods_other = vm_other.vm_inventory['goods']
        result_goods = result_vm.vm_inventory['goods']

        cashier = self.vm_inventory['cashier']
        cashier_other = vm_other.vm_inventory['cashier']
        cashier_result = result_vm.vm_inventory['cashier']

        for good_name_other in goods_other.keys():
            if good_name_other in goods.keys():
                result_goods[good_name_other] = min(goods[good_name_other][0], \
                                                    goods_other[good_name_other][0])

        result_vm.vm_inventory['cashier'] = min(cashier, cashier_other)

        return result_vm

    def __gt__(self, other):
        return self.vm_inventory['cashier'] > other.vm_inventory['cashier']
    def __ge__(self, other):
        return self.vm_inventory['cashier'] >= other.vm_inventory['cashier']
    def __lt__(self, other):
        return self.vm_inventory['cashier'] < other.vm_inventory['cashier']
    def __le__(self, other):
        return self.vm_inventory['cashier'] <= other.vm_inventory['cashier']


vd1 = VendingMachine()
vd2 = VendingMachine()

vd1.add_good('mars', 10)

vd2.vm_inventory['goods']['mmars'] = (111, 10)
vd2.vm_inventory['cashier'] = 20

print('vd1', vd1.vm_inventory)
print('vd2', vd2.vm_inventory)
print('')


print('Diff: ', (vd1 - vd2).vm_inventory)
print('Sum:', (vd1 + vd2).vm_inventory)
print('Union:', vd1.union(vd2).vm_inventory)
print('Intersection', vd1.intersection(vd2).vm_inventory)

print('')
print('VedMashine1 > VedMashine12 : ', vd1 > vd2)
print('VedMashine1 >= VedMashine12 : ', vd1 >= vd2)
print('VedMashine1 < VedMashine12 : ', vd1 < vd2)
print('VedMashine1 <= VedMashine12 : ', vd1 <= vd2)
