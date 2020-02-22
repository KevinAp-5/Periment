import json


class Periment:
    def __init__(self, show='', guess='', rang=118):
        # Json path
        self.file = '/home/kevin/Periment/periment/PeriodicTableJSON.json'
        self.a = guess
        self.rang = rang
        self.b = show

    def show(self):
        if self.b == [''] or self.b == '':
            self.b = ['name', 'symbol', 'number', 'category', 'summary']

        with open(self.file) as jsonnn:
            data = json.load(jsonnn)

        # Loop to show the elements
        for counter in range(self.rang):
            base = data['elements'][counter]
            print('-' * 30)
            # checks if the key exist
            for show_elements in self.b:
                if show_elements not in base:
                    self.b.remove(show_elements)

            for loop in range(len(self.b)):
                print(f'{self.b[loop]}: {base[self.b[loop]]}')
            print('')

    def guess(self):
        if self.a == [''] or self.a == '':
            self.a = ['name', 'symbol', 'number']

        with open(self.file) as jsonnn:
            data = json.load(jsonnn)

        show = input('What to show?: ').strip()

        for counter in range(self.rang):
            base = data['elements'][counter]

            if show not in base:
                print(f"Error! {show} doesn't exist")
                break

            print(f'{show}: {base[show]}')
            try:
                self.a.remove(show)
            except Exception:
                pass

            for loop in range(len(self.a)):
                it = base[self.a[loop]]
                print('-' * 30)
                print(self.a[loop], end='')
                answer = input(': ').strip()

                if answer == it:
                    print('You got it')
                else:
                    print(f'Wrong. {it}')
            print('')
