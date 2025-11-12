import re
import math
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 320)
Config.set('graphics', 'height', 500)


class CalculatorApp(App):
    def safe_eval(self, expression):
        """ Secure calculation of a mathematical expression
            Безопасное вычисление математического выражения """
        if not re.match(r'^[0-9+\-*/(). ]+$', expression):
            return "Ошибка"
        try:
            return eval(expression)
        except ZeroDivisionError:
            return 'Делить на 0 нельзя'
        except SyntaxError:
            return 'Ошибка ввода'

    def update_label(self):
        """Refreshes the window with numbers / Обновляет окно с цифрами"""
        self.lbl.text = self.formula

    def add_number(self, instance):
        """Entering numbers on the scoreboard / Ввод чисел на табло"""
        if self.formula == '0':
            self.formula = ''

        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        # Check for duplicate operators / Проверка на дублирование операторов
        last_char = self.formula[-1]
        if last_char in "+-*/":
            return
        # Prohibition of two dots in one number / Запрет на две точки в одном числе
        if instance.text == "." and "." in self.formula.split(" ")[-1]:
            return

        """ Adding operations to the scoreboard / Добавление операций на табло
            Special conditions for mul and div symbols / Спец условия для символов умн и дел"""

        if (str(instance.text)).lower() == '×':
            self.formula += '*'
        elif (str(instance.text)).lower() == '÷':
            self.formula += '/'
        else:
            self.formula += (instance.text)
        self.update_label()

    def calc_result(self, instance):
        """Output of the result / Вывод результата
        The eval() function is used / Используется функция eval()"""

        result = str(self.safe_eval(self.lbl.text))
        self.lbl.text = str(result)
        self.formula = str(result) if False != all(result != i for i in ("Ошибка", "Делить на 0 нельзя", "Ошибка ввода")) else "0"

    def calc_ce(self, instance):
        """Full reset on the screen / Полный сброс на экране."""
        self.formula = '0'
        self.update_label()

    def calc_back(self, instance):
        """Character-by-character deletion / Посимвольное удаление"""
        self.formula = str(self.formula)[:-1]
        if self.formula == '':
            self.formula = '0'
        self.update_label()

    def calc_square(self, instance):
        """Extracting the square root / Извлечение квадратного корня"""
        try:
            number = float(self.lbl.text)
            if number < 0:
                self.lbl.text = 'Ошибка ввода'
                self.formula = '0'
            else:
                self.lbl.text = str(math.sqrt(number))

        except ValueError:
            self.lbl.text = 'Ошибка'
            self.formula = '0'

    def calc_exit(self, instance):
        """Exit and stop the program / выход из программы"""
        self.stop()

    def build(self):
        """Building calculator buttons / Построение кнопок калькулятора"""
        self.formula = '0'
        b1 = BoxLayout(orientation='vertical', padding=5)
        g1 = GridLayout(cols=4, spacing=1, size_hint=(1, .6))

        self.lbl = Label(text="0", font_size=42, halign='right', valign='center',
                         size_hint=(1, .4), text_size=(330 - 50, 500 * .4 - 50))
        b1.add_widget(self.lbl)

        g1.add_widget(Button(text="√", font_size=22, on_press=self.calc_square))
        g1.add_widget(Button(text="CE", font_size=22, on_press=self.calc_ce))
        g1.add_widget(Button(text="<-", font_size=22, on_press=self.calc_back))
        g1.add_widget(Button(text="÷", font_size=22, on_press=self.add_operation))

        g1.add_widget(Button(text="7", font_size=22, on_press=self.add_number))
        g1.add_widget(Button(text="8", font_size=22, on_press=self.add_number))
        g1.add_widget(Button(text="9", font_size=22, on_press=self.add_number))
        g1.add_widget(Button(text="×", font_size=22, on_press=self.add_operation))

        g1.add_widget(Button(text="4", font_size=22, on_press=self.add_number))
        g1.add_widget(Button(text="5", font_size=22, on_press=self.add_number))
        g1.add_widget(Button(text="6", font_size=22, on_press=self.add_number))
        g1.add_widget(Button(text="-", font_size=22, on_press=self.add_operation))

        g1.add_widget(Button(text="1", font_size=22, on_press=self.add_number))
        g1.add_widget(Button(text="2", font_size=22, on_press=self.add_number))
        g1.add_widget(Button(text="3", font_size=22, on_press=self.add_number))
        g1.add_widget(Button(text="+", font_size=22, on_press=self.add_operation))

        g1.add_widget(Button(text='off', font_size=22, on_press=self.calc_exit, background_color=(1, 0.6, 0.2, 1)))
        g1.add_widget(Button(text="0", font_size=22, on_press=self.add_number))
        g1.add_widget(Button(text=".", font_size=22, on_press=self.add_operation))
        g1.add_widget(Button(text="=", font_size=22, on_press=self.calc_result, background_color=(0, 0.7, 1, 1)))

        b1.add_widget(g1)
        return b1

if __name__ == "__main__":
    CalculatorApp().run()
