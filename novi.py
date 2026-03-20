import pandas as pd
print('version',pd.__version__)


# 1 head(n) - показывает первые n строк таблицы
# 2 tail(n) - показывает последние n строк таблицы
# 3 info() - информация о таблице: типы данных, количество строк, пустые значения
# 4 describe() - статистика по числам: среднее, минимум, максимум, стандартное отклонение
# 5 value_counts() - считаем повторения
# 6 groupby() - группирует данные по столбцу для расчётов по группам
# 7 sort_values() - сортирует таблицу по значениям в указанном столбце
# 8 dropna() - удаляет строки, где есть пустые значения
# 9 merge() - объединяет две таблицы по общему столбцу
# 10 apply() - применяет свою функцию к каждому элементу столбца
# 11 shape - показывает размер таблицы в формате (строки, столбцы)


d1 = {
    'Имя': ['Аня', 'Борис', 'Вика', 'Глеб', 'Дима'],
    'Оценка': [5, 4, 5, 3, 4],
    'Класс': ['9А', '9Б', '9А', '9Б', '9А']
}

d2 = {
    'Класс': ['9А', '9Б'],
    'Учитель': ['Иванова', 'Петров']
}

df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)

print("=== head(2) ===")
print(df1.head(2))

print("=== tail(2) ===")
print(df1.tail(2))

print("=== info() ===")
df1.info()

print("=== describe() ===")
print(df1.describe())

print("=== value_counts() ===")
print(df1['Оценка'].value_counts())

print("=== groupby('Класс').mean() ===")
print(df1.groupby('Класс')['Оценка'].mean())

print("=== sort_values(by='Оценка') ===")
print(df1.sort_values(by='Оценка'))

print("=== dropna() ===")
print(df1.dropna())

print("=== merge() ===")
print(pd.merge(df1, df2, on='Класс'))

print("=== apply(lambda x: x + 1) ===")
print(df1['Оценка'].apply(lambda x: x + 1))

print("=== shape ===")
print(df1.shape)