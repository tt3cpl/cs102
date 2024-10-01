import tkinter as tk
from math import sqrt

from tkinter import ttk


class Calculator:
    '''Реализация как графической, так и логической части калькулятора'''
    def __init__(self, main):
        self.main = main
        self.main.title("Калькулятор")
        self.main.geometry("470x150")

        self.number_entry = ttk.Entry(self.main, width=20)
        self.number_entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        self.button_1 = ttk.Button(self.main, text="1", command=lambda: self.button_click(1))
        self.button_2 = ttk.Button(self.main, text="2", command=lambda: self.button_click(2))
        self.button_3 = ttk.Button(self.main, text="3", command=lambda: self.button_click(3))
        self.button_4 = ttk.Button(self.main, text="4", command=lambda: self.button_click(4))
        self.button_5 = ttk.Button(self.main, text="5", command=lambda: self.button_click(5))
        self.button_6 = ttk.Button(self.main, text="6", command=lambda: self.button_click(6))
        self.button_7 = ttk.Button(self.main, text="7", command=lambda: self.button_click(7))
        self.button_8 = ttk.Button(self.main, text="8", command=lambda: self.button_click(8))
        self.button_9 = ttk.Button(self.main, text="9", command=lambda: self.button_click(9))
        self.button_0 = ttk.Button(self.main, text="0", command=lambda: self.button_click(0))
        self.clear_button = ttk.Button(self.main, text="C", command=self.button_clear)
        self.add_button = ttk.Button(self.main, text="+", command=self.button_add)
        self.equal_button = ttk.Button(self.main, text="=", command=self.button_equal)
        self.subtract_button = ttk.Button(self.main, text="-", command=self.button_subtraction)
        self.multiply_button = ttk.Button(self.main, text="*", command=self.button_multiply)
        self.divide_button = ttk.Button(self.main, text="/", command=self.button_divide)
        self.floor_div_button = ttk.Button(self.main, text="//", command=self.button_floor_div)
        self.modulus_button = ttk.Button(self.main, text="%", command=self.button_modulus)
        self.sqrt_button = ttk.Button(self.main, text="√", command=self.button_sqrt)
        self.neg_button = ttk.Button(self.main, text="+/-", command=self.button_neg)

        self.button_1.grid(row=1, column=0)
        self.button_2.grid(row=1, column=1)
        self.button_3.grid(row=1, column=2)
        self.add_button.grid(row=1, column=3)
        self.floor_div_button.grid(row=1, column=4)

        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)
        self.subtract_button.grid(row=2, column=3)
        self.modulus_button.grid(row=2, column=4)

        self.button_7.grid(row=3, column=0)
        self.button_8.grid(row=3, column=1)
        self.button_9.grid(row=3, column=2)
        self.multiply_button.grid(row=3, column=3)
        self.sqrt_button.grid(row=3, column=4)

        self.clear_button.grid(row=4, column=0)
        self.button_0.grid(row=4, column=1)
        self.equal_button.grid(row=4, column=2)
        self.divide_button.grid(row=4, column=3)
        self.neg_button.grid(row=4, column=4)

        self.f_num = 0
        self.math = ""

    def button_click(self, number):
        '''Обработчик нажатий на кнопки-цифры'''
        current = self.number_entry.get()
        self.number_entry.delete(0, tk.END)
        self.number_entry.insert(0, str(current) + str(number))

    def button_clear(self):
        '''Чистка поля'''
        self.number_entry.delete(0, tk.END)

    def button_add(self):
        '''Обработка команды сложение'''
        first_number = self.number_entry.get()
        self.math = "addition"
        self.f_num = int(first_number)
        self.number_entry.delete(0, tk.END)

    def button_equal(self):
        '''Обработка команды равенсво'''
        second_number = self.number_entry.get()
        self.number_entry.delete(0, tk.END)

        if self.math == "addition":
            self.number_entry.insert(0, self.f_num + int(second_number))

        if self.math == "subtraction":
            self.number_entry.insert(0, self.f_num - int(second_number))

        if self.math == "multiplication":
            self.number_entry.insert(0, self.f_num * int(second_number))

        if self.math == "division":
            self.number_entry.insert(0, self.f_num / int(second_number))

        if self.math == "floor_div":
            self.number_entry.insert(0, self.f_num // int(second_number))

        if self.math == "modulus":
            self.number_entry.insert(0, self.f_num % int(second_number))

    def button_subtraction(self):
        '''Обработка команды разность'''
        first_number = self.number_entry.get()
        self.math = "subtraction"
        self.f_num = int(first_number)
        self.number_entry.delete(0, tk.END)

    def button_multiply(self):
        '''Обработка команды умножение'''
        first_number = self.number_entry.get()
        self.math = "multiplication"
        self.f_num = int(first_number)
        self.number_entry.delete(0, tk.END)

    def button_divide(self):
        '''Обработка команды деление (с остатком)'''
        first_number = self.number_entry.get()
        self.math = "division"
        self.f_num = int(first_number)
        self.number_entry.delete(0, tk.END)

    def button_floor_div(self):
        '''Обработка команды деление (целочисленное)'''
        first_number = self.number_entry.get()
        self.math = "floor_div"
        self.f_num = int(first_number)
        self.number_entry.delete(0, tk.END)

    def button_modulus(self):
        '''Обработка команды остаток от деления'''
        first_number = self.number_entry.get()
        self.math = "modulus"
        self.f_num = int(first_number)
        self.number_entry.delete(0, tk.END)

    def button_sqrt(self):
        '''Обработка команды извлечение квадратного корня'''
        number = float(self.number_entry.get())
        result = sqrt(number)
        if result.is_integer():
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, int(result))
        else:
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, result)

    def button_neg(self):
        '''Обработка команды присваивание полярности числу'''
        current = self.number_entry.get()
        if current.startswith("-"):
            current = current[1:]
        else:
            current = "-" + current
        self.number_entry.delete(0, tk.END)
        self.number_entry.insert(0, current)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
