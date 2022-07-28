class Warehouse:
    def __init__(self, count = 0):
        self.max_count = count
        self.eq_list = []

    def store(self, eq_list):
        self.eq_list.extend(eq_list)
        return eq_list

    def transfer(self, model, count1 = 0):
        self.max_count1 = count1
        self.model = model
        self.eq_tr_list = dict([('printer',Printer()), ('scaner',Scaner()), ('xerox',Xerox())])
        return eq_tr_list



class OfficeEquipment:
    def __init__(self, model, number):
        self.model = model
        self.number = number
        self.eq_list = dict([('printer',Printer()), ('scaner',Scaner()), ('xerox',Xerox())])


class Printer(OfficeEquipment):
    def __init__(self, number):
        super().__init__(number)

class Scaner(OfficeEquipment):
    def __init__(self, number):
        super().__init__(number)

class Xerox(OfficeEquipment):
    def __init__(self, number):
        super().__init__(number)

warehouse = Warehouse(1000)
printer = Printer(60)
scaner = Scaner(50)
xerox = Xerox(7)

print(eq_list)
Warehouse.transfer(printer,10)
print(eq_tr_list)


