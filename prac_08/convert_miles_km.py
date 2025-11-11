from kivy.app import App
from kivy.lang import Builder

CONVERT_TO_KM = 1.60934

class MilesConverterApp(App):
    def build(self):
        self.title = 'Miles Convert to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles_km(self):
        miles = self.get_valid_miles()
        km = miles * CONVERT_TO_KM
        self.root.ids.output_id.text = str(km)

    def get_valid_miles(self):
        """ return miles if valid return 0.0 if invalid"""
        try:
            miles = float(self.root.ids.input_miles.text)
            return miles
        except ValueError:
            return 0.0

MilesConverterApp().run()