from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class CurrencyConverterApp(App):
    # def __init__(self):
    #     pass

    def build(self):
        Window.size = 300, 500
        Window.clearcolor = (1, .5, 0, 1)
        self.title = "Currency Converter"
        self.root = Builder.load_file('gui.kv')
        return self.root




CurrencyConverterApp().run()
