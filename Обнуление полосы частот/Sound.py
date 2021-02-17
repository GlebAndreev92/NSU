#Импорт библиотек
import matplotlib.pyplot as plt
from scipy.fft import fft,ifft
import numpy as np

# функция скользящей средней
def moving_avg(x, n):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[n:] - cumsum[:-n]) / float(n)

#формирование зашумлённого сигнала сигнала
tt = np.linspace(0, 1, 128, endpoint=True)
xx = 100*np.cos(2*np.pi*2*tt)+10*np.cos(2*np.pi*60*tt)
#визуализация формы сигнала
plt.plot(xx,'b')
plt.title('Исходный сигнал')
plt.show()

#преобразование Фурье
c=fft(xx,1024)
cc1=np.abs(c)
b=c

b[400:700]=0 #обнуление высокочастотной состовляющей части спектра сигнала
cc=np.abs(b)
c=fft(xx,1024)
m=c
m[0:400]=0
m[624:1024]=0
cc2=np.abs(m)
d=ifft(b) # обратное преобразование Фурье
h=ifft(m)

plt.plot(cc,'b')
plt.title('Обнуление ВЧ части спектра')
plt.xlim([0, 1024 / 2])
plt.show()

plt.plot(cc1,'r')
plt.title('Исходный спектр')
plt.xlim([0, 1024 / 2])
plt.show()

plt.plot(cc2,'b')
plt.title('Обнуление НЧ части спектра')
plt.xlim([0, 1024/2])
plt.show()

plt.plot(d,'r')
plt.title('Обратный сигнал без ВЧ части')
plt.xlim([0, 127])
plt.show()

plt.plot(h,'r')
plt.title('Обратный сигнал без НЧ части')
plt.xlim([0, 127])
plt.show()
