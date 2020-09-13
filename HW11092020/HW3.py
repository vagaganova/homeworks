class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self._income = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position
class Position(Worker):
    def __init__(self,name, surname, position,wage, bonus):
        super().__init__(name, surname, position,wage, bonus)
    def get_full_name(self):
        return self.name + self.surname
    def get_total_income(self):
        return self._income.get('wage',0) + self._income.get('bonus',0)
new_worker = Position('Valeria','Gaganova','developer',100000,5000)
print(new_worker.get_full_name())
print(new_worker.get_total_income())