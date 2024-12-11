import numpy as np 
import matplotlib.pyplot as plt 
import numexpr as ne 
from pyautogui import alert, prompt
import re

def func_builder(formula):

	# присваивание области определения функции
	x = np.linspace(-40, 40, 10000)

	# перевод строчного вида формулы в арифметический (в случае неудачи - завершение работы программы)
	try:
		y = ne.evaluate(formula)
	except:
		alert(title='Ошибка', text='Ошибка: Неверно введённое значение')
		quit()

	# настройка параметров графика
	title_f = 'График функции y={r}'.format(r=formula)
	plt.title(title_f)
	plt.plot(x, y, color='blue')
	plt.axhline(0, color='black')
	plt.axvline(0, color='black')
	plt.grid()
	plt.ylabel('Ось Y')
	plt.xlabel('Ось X')

	# определение расположение координат (1 и 3 аргументы) и единичных отрезков (2 и 4 аргументы)
	plt.axis([-15, 15, -8, 10]) 
	
	# подсветка положительных и отрициательных значений функции зелёным и красным цветами соответсвтенно (ПРИ ЖЕЛАНИИ РАСКОММЕНТИРОВАТЬ)
	# plt.fill_between(x, 999, where=y>0, facecolor='green', alpha=.5)
	# plt.fill_between(x, -999, where=y<0, facecolor='red', alpha=.5)

	# создание окна графика
	plt.show()

while True:
	# запуск окна с вводом функции
	input_var = prompt(title='Построитель графиков', text='Введите функцию: ')

	# проверка на наличие "нулевого ввода"
	if input_var is None or ''.join(input_var) == '':
		quit()
	else:
		func_builder(input_var)