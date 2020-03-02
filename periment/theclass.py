from random import shuffle
import json


class Periment:
    def __init__(self, show='', guess='', random=False, rang=118):
        # Json path
        self.file = '/home/kevin/Periment/periment/PeriodicTableJSON.json'
        self.a = guess
        self.rang = rang
        self.b = show

        if self.a == [''] or self.a == '':
            self.a = ['name', 'symbol', 'number']
        if self.b == [''] or self.b == '':
            self.b = ['name', 'symbol', 'number', 'category', 'summary']

    def show(self, random=False, random_range=119):
        with open(self.file) as jsonnn:
            data = json.load(jsonnn)

        if random is True:
            random_number = list(range(0, random_range))
            shuffle(random_number)

        # Loop to show the elements
        for counter in range(self.rang):
            # Random mode
            if random is True:
                base = data['elements'][random_number[counter]]
            else:
                base = data['elements'][counter]
            print('-' * 30)

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

        with open(self.file) as jsonnn:
            data = json.load(jsonnn)

        show = input('What to ask?: ').strip()

        hit_counter = 0
        for counter in range(self.rang):
            # Randomize the elements
            if random is True:
                base = data['elements'][random_number[counter]]
            else:
                base = data['elements'][counter]

            # check if the key exist in json
            for hm in self.a:
                if hm not in base:
                    self.a.remove(hm)

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
                print(self.a[loop], end='')
                answer = input(': ').strip()

                if answer.isdigit() and type(it) == int:
                    answer = int(answer)
                elif answer.isdigit() and type(it) == float:
                    answer = float(answer)

                if answer == it:
                    hit_counter += 1
                    print(f'You got it\nhits: {hit_counter}')
                else:
                    print(f'Wrong. {it}')
            print(f'You hit {hit_counter} elements!')
            print('')
