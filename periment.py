import json
from os import getcwd
from time import sleep
from random import shuffle


class Periment:
    def __init__(self, path=None):
        # Json path
        if path is None:
            self.path = f'{getcwd()}/PeriodicTableJSON.json'
        else:
            self.path = path

        self.filter = ''

        if self.filter in ([''], ''):
            self.filter = ['name', 'symbol', 'number', 'category', 'summary']

        try:
            with open(self.path) as table:  # Open the json
                self.data = json.load(table)
        except FileNotFoundError:
            print("Check the path of PeriodicTable or insert it on 'path'.")
        except Exception as error:
            print(f'Occurred an error: {error}')

    @staticmethod
    def anima():
        for x in ('-' * 50):
            print(x, end='', flush=True)
            try:
                sleep(0.03)
            except KeyboardInterrupt:
                print()
                exit()
        print()

    def show(self, animation=False, random=False, _range=119):
        if random is True:
            list_number = list(range(0, _range))
            shuffle(list_number)
        else:
            list_number = list(range(_range))

        # Loop to show the elements
        for counter in list_number:
            base = self.data['elements'][counter]

            if animation is True:
                self.anima()
            else:
                print('-' * 30)

            # check if the key exist in json
            for show_elements in self.filter:
                if show_elements not in base:
                    self.filter.remove(show_elements)

            for loop in range(len(self.filter)):
                print(f'{self.filter[loop]}: {base[self.filter[loop]]}')
            print('')

    def returning(self, called, name, animation=False):
        if type(name) == str:
            name = name.capitalize()
        for counter in range(len(self.data['elements'])):
            base = self.data['elements'][counter]

            if not base[called] != name:
                if animation is True:
                    self.anima()
                else:
                    print('-' * 30)

                # Shows the keys and values
                for loop in range(len(self.filter)):
                    print(f'{self.filter[loop]}: {base[self.filter[loop]]}')
                print('')
                break

    def set_filter(self, *args):
        self.filter = args
