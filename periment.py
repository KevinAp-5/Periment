import json
from os import getcwd
from time import sleep
from random import shuffle


class Periment:
    def __init__(self, path=None):
        if path is None:
            self.path = f'{getcwd()}/PeriodicTableJSON.json'
        else:
            self.path = path

        self.filter = ['name', 'symbol', 'number', 'category', 'summary']

        try:
            with open(self.path) as table:  # Open the json
                self.data = json.load(table)
        except FileNotFoundError:
            print("Check the path of PeriodicTable or insert it on 'path'.")

    @staticmethod
    def anima(slow=True):
        sleep_time = 0 if slow is False else 0.02

        for item in ('-' * 50):
            print(item, end='', flush=True)
            try:
                sleep(sleep_time)
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

    def returning(self, called, name, animation=False):
        if type(name) == str:
            name = name.capitalize()

        for counter in range(len(self.data['elements'])):
            base = self.data['elements'][counter]
            if not base[called] != name:
                self.anima(slow=animation)
                # Show the keys and values
                for loop in range(len(self.filter)):
                    print(f'{self.filter[loop]}: {base[self.filter[loop]]}')
                if animation is True:
                    sleep(2)
                print()
                break

    def set_filter(self, *args):
        self.filter = args

