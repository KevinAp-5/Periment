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

        self.guess_filter = ''
        self.b = ''
        self.rangerer = 118

        if self.guess_filter in ([''], ''):
            self.guess_filter = ['name', 'symbol', 'number']
        if self.b in ([''], ''):
            self.b = ['name', 'symbol', 'number', 'category', 'summary']

        try:
            with open(self.path) as table:  # Open the json
                self.data = json.load(table)
        except FileNotFoundError:
            print("Check the path of PeriodicTable or insert it on 'path'.")
        except Exception as error:
            print(f'Occurred a error: {error}')

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
        for counter in range(self.ranger):
            # Random mode
            if random is True:
                base = self.data['elements'][random_number[counter]]
            else:
                base = self.data['elements'][counter]

            if animation is True:
                self.anima()
            else: print('-' * 30)

            # check if the key exist in json
            for show_elements in self.b:
                if show_elements not in base:
                    self.b.remove(show_elements)

            for loop in range(len(self.b)):
                print(f'{self.b[loop]}: {base[self.b[loop]]}')
            print('')

    def guess(self, random=False, random_range=118):
        if random is True:
            random_number = list(range(0, random_range))
            shuffle(random_number)

        show = input('What to ask?: ').strip()

        for counter in range(self.ranger):
            # Randomize the elements
            if random is True:
                base = self.data['elements'][random_number[counter]]
            else:
                base = self.data['elements'][counter]

            # check if the key exist in json
            for keys in self.guess_filter:
                if keys not in base:
                    self.guess_filter.remove(keys)

            if show not in base:
                print(f"Error! {show} doesn't exist")
                break

            print(f'{show}: {base[show]}')

            # Remove the chosen option
            try:
                self.guess_filter.remove(show)
            except Exception:
                pass

            for loop in range(len(self.guess_filter)):
                it = base[self.guess_filter[loop]]
                print('-' * 30)

                try:
                    answer = input(f'{self.guess_filter[loop]}: ').strip()
                except KeyboardInterrupt:
                    print('\nGoodBye!')
                    exit()

                if isinstance(it, int):
                    answer = int(answer)
                elif isinstance(it, float):
                    answer = float(answer)

                if answer == it:
                    print(f'You got it!')
                else:
                    print(f'Wrong. {it}')
                    if answer.upper() == it:
                        print('You have to use uppercase too...')
            print('')

    def returning(self, called, name, animation=True):
        if type(name) == str: name = name.capitalize()
        for counter in range(self.ranger):
            base = self.data['elements'][counter]

            if not base[called] != name:
                if animation is True: self.guess_filternima()
                else: print('-' * 30)

                # Shows the keys and values
                for loop in range(len(self.b)):
                    print(f'{self.b[loop]}: {base[self.b[loop]]}')
                print('')
                break
