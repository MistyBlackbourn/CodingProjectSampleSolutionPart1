from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from datetime import datetime
import time
from trip import *
from currency import *


class CurrencyConverterApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.location_list = []
        self.trip_origin = ""
        self.home_to_target = ""
        self.target_to_home = ""
        self.country = ""
        self.date_string = ""
        self.target_currency = ()
        self.home_currency = ()

    def build(self):
        Window.size = 300, 500
        Window.clearcolor = (1, .5, 0, 1)
        self.title = "Currency Converter"
        self.root = Builder.load_file('gui.kv')
        return self.root

    def trip_details(self):
        file = open('config.txt', mode='r')
        self.trip_origin = file.readline().strip()
        for line in file:
            details = line.strip().split(',')
            details = tuple(details)
            self.location_list.append(details[0])
        file.close()
        return self.location_list

    def current_location(self):
        file = open('config.txt', mode='r')
        details = []
        file.readline()
        for line in file:
            dates = line.strip().split(',')
            date_details = tuple(dates)
            details.append(date_details)
        self.country = Details.current_country(self, self.date_string, details)
        return self.country

    def todays_date(self):
        date = datetime.now()
        self.date_string = date.strftime('%Y/%m/%d')
        return self.date_string

    def conversion(self, target_currency):
        print(self.trip_origin, target_currency)
        self.home_currency = get_details(self.trip_origin)
        print(self.home_currency)
        self.target_currency = get_details(target_currency)
        print(self.target_currency)
        self.target_to_home = convert(1, self.target_currency[1], self.home_currency[1])
        print(self.target_to_home)
        self.home_to_target = convert(1, self.home_currency[1], self.target_currency[1])
        print(self.home_to_target)
        self.root.ids.status.text = ('Updated at {}'.format(time.strftime('%H:%M:%S')))

    def update_currency(self, target_currency):
        print(self.trip_origin)
        print(target_currency)
        if not target_currency:
            target_currency = self.current_location()
        self.home_currency = get_details(self.trip_origin)
        self.target_currency = get_details(target_currency)
        self.target_to_home = convert(1, self.target_currency[1], self.home_currency[1])
        print(self.target_to_home)
        self.home_to_target = convert(1, self.home_currency[1], self.target_currency[1])
        if not self.root.ids.country_selection.text:
            self.root.ids.country_selection.text = self.country
        self.root.ids.status.text = ('Updated at {}'.format(time.strftime('%H:%M:%S')))

    def convert_to_target(self, amount):
        converted_amount = float(amount.text) * self.home_to_target
        self.root.ids.target_to_home.text = str(round(converted_amount, 3))
        self.root.ids.status.text = (
            '{} ({}) to {} ({})'.format(self.home_currency[1], self.home_currency[2], self.target_currency[1],
                                        self.target_currency[2]))

    def convert_to_home(self, amount):
        converted_amount = float(amount.text) * self.target_to_home
        self.root.ids.home_to_target.text = str(round(converted_amount, 3))
        print(self.target_currency)
        self.root.ids.status.text = (
            '{} ({}) to {} ({})'.format(self.target_currency[1], self.target_currency[2], self.home_currency[1],
                                        self.home_currency[2]))


if __name__ == '__main__':
    app = CurrencyConverterApp()
    app.run()
