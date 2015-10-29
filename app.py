from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from datetime import datetime


class CurrencyConverterApp(App):
    # def __init__(self):
    #     pass

    def build(self):
        Window.size = 300, 500
        Window.clearcolor = (1, .5, 0, 1)
        self.title = "Currency Converter"
        self.root = Builder.load_file('gui.kv')
        return self.root

    def trip_details(self):
        location_list = []
        file = open('config.txt', mode='r')
        file.readline()
        for line in file:
            details = line.strip().split(',')
            details = tuple(details)
            location_list.append(details[0])
        file.close()
        return location_list

    def trip_origin(self):
        file = open('config.txt', mode='r')
        trip_origin = file.readline()
        file.close()
        return trip_origin

    def current_location(self):
        date = todays_date()
        file = open('config.txt', mode = 'r')
        for line in file:
            pass

    def todays_date(self):
        date = datetime.now()
        return date.strftime('%Y/%m/%d')

CurrencyConverterApp().run()
