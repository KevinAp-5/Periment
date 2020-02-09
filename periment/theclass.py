import json


class Periment:
    def __init__(self, toshow='', rang=119):
        self.file = '/home/kevin/Periment/periment/PeriodicTableJSON.json'
        if toshow != list:
            self.toshow = []
            self.toshow.append(toshow)
        else:
            self.toshow = toshow
        self.rang = rang

    def show(self):
        if self.toshow == []:
            self.toshow = ['name', 'symbol', 'number']

        with open(self.file) as jsonnn:
            data = json.load(jsonnn)

        for counter in range(self.rang):
            base = data['elements'][counter]
            items = base[self.toshow[0]]
            print(items)
