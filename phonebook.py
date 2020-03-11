class PhoneBook():
    def __init__(self):
        self._numbers = {}

    def add(self, name, number):
        self._numbers[name] = number

    def lookup(self, name):
        return self._numbers[name]

    def is_consistent(self):
        for name1, number1 in self._numbers.items():
            for name2, number2 in self._numbers.items():
                if name1 == name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True
