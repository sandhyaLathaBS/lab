from datetime import date


class Greetings:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def show_greetings(self):
        today = date.today()
        age = self.age
        name = self.name
        hundthYear = today.year + (100 - age)
        print("Hai, %s You gonna live for 100 years lets cheers on %d th year...!" % (
            name, hundthYear))


name = str(input('Enter YOur name'))
age = int(input('Enter YOur age'))

Obj = Greetings(name, age)
Obj.show_greetings()
