from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        # Main layout of the calculator
        self.layout = GridLayout(cols=4, padding=50, spacing=20, row_force_default=True, row_default_height=60)
        # Input/output display
        self.display = TextInput(
            multiline=False, halign="center", font_size=32, readonly=True, size_hint_y=0.3
        )
        self.layout.add_widget(self.display)

        # Buttons for the calculator
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', 'C', '+',
            '=', 'Back', 'Spike', 
        ]
        # Adding buttons to the layout
        for button in buttons:
            self.layout.add_widget(self.create_button(button))

        return self.layout

    def create_button(self, text):
        button = Button(
            text=text,
            font_size=24,
            background_color=(0.5, 0.5, 0.5, 1),
            color=(1, 1, 1, 1)
        )
        button.bind(on_press=self.on_button_press)
        return button

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.display.text = ""  # Clear the display
        elif text == "=":
            try:
                # Evaluate the expression in the display
                self.display.text = str(eval(self.display.text))
            except Exception:
                self.display.text = "Error"
        elif text == "Back":
            # Remove the last character
            self.display.text = self.display.text[:-1]
        elif text == "Spike":
            self.display.text = "Made By Spike"
        else:
            # Append button text to the display
            self.display.text += text

if __name__ == "__main__":
    CalculatorApp().run()
