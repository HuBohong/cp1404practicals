from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self,button):
        name = self.root.ids.name_input.text
        self.root.ids.output_label.text = f"Hello, {name}!"

BoxLayoutDemo().run()
