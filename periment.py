import json
from os import getcwd
from time import sleep
from random import shuffle


class Periment:
    def __init__(self):
        self.path = f'{getcwd()}/PeriodicTableJSON.json'
        self.filter = ['name', 'symbol', 'number', 'category', 'summary']
        self.data = self.open_file()

    def open_file(self):
        try:
            with open(self.path) as table:  # Open the json
                return json.load(table)
        except FileNotFoundError:
            print("Check the path of PeriodicTable or insert it on 'path'.")
            exit()

    @staticmethod
    def anima(speed=True):
        for item in ('-' * 50):
            print(item, end='', flush=True)
            try:
                sleep(0 if speed is False else 0.02)
            except KeyboardInterrupt:
                exit()
        print()

    def show(self, _range=119, animation=False, random=False):
        if random is True:
            list_number = list(range(0, _range))
            shuffle(list_number)
        else:
            list_number = list(range(_range))

        # Loop to show the elements
        for counter in list_number:
            base = self.data['elements'][counter]
            self.anima(slow=animation)

            # check if the key exists in json
            for show_elements in self.filter:
                if show_elements not in base:
                    self.filter.remove(show_elements)

            for loop in range(len(self.filter)):
                print(f'{self.filter[loop]}: {base[self.filter[loop]]}')

            if animation is True:
                sleep(2)
            print()

    def returning(self, index, animation=True):
        element = self.data['elements'][118 if index >= 120 else index-1]

        new_elements = dict()
        for element_filter in self.filter:
            new_elements.update({element_filter: element.get(element_filter)})

        self.anima(animation)
        for label, content in new_elements.items():
            print(f'{label}: {content}')
        self.anima(animation)

    def set_filter(self, *args):
        self.filter = args
