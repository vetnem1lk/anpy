import pandas as pd
import numpy as np
import pycountry
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
# Используем класс YandexTranslate из модуля yandex_translate
from yandex_translate import YandexTranslate
# Используем класс YandexTranslateException из модуля yandex_translate
from yandex_translate import YandexTranslateException

YANDEX_API_KEY = 'Здесь должен быть определен API ключ !!!!!'
try:
    translate_obj = YandexTranslate(YANDEX_API_KEY)
except YandexTranslateException:
    translate_obj = None

# Размер надписей на графиках
PLOT_LABEL_FONT_SIZE = 14
# Генерация цветовой схемы
# Возвращает список цветов


def getColors(n):
    COLORS = []
    cm = plt.cm.get_cmap('hsv', n)
    for i in np.arange(n):
        COLORS.append(cm(i))
    return COLORS


def dict_sort(my_dict):
    keys = []
    values = []
    my_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    for k, v in my_dict:
        keys.append(k)
        values.append(v)
    return (keys, values)


df = pd.read_csv('./scrubbed.csv', escapechar='`', low_memory=False)


# Получить из таблицы список всех меток country с их количеством
country_label_count = pd.value_counts(df['country'].values)
for label in list(country_label_count.keys()):
    # Перевести код страны в полное название
    c = pycountry.countries.get(alpha_2=str(label).upper())
    # Перевести название страны на русский язык

shapes_label_count = pd.value_counts(df['shape'].values)
# Перевести название формы объекта на русский язык

country_count = pd.value_counts(df['country'].values, sort=True)
country_count_keys, country_count_values = dict_sort(dict(country_count))
TOP_COUNTRY = len(country_count_keys)
plt.title('Страны, где больше всего наблюдений', fontsize=PLOT_LABEL_FONT_SIZE)
plt.bar(np.arange(TOP_COUNTRY), country_count_values,
        color=getColors(TOP_COUNTRY))
plt.xticks(np.arange(TOP_COUNTRY), country_count_keys, rotation=0, fontsize=12)
plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
plt.ylabel('Количество наблюдений', fontsize=PLOT_LABEL_FONT_SIZE)
plt.show()

MONTH_COUNT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MONTH_LABEL = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
               'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

for i in df['datetime']:
    m, d, y_t = i.split('/')
    MONTH_COUNT[int(m)-1] = MONTH_COUNT[int(m)-1] + 1

plt.bar(np.arange(12), MONTH_COUNT, color=getColors(12))
plt.xticks(np.arange(12), MONTH_LABEL, rotation=90,
           fontsize=PLOT_LABEL_FONT_SIZE)
plt.ylabel('Частота появления', fontsize=PLOT_LABEL_FONT_SIZE)
plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
plt.title('Частота появления объектов по месяцам',
          fontsize=PLOT_LABEL_FONT_SIZE)
plt.show()


shapes_type_count = pd.value_counts(df['shape'].values)
shapes_type_count_keys, shapes_type_count_values = dict_sort(
    dict(shapes_type_count))
OBJECT_COUNT = len(shapes_type_count_keys)
plt.title('Типы объектов', fontsize=PLOT_LABEL_FONT_SIZE)
bar = plt.bar(np.arange(OBJECT_COUNT), shapes_type_count_values,
              color=getColors(OBJECT_COUNT))
plt.xticks(np.arange(OBJECT_COUNT), shapes_type_count_keys,
           rotation=90, fontsize=PLOT_LABEL_FONT_SIZE)
plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
plt.ylabel('Сколько раз видели', fontsize=PLOT_LABEL_FONT_SIZE)
