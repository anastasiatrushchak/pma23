import pandas as pn
import matplotlib.pyplot as plt


data = pn.read_csv("austin_airport_departure_data_2015_july.csv")
print(data)
# pn.set_option('display.max_rows', 1000)

data["Date (MM/DD/YYYY)"] = pn.to_datetime(data["Date (MM/DD/YYYY)"], format='%m/%d/%Y')


#А)
print("<---------------------Виліти по дням--------------------->")
print(data["Date (MM/DD/YYYY)"].dt.day.value_counts())
print("<---------------------Виліти по місяцям--------------------->")
print(data["Date (MM/DD/YYYY)"].dt.month.value_counts())

#B)
b = data["Tail Number"].value_counts()
print(b)

#C)
c1 = data.groupby(data["Date (MM/DD/YYYY)"].dt.month)['Departure Delay(Minutes)'].mean()
print("<---------------------Середня затримака в місяць--------------------->")
print(c1)
c2 = data.groupby(data["Date (MM/DD/YYYY)"].dt.day)['Departure Delay(Minutes)'].mean()
print("<---------------------Середня затримака в день--------------------->")
print(c2)

#D)
d1 = data["Actual Elapsed Time(Minutes)"].max()
print("<---------------------Максимальний час--------------------->")
print(d1)
d2 = data["Actual Elapsed Time(Minutes)"].min()
print("<---------------------Мінімальний час--------------------->")
print(d2)

#E)
e1 = data["Departure Delay(Minutes)"].max()
print("<---------------------Максимальний час--------------------->")
print(e1)
e2 = data["Departure Delay(Minutes)"].min()
print("<---------------------Мінімальний час--------------------->")
print(e2)

#F)
data = data.sort_values(by="Departure Delay(Minutes)")
plt.plot(data["Departure Delay(Minutes)"], data["Actual Elapsed Time(Minutes)"]) # ні немає якби була задежність то вимальовувалась рівна лінія
plt.show()