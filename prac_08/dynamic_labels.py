from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty()
    def build(self):
        """ initial the widget """
        self.title = "Dynamic Labels"
        self.root = Builder.load_string("dynamic_labels.kv")

