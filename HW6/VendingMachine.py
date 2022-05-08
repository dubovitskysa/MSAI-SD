from Logger import Logger


class VendingMachineCashier:
    def __init__(self):
        self.amount = 100
        self.logger = Logger(self)

    def __sub__(self, cashier_other):

        cashier_result = VendingMachineCashier()

        if self.amount >= cashier_other.amount:
            cashier_result.amount = self.amount - cashier_other.amount
        else:
            self.logger.log_string(f'The  amount  of  money  in source cashier is  less  that '
                                   f' subtracted  value. Set  result  to 0 '
                                   )
            cashier_result.amount = 0
        return cashier_result

    def __add__(self, cashier_other):
        cashier_result = VendingMachineCashier()
        cashier_result.amount = self.amount + cashier_other.amount
        return cashier_result

    def union(self, inv_other):
        return self + inv_other

    def intersection(self, cashier_other):

        cashier_result = VendingMachineCashier()
        cashier_result.amount = min(self.amount, cashier_other.amount)
        return cashier_result

    def __gt__(self, cashier_other):
        return self.amount > cashier_other.amount

    def __ge__(self, cashier_other):
        return self.amount >= cashier_other.amount

    def __lt__(self, cashier_other):
        return self.amount < cashier_other.amount

    def __le__(self, cashier_other):
        return self.amount <= cashier_other.amount

    def to_string(self):
        return str(self.amount)


class VendingMachineInventory:
    def __init__(self):
        self.logger = Logger(self)
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
            'purchase_history': []
        }

    def clear_inventory(self):
        for good in self.vm_inventory['goods']:
            self.vm_inventory['goods'][good][0] = 0

    def add_good(self, good_name, qnt):
        goods = self.vm_inventory['goods']
        if good_name in goods:
            good = goods[good_name]
            good[0] += qnt
            result = True
        else:
            self.logger.log_string(f'The  good {good_name} is  not  in inventory, skipped')
            result = False

        return result

    def sub_good(self, good_name, qnt):
        goods = self.vm_inventory['goods']
        if good_name in goods:
            good = goods[good_name]
            if good[0] >= qnt:
                good[0] -= qnt

            else:
                raise ValueError(f'There  are  not enough amount of {good_name}, '
                                 f'to extract {qnt}, Skipped')
        else:
            raise ValueError(f'The  good ,{good_name},is  not  in inventory, skipped ')

    def __sub__(self, vm_other):

        result_inv = VendingMachineInventory()
        result_inv.clear_inventory()

        goods = self.vm_inventory['goods']
        goods_other = vm_other.vm_inventory['goods']
        result_goods = result_inv.vm_inventory['goods']

        for good_name_other in goods_other.keys():
            if good_name_other in goods.keys():
                if goods[good_name_other][0] >= goods_other[good_name_other][0]:
                    result_goods[good_name_other] = goods[good_name_other][0] - \
                                                    goods_other[good_name_other][0]
                else:
                    self.logger.log_string(f'The quantity  of {good_name_other}  in source '
                                           f'inventory is less then subtracted value. '
                                           f'Set  results to 0 {goods[good_name_other][0]}'
                                           f' and {[good_name_other][0]}'
                                           )
                    result_goods[good_name_other] = 0
            else:
                self.logger.log_string(f'This vending machine does '
                                       f'not contain {good_name_other} Skipped')

        return result_inv

    def __add__(self, inv_other):

        result_inv = VendingMachineInventory()
        result_inv.clear_inventory()

        goods = self.vm_inventory['goods']
        goods_other = inv_other.vm_inventory['goods']
        result_goods = result_inv.vm_inventory['goods']

        for good_name_other in goods_other.keys():
            if good_name_other in goods.keys():
                result_goods[good_name_other] = goods[good_name_other][0] + \
                                                goods_other[good_name_other][0]
            else:
                self.logger.log_string(f'Good {good_name_other}  is  not is in  inventory,'
                                       f' skipping add operation')

        return result_inv

    def union(self, inv_other):

        result_inv = VendingMachineInventory()
        result_inv.clear_inventory()

        goods = self.vm_inventory['goods']
        goods_other = inv_other.vm_inventory['goods']
        result_goods = result_inv.vm_inventory['goods']

        for good_name_other in goods_other.keys():
            if good_name_other in goods.keys():
                result_goods[good_name_other] = goods[good_name_other][0] + \
                                                goods_other[good_name_other][0]
            else:
                result_goods[good_name_other] = goods_other[good_name_other][0]

        return result_inv

    def intersection(self, inv_other):

        result_inv = VendingMachineInventory()
        result_inv.clear_inventory()

        goods = self.vm_inventory['goods']
        goods_other = inv_other.vm_inventory['goods']
        result_goods = result_inv.vm_inventory['goods']

        for good_name_other in goods_other.keys():
            if good_name_other in goods.keys():
                result_goods[good_name_other] = min(goods[good_name_other][0],
                                                    goods_other[good_name_other][0])

        return result_inv

    def to_string(self):
        return str(self.vm_inventory)


