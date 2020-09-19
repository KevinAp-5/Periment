from random import shuffle
from time import sleep
import json
from sys import argv
from os import getcwd


class Periment:
    def __init__(self, show='', guess='', random=False, rang=118,
                path=f'{getcwd()}/PeriodicTableJSON.json'):
        # Json path
        self.path = path
        self.a = guess
        self.b = show
        self.rang = rang

        if self.a == [''] or self.a == '':
            self.a = ['name', 'symbol', 'number']
        if self.b == [''] or self.b == '':
            self.b = ['name', 'symbol', 'number', 'category', 'summary']
        try:
            with open(self.path) as jsonnn:  # Open the json
                self.data = json.load(jsonnn)
        except FileNotFoundError:
            print("Check the path of PeriodicTable or insert it on 'path'.")

    @staticmethod
    def anima():
        for x in ('-' * 50):
            print(x, end='', flush=True)
            sleep(0.03)
        print()

    def show(self, animation=False, random=False, random_range=119):
        if random is True:
            random_number = list(range(0, random_range))
            shuffle(random_number)

        # Loop to show the elements
        for counter in range(self.rang):
            # Random mode
            if random is True:
                base = self.data['elements'][random_number[counter]]
            else: base = self.data['elements'][counter]

            if animation is True: self.anima()
            else: print('-' * 30)

            # check if the key exist in json
            for show_elements in self.b:
                if show_elements not in base:
                    self.b.remove(show_elements)

            for loop in range(len(self.b)):
                print(f'{self.b[loop]}: {base[self.b[loop]]}')
            print('')

    def guess(self, random=False, random_range=119):
        if random is True:
            random_number = list(range(0, random_range))
            shuffle(random_number)

        show = input('What to ask?: ').strip()

        for counter in range(self.rang):
            # Randomize the elements
            if random is True:
                base = self.data['elements'][random_number[counter]]
            else: base = self.data['elements'][counter]

            # check if the key exist in json
            for keys in self.a:
                if keys not in base:
                    self.a.remove(keys)

            if show not in base:
                print(f"Error! {show} doesn't exist")
                break

            print(f'{show}: {base[show]}')

            # Remove the chosen option
            try:
                self.a.remove(show)
            except Exception:
                pass

            for loop in range(len(self.a)):
                it = base[self.a[loop]]
                print('-' * 30)
                answer = input(f'{self.a[loop]}: ').strip()

                if answer.isdigit() and type(it) == int:
                    answer = int(answer)
                elif answer.isdigit() and type(it) == float:
                    answer = float(answer)

                if answer == it:
                    print(f'You got it!\n')
                else:
                    print(f'Wrong. {it}')
            print('')

    def returning(self, called, name, animation=True):
        if type(name) == str: name = name.capitalize()

        for counter in range(self.rang):
            base = self.data['elements'][counter]

            if not base[called] != name:
                if animation is True: self.anima()
                else: print('-' * 30)

                # Shows the keys and values
                for loop in range(len(self.b)):
                    print(f'{self.b[loop]}: {base[self.b[loop]]}')
                print('')
                break
