from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from datetime import datetime
from trip import *
from currency import *
from kivy.properties import StringProperty


class CurrencyConverterApp(App):
    def __init__(self, **kwargs):
        super(CurrencyConverterApp, self).__init__(**kwargs)
        self.location_list = []

    def build(self):
        Window.size = 300, 500
        Window.clearcolor = (1, .5, 0, 1)
        self.title = "Currency Converter"
        self.root = Builder.load_file('gui.kv')
        return self.root

    def trip_details(self):
        file = open('config.txt', mode='r')
        file.readline()
        for line in file:
            details = line.strip().split(',')
            details = tuple(details)
            self.location_list.append(details[0])
        file.close()
        return self.location_list

    def trip_origin(self):
        file = open('config.txt', mode='r')
        trip_origin = file.readline()
        file.close()
        return trip_origin

    def current_location(self):
        date_string = CurrencyConverterApp.todays_date(self)
        print(date_string)
        file = open('config.txt', mode='r')
        details = []
        file.readline()
        for line in file:
            dates = line.strip().split(',')
            date_details = tuple(dates)
            details.append(date_details)
            print(details)
        country = Details.current_country(self, date_string, details)
        return country

    def todays_date(self):
        date = datetime.now()
        return date.strftime('%Y/%m/%d')

    def conversion(self, home_currency, target_currency):
        print(type(home_currency))
        home_currency = get_details('Australia')
        print(home_currency)
        target_currency = get_details(target_currency)
        print(target_currency)
        target_to_home = convert(1, target_currency[1], home_currency[1])
        print(target_to_home)
        home_to_target = convert(1, home_currency[1], target_currency[1])
        print(home_to_target)

    def update_currency(self, home_currency, target_currency):
        print(home_currency)
        print(target_currency)
        if not target_currency:
            target_currency = CurrencyConverterApp.current_location(self)
        home_currency = get_details('Australia')
        target_currency = get_details(target_currency)
        target_to_home = convert(1, target_currency[1], home_currency[1])
        print(target_to_home)
        home_to_target = convert(1, home_currency[1], target_currency[1])
        print(home_to_target)

    def convert(self, amount):
        pass
    #     conversion_amount = home_to_target * amount
    #     print(conversion_amount)


if __name__ == '__main__':
    app = CurrencyConverterApp()
    app.run()
