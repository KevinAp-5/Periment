import json


class Perimemo:
    def __init__(self):
        self.file = '/home/kevin/python/perimemo/PeriodicTableJSON.json'
        self.show = ['name', 'number', 'symbol']

    def practice(self):
        with open(self.file) as jsonnn:
            data = json.load(jsonnn)

        for counter in range(118 + 1):
            name = data['elements'][counter][self.show[0]]
            number = data['elements'[counter]['number']]

            print(f'What is the {number} of {name}?')
            guess_number = int(input('>> '))

            if guess_number == number:
                print('You got it!')
                print(f'{name} -> {number}')

            elif guess_number != number:
                print('Nice try')

    def show(self):