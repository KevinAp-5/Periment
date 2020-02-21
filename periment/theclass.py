import json


class Periment:
    def __init__(self, toshow='', rang=118):
        # Json path
        self.file = '/home/kevin/Periment/periment/PeriodicTableJSON.json'
        self.show = toshow
        self.rang = rang

    def show(self):
        if self.show == [''] or self.show == '':
            self.show = ['name', 'symbol', 'number', 'category', 'summary']

        with open(self.file) as jsonnn:
            data = json.load(jsonnn)

        # Loop to show the elements
        for counter in range(self.rang):
            base = data['elements'][counter]
            print('-' * 30)
            # checks if the key exist
            for c in self.show:
                if c not in base:
                    self.show.remove(c)

            for c in range(len(self.show)):
                print(f'{self.toshow[c]}: {base[self.toshow[c]]}')
            print('')
