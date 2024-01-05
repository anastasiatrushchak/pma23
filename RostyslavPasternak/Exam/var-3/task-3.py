import pandas as pn
import matplotlib.pyplot as plt

data = pn.read_csv("tips (1).csv")
print(data)

#a)
print("<-------Хто дає більші чайові: курці чи ні------>")
a = data.groupby("smoker")["total_bill"].mean()
print(a)

#b)
b = data.groupby("day")["total_bill"].mean()
print("<---------b) Чайові по днях тижня)--------->")
print(b)
b.plot(kind="bar", title="b) Чайові по днях тижня")
plt.show()

#c)
c = data.groupby("time")["total_bill"].mean()
print("<---------с) чайові взалежності від часу (обід, вечеря)--------->")
print(c)

#d)
data['total_bill'].hist(bins=100, figsize=(8, 6))
plt.xlabel('Сума рахунку')
plt.ylabel('Кількість')
plt.title('Гістограма рахунків')
plt.show()

#e)
plt.scatter(data['total_bill'], data['tip'])
plt.xlabel('Сума рахунку')
plt.ylabel('Чай')
plt.title('Скаттер рахунок-чайові')
plt.show()

#f)
f = data.groupby("sex")["total_bill"].mean()
f.plot(kind="bar")
plt.show()
