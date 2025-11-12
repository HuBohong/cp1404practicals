from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    status_text = StringProperty()
    def __init__(self, **kwargs):
        """ construct main app"""
        super().__init__(**kwargs)
        self.label_names = ["Billy", "Alan", "Xinya", "Zonglin", "Edith", "Alice"]


    def build(self):
        """ initial the widget """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.creat_widget()

    def creat_widget(self):
        """ create widget dynamically """
        for label_name in self.label_names:
            temp_label = Label(text=label_name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
