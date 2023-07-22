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

    def index_fixer(self, index):
        if index >= 120:
            return 118
        else:
            return index-1

    def filter_element(self, elements):
        new_elements = dict()
        for element_filter in self.filter:
            new_elements.update({element_filter: elements.get(element_filter)})
        return new_elements

    def show(self, index_limit, animation=False, random=False):
        index_limit = self.index_fixer(index_limit)+1

        element_base = self.data['elements']
        if random:
            shuffle(element_base)
        element_base = element_base[0:index_limit]

        for element in element_base:
            self.anima(animation)
            for label, content in self.filter_element(element).items():
                print(f'{label}: {content}')

    def returning(self, index, animation=True):
        element = self.data['elements'][self.index_fixer(index)]

        new_elements = self.filter_elements(element)

        self.anima(animation)
        for label, content in new_elements.items():
            print(f'{label}: {content}')
        self.anima(animation)

    def set_filter(self, *args):
        self.filter = args

