import matplotlib.pyplot as plt
import pandas as pn

data = pn.read_csv("titanic_train.csv")
print(data)

a = data["Survived"].value_counts()
print(a)

b1 = data.groupby("Pclass")["Survived"].value_counts().unstack()
print(b1)
b2 = b1.div(b1.sum(axis=1), axis=0) * 100
print("Відносні величини виживання по класах:")
print(b2)


bins = [0, 30, 60, 100]
labels = ['Молоді (до 30 років)', 'Середні (30-60 років)', 'Старші (понад 60 років)']
data['AgeGroup'] = pn.cut(data['Age'], bins=bins, labels=labels, right=False)

age_survival_counts = data.groupby('AgeGroup')['Survived'].value_counts().unstack()
age_survival_percentages = age_survival_counts.div(age_survival_counts.sum(axis=1), axis=0) * 100


d = data["Embarked"].value_counts()
print(d)


e = data.groupby("Pclass")["Fare"].mean()
data = data.sort_values(by="Parch")
e.plot(kind="bar")
plt.show()


# plt.figure(figsize=(10, 6))
# plt.boxplot([data[data['Pclass'] == 1]['Fare'],
#              data[data['Pclass'] == 2]['Fare'],
#              data[data['Pclass'] == 3]['Fare']],
#             labels=['Pclass 1', 'Pclass 2', 'Pclass 3'])
# plt.title('Залежність плати за квиток від класу каюти')
# plt.xlabel('Клас каюти')
# plt.ylabel('Плата за квиток')
# plt.show()