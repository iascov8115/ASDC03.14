# Индивидуальная работа №3 - Динамические структуры данных

## Структура проекта

    .
    ├── data
    │   └── students_data.csv
    ├── main.py
    ├── src
    │   └── classes
    │       ├── binary_tree.py
    │       ├── faculty.py
    │       ├── singly_linked_list.py
    │       └── student.py
    └── tests
        ├── test_binary_tree.py
        └── test_singly_linked_list.py

* Директория data содержит csv файл с данными
* Директория tests содержит файлы с тестами:
    * Тестирование бинарного дерево поиска
    * Тестирование односвязного списка
* Директория classes содержит классы структур данных:
    * Бинарное дерево поиска
    * Односвязный список
    * Студент
    * Факультет

<hr>

## Установка и запуск

Для запуска проекта необходим интерпретатор Python

```
git clone git@github.com:iascov8115/ASDC03.git
cd ASDC03
python main.py
```

<hr>

## Запуск тестов

```
python -m unittest -v tests/test_*
```

<hr>

## Требования к работе

Создайте новый проект и клонируйте в него проект, полученный в результате выполнения лабораторной работы №3.

Создайте папку tests. Для каждого класса из проекта создайте файл с тестами.

Отредактируйте README.md файл, добавив пункт тестирования, поясняющий, как запускать тесты.