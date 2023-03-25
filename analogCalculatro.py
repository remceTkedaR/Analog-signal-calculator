# Kalkulatro saklowania wartosci analogowych procesowe ( 0-27648)
#
# przykładowo sygnał procesowy 0-27648 skalujemy do zakresu 0-100%
# wartość zmiennej max 100%
# wartość min zmiennej 0%
# max wartość procesowa 27648
# min wartość procesowa 0
# y = (y1-y0)/(x1-x0) * (x - x0) + y0
# --------------------------------------

import math

value_out = 0.0
y_out = 0.0
x_value = 0.0
x1_value = 27648  # max wartość procesowa sygnału
x0_value = 0  # min wartość procesowa sygnału
y1_value = 100.0
y0_value = 0.0


# y1_value = 0.0  # max wartość zmiennej
#  y0_value = 0.0  # min wartość zmiennej


def calculation_analog(x1_value, x0_value, y1_value, y0_value):
    x_value = input("podaj wartośc procesową z zakresu 27648 - 0 : ")
    y_out = (y1_value - y0_value) / (x1_value - x0_value) * (int(x_value) - x0_value) + y0_value
    return y_out


value_out = calculation_analog(27648, 0, 100, 0)

print(value_out)
