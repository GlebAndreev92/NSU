#Импорт библиотек
import matplotlib.pyplot as plt
import numpy as np

# функция скользящей средней
def moving_avg(x, n):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[n:] - cumsum[:-n]) / float(n)

#формирование зашумлённого сигнала сигнала
tt = np.linspace(0, 1, 128, endpoint=True)
xx = 100*np.cos(2*np.pi*2*tt)+20*np.cos(2*np.pi*60*tt)
#визуализация формы сигнала
plt.plot(xx,'b')
plt.show()

xy=moving_avg(xx,3) # обработка сигнала скользящей средней с окном = 3

# вывод результатов
plt.plot(xx,'b')
plt.plot(xy,'r')
plt.show()

