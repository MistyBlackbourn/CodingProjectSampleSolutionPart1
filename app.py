from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from datetime import datetime
from trip import *
from currency import *


class CurrencyConverterApp(App):
    def __init__(self, **kwargs):
        super(CurrencyConverterApp, self).__init__(**kwargs)
        self.location_list = []
        self.trip_origin = ""
        self.home_to_target = ""
        self.target_to_home = ""
        self.country = ""

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
        date_string = CurrencyConverterApp.todays_date(self)
        file = open('config.txt', mode='r')
        details = []
        file.readline()
        for line in file:
            dates = line.strip().split(',')
            date_details = tuple(dates)
            details.append(date_details)
        self.country = Details.current_country(self, date_string, details)
        return self.country

    def todays_date(self):
        date = datetime.now()
        return date.strftime('%Y/%m/%d')

    def conversion(self, target_currency):
        print(self.trip_origin, target_currency)
        home_currency = get_details(self.trip_origin)
        print(home_currency)
        target_currency = get_details(target_currency)
        print(target_currency)
        self.target_to_home = convert(1, target_currency[1], home_currency[1])
        print(self.target_to_home)
        self.home_to_target = convert(1, home_currency[1], target_currency[1])
        print(self.home_to_target)

    def update_currency(self, target_currency):
        print(self.trip_origin)
        print(target_currency)
        if not target_currency:
            target_currency = CurrencyConverterApp.current_location(self)
        home_currency = get_details('Australia')
        target_currency = get_details(target_currency)
        self.target_to_home = convert(1, target_currency[1], home_currency[1])
        print(self.target_to_home)
        self.home_to_target = convert(1, home_currency[1], target_currency[1])
        if not self.root.ids.country_selection.text:
            self.root.ids.country_selection.text = self.country
        print(self.home_to_target)

    def convert_to_target(self):
        converted_amount = float(self.root.ids.target_to_home.text) * float(self.home_to_target)
        self.root.ids.home_to_target = converted_amount

    def convert_to_home(self):
        converted_amount = float(self.root.ids.home_to_target.text) * float(self.target_to_home)
        self.root.ids.target_to_home = converted_amount


if __name__ == '__main__':
    app = CurrencyConverterApp()
    app.run()
