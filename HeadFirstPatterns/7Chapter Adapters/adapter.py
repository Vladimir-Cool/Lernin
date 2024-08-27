from base_duck import Duck
from base_turkey import Turkey


class TurkeyAdapterToDuck(Duck):
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()


class DuckAdapterToTurkey(Turkey):
    def __init__(self, duck: Duck):
        self.duck = duck

    def gobble(self):
        self.duck.quack()

    def fly(self):
        self.duck.fly()
