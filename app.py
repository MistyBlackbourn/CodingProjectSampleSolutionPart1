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
        self.locations = []
        self.trip_origin = ""
        self.home_to_target = ""
        self.target_to_home = ""
        self.country = ""
        self.date_string = ""
        self.target_currency = ()
        self.home_currency = ()
        self.status = ""

        try:
            file = open('config.txt', mode='r')
            self.trip_origin = file.readline().strip()
            for line in file:
                details = line.strip().split(',')
                details = tuple(details)
                country_name = details[0]
                start_date = details[1]
                end_date = details[2]
                Details.add(self, country_name, start_date, end_date)
                self.location_list.append(country_name)
            file.close()
            self.status = "Trip Details Accepted"
        except Error:
            self.status = "Invalid Details"
        except FileNotFoundError:
            self.status = "No File Found"

    def build(self):
        Window.size = 300, 500
        Window.clearcolor = (1, .5, 0, 1)
        self.title = "Currency Converter"
        self.root = Builder.load_file('gui.kv')

    def current_location(self):
        self.country = Details.current_country(self, self.date_string)
        return self.country

    def todays_date(self):
        date = datetime.now()
        self.date_string = date.strftime('%Y/%m/%d')
        return self.date_string

    def currency_conversion(self, target_currency):
        self.home_currency = get_details(self.trip_origin)
        self.target_currency = get_details(target_currency)
        self.target_to_home = convert(1, self.target_currency[1], self.home_currency[1])
        self.home_to_target = convert(1, self.home_currency[1], self.target_currency[1])
        self.root.ids.status.text = ('Updated at {}'.format(time.strftime('%H:%M:%S')))
        self.root.ids.home_to_target.disabled = False
        self.root.ids.target_to_home.disabled = False

    def update_currency_conversion(self, target_currency):
        if not target_currency:
            target_currency = self.current_location()
        self.home_currency = get_details(self.trip_origin)
        self.target_currency = get_details(target_currency)
        self.target_to_home = convert(1, self.target_currency[1], self.home_currency[1])
        self.home_to_target = convert(1, self.home_currency[1], self.target_currency[1])
        if not self.root.ids.country_selection.text:
            self.root.ids.country_selection.text = self.country
        self.root.ids.status.text = ('Updated at {}'.format(time.strftime('%H:%M:%S')))
        self.root.ids.home_to_target.disabled = False
        self.root.ids.target_to_home.disabled = False

    def convert_to_target(self, amount):
        converted_amount = float(amount.text) * self.home_to_target
        self.root.ids.target_to_home.text = str(round(converted_amount, 3))
        self.root.ids.status.text = (
            '{} ({}) to {} ({})'.format(self.home_currency[1], self.home_currency[2], self.target_currency[1],
                                        self.target_currency[2]))

    def convert_to_home(self, amount):
        converted_amount = float(amount.text) * self.target_to_home
        self.root.ids.home_to_target.text = str(round(converted_amount, 3))
        self.root.ids.status.text = (
            '{} ({}) to {} ({})'.format(self.target_currency[1], self.target_currency[2], self.home_currency[1],
                                        self.home_currency[2]))

    def status_label(self):
        return self.status


if __name__ == '__main__':
    app = CurrencyConverterApp()
    app.run()
