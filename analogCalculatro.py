# Kalkulatro saklowania wartosci analogowych procesowe ( 0-27648)
# Process analog value scaling calculator
# przykładowo sygnał procesowy 0-27648 skalujemy do zakresu 0-100%
# for example, the process signal 0-27648 is scaled to the range of 0-100%
# wartość zmiennej max 100%
# variable value max 100%
# wartość min zmiennej 0%
# minimum value of the variable 0%
# max wartość procesowa 27648
# max process value 27648
# min wartość procesowa 0
# min process value 0
# --------------------------------------
# y = (y1-y0)/(x1-x0) * (x - x0) + y0
# --------------------------------------


""""
#value_out = 0.0
#y_out = 0.0
#x_value = 0.0
x1_value = 27648  # max wartość procesowa sygnału / signal process value
x0_value = 0  # min wartość procesowa sygnału / signal process value
y1_value = 100.0
y0_value = 0.0
"""

# y1_value = 0.0  # max wartość zmiennej / variable value
#  y0_value = 0.0  # min wartość zmiennej / variable value


def calculation_analog(x1_value, x0_value, y1_value, y0_value):

    # enter a percentage value in the range 27648 - 0
    x_value = input("podaj wartość procesową z zakresu 27648 - 0 : ")
    x1_value = 27648
    x0_value = 0
    y_out: float = (y1_value - y0_value) / (x1_value - x0_value) * (int(x_value) - x0_value) + y0_value
    return y_out


value_out: float = calculation_analog(27648, 0, 100, 0)

print(value_out)
