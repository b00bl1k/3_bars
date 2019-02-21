# Ближайшие бары

Скрипт, позволяющий найти:
- Самый большой бар;
- Самый маленький бар;
- Самый близкий бар (необходимо ввести gps-координаты).

Перед запуском необходимо скачать список баров https://devman.org/fshare/1503831681/4/

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py bars.json # possibly requires call of python3 executive instead of just python
Please input your location (lat, lon): 55.770507, 37.613110
Closest bar: ПИВНОЙ БАР ЭЛЕФАНТ Address: 2-й Колобовский переулок, дом 12
Biggest bar: Спорт бар «Красная машина» Seats count: 450
Smallest bar: БАР. СОКИ Seats count: 0
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
