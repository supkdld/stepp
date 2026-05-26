import matplotlib.pyplot as plt
import seaborn as sns

# Предположим, у нас есть статистика по запросам
data = [10, 15, 7, 18, 22]
labels = [ '3anpoc 1 ' , '3anpoc 2 ' , '3anpoc 3' , '3anpoc 4', '3anpc 5 ']

plt.figure(figsize=(10, 5))
sns.barplot(x=labels, y=data)
plt.title('Статистика запросов к приложению')
plt.xlabel('3anpoсы')
plt.ylabel('Количество ')
plt.savefig('requests_stats.png')
plt.show()