class VendingMachine:

    def __init__(self):
        self.logger = Logger(self)
        self.inventory = VendingMachineInventory()
        self.cashier = VendingMachineCashier()

    def clear_inventory(self):
        self.inventory.clear_inventory()

    def add_good(self, good_name, qnt):
        self.inventory.add_good(good_name, qnt)

    def sub_good(self, good_name, qnt):
        self.inventory.sub_good(good_name, qnt)

    def __sub__(self, vm_other):
        result_vm = VendingMachine()
        result_vm.inventory = self.inventory - vm_other.inventory
        result_vm.cashier = self.cashier - vm_other.cashier

        return result_vm

    def __add__(self, vm_other):
        result_vm = VendingMachine()
        result_vm.inventory = self.inventory + vm_other.inventory
        result_vm.cashier = self.cashier + vm_other.cashier
        return result_vm

    def union(self, vm_other):
        result_vm = VendingMachine()
        result_vm.clear_inventory()

        result_vm.inventory = self.inventory.union(vm_other.inventory)
        result_vm.cashier = self.cashier.union(vm_other.cashier)

        return result_vm

    def intersection(self, vm_other):
        result_vm = VendingMachine()
        result_vm.clear_inventory()

        result_vm.inventory = self.inventory.intersection(vm_other.inventory)
        result_vm.cashier = self.cashier.intersection(vm_other.cashier)

        return result_vm

    def __gt__(self, other_vm):
        return self.cashier > other_vm.cashier

    def __ge__(self, other_vm):
        return self.cashier >= other_vm.cashier

    def __lt__(self, other_vm):
        return self.cashier < other_vm.cashier

    def __le__(self, other_vm):
        return self.cashier <= other_vm.cashier

    def to_string(self):
        return f' Inventory: {self.inventory.to_string()} Cashier: {self.cashier.to_string()}'


vd1 = VendingMachine()
vd2 = VendingMachine()

vd1.add_good('mars', 10)

vd2.inventory.vm_inventory['goods']['mmars'] = (111, 10)
vd2.inventory.vm_inventory['cashier'] = 20

print('vd1', vd1.to_string())
print('vd2', vd2.to_string())
print('')

print('Diff: vd1 - vd2 ', (vd1 - vd2).to_string())
print('Sum:  vd1 + vd2', (vd1 + vd2).to_string())
print('Union: vd1 U vd2', vd1.union(vd2).to_string())
print('Intersection vd1 int vd2', vd1.intersection(vd2).to_string())

print('')
print('VedMachine1  > VedMachine12 : ', vd1 > vd2)
print('VedMachine1 >= VedMachine12 : ', vd1 >= vd2)
print('VedMachine1  < VedMachine12 : ', vd1 < vd2)
print('VedMachine1 <= VedMachine12 : ', vd1 <= vd2)
