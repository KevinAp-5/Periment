import json


class Periment:
    def __init__(self, toshow='', rang=119):
        # Json path
        self.file = '/home/kevin/Periment/periment/PeriodicTableJSON.json'

        if toshow != list:
            self.toshow = []
            self.toshow.append(toshow)
        else:
            self.toshow = toshow
        self.rang = rang

    def show(self):
        if self.toshow == ['']:
            self.toshow = ['name', 'symbol', 'number', 'summary']

        with open(self.file) as jsonnn:
            data = json.load(jsonnn)

        # Loop to show the elements
        for counter in range(self.rang):
            base = data['elements'][counter]
            for c in range(len(self.toshow)):
                print(base[self.toshow[c]])
            print('')
            print('-' * 30)
