from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class RandomNumberGenerator(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        generate_button = Button(text="Generate")
        result_label = Label(text="", font_size=48)

        def generate_random_number(instance):
            random_number = str(random.randint(100, 999))  # Rastgele 3 basamaklı sayı oluşturur
            result_label.text = random_number

        generate_button.bind(on_press=generate_random_number)

        layout.add_widget(generate_button)
        layout.add_widget(result_label)

        return layout

if __name__ == '__main__':
    RandomNumberGenerator().run()
