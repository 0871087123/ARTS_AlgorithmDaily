import numpy as np
import matplotlib.pyplot as plt
from math import sin
from math import cos

# function to integration
def funx(x):
    return cos(x)

def original_integration(x):       # symbolic caculation
    return sin(x)

def mento_integration(x):
    sample_num = 200
    step = x / sample_num
    sum = 0.0
    for idx in range(0, sample_num):
        dp = step * (idx + 1)
        value = funx(dp)
        sum += value * x
    sum = sum / sample_num
    return sum

x=np.arange(0, 10.0, 0.1)
y=[]
basey=[]
for i in x:
    basey.append(original_integration(i))
    y.append(mento_integration(i))


plt.plot(x, y, color='blue')
plt.plot(x, basey, color='red')

plt.legend()

plt.show()
