class OfficeEquipment:
    def __init__(self,cost,inv_number):
        self.cost = cost
        self.inv_number = inv_number

class Printer(OfficeEquipment):
    def __init__(self,cost,inv_number,color_print = False):
        super().__init__(cost,inv_number)
        self.color_print = color_print

class Scanner(OfficeEquipment):
    def __init__(self,cost,inv_number,doubleside_scanning = True):
        super().__init__(cost,inv_number)
        self.doubleside_scanning = doubleside_scanning

class Xerox(OfficeEquipment):
    def __init__(self,cost,inv_number):
        super().__init__(cost,inv_number)

class OrgStore:
    def __init__(self,store_name):
        self.store_name = store_name
        self.store = {
            'printers': {},
            'scanners': {},
            'xeroxes': {},
            'other': {}
        }
        self.in_use = {}

    def __str__(self):
        return self.store_name + '\n' + \
               self.store.__str__()

    def procurement(self,orgs: OfficeEquipment):
        if isinstance(orgs,Printer):
            self.store['printers'][orgs.inv_number] = orgs
        elif isinstance(orgs,Scanner):
            self.store['scanners'][orgs.inv_number] = orgs
        elif isinstance(orgs,Xerox):
            self.store['xeroxes'][orgs.inv_number] = orgs
        else:
            self.store['other'][orgs.inv_number] = orgs

    def procurement(self,orgs: list):
        for org in orgs:
            if isinstance(org, Printer):
                self.store['printers'][org.inv_number] = org
            elif isinstance(org, Scanner):
                self.store['scanners'][org.inv_number] = org
            elif isinstance(org, Xerox):
                self.store['xeroxes'][org.inv_number] = org
            else:
                self.store['other'][org.inv_number] = org

    def send_to_department(self,inv_number):


MyStore = OrgStore('pth')
MyStore.procurement([Printer(12000,'1231231231'),Xerox(12000,'12312w1231'),Xerox(12000,'1231231231'),Scanner(12000,'1231231')])
print(MyStore)