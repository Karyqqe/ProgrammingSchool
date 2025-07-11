from flask import Flask, render_template, request, jsonify
import io
import contextlib
import markdown

app = Flask(__name__)

# Пример уроков с расширенной теорией
lessons = [
    {
        "id": 1,
        "title": "Привет, мир!",
        "description": "Напишите программу, которая выводит 'Hello, world!'",
        "theory": """
### Введение в вывод текста

#### Что такое вывод текста?
В программировании вывод текста — это способ, которым программа общается с пользователем. В Python для этого используется функция `print()`. Она отправляет текст или числа в консоль (терминал), чтобы вы могли их увидеть.

#### Зачем это нужно?
Вывод текста полезен для:
- Проверки, работает ли программа правильно.
- Передачи информации пользователю.
- Отладки кода (например, чтобы увидеть промежуточные результаты).

#### Как работает `print()`?
Функция `print()` принимает один или несколько аргументов (то, что вы хотите вывести) и отображает их в консоли. Например:
```python
print('Hello, world!')
```
Этот код выведет строку `Hello, world!`. После вывода `print()` автоматически добавляет переход на новую строку.

#### Примеры
1. Вывод строки:
```python
print('Привет, Python!')
```
Результат: `Привет, Python!`

2. Вывод нескольких слов:
```python
print('Hello', 'world!')
```
Результат: `Hello world!` (слова разделяются пробелом).

3. Вывод числа:
```python
print(42)
```
Результат: `42`

#### Полезные советы
- Если вы хотите вывести текст без перехода на новую строку, используйте параметр `end`:
```python
print('Hello', end=' ')
print('world!')
```
Результат: `Hello world!`

- Строки можно заключать в одинарные (`'`) или двойные (`"`) кавычки — это одно и то же.

#### Связь с практикой
В этом уроке вы напишете простую программу, которая выведет `Hello, world!`. Это классическое первое задание в программировании, которое помогает понять, как работает вывод в Python.
        """,
        "expected_output": "Hello, world!"
    },
    {
        "id": 2,
        "title": "Сложение чисел",
        "description": "Сложите два числа, чтобы получилось 7, и выведите результат",
        "theory": """
### Основы арифметики в Python

#### Что такое арифметические операции?
Арифметические операции — это математические действия, такие как сложение, вычитание, умножение и деление. В Python они выполняются с помощью специальных символов, называемых операторами.

#### Оператор сложения
Оператор `+` используется для сложения двух чисел. Например:
```python
result = 5 + 2
```
Здесь `result` будет равно `7`.

#### Как вывести результат?
Чтобы показать результат сложения, используйте функцию `print()`. Например:
```python
print(5 + 2)
```
Результат: `7`

#### Какие типы чисел есть в Python?
Python поддерживает два основных типа чисел:
- **Целые числа** (`int`): Например, `1`, `42`, `-10`.
- **Числа с плавающей точкой** (`float`): Например, `3.14`, `0.5`.

Сложение работает с обоими типами. Например:
```python
print(3.5 + 2.5)
```
Результат: `6.0`

#### Примеры
1. Сложение целых чисел:
```python
print(4 + 3)
```
Результат: `7`

2. Сложение с переменными:
```python
a = 5
b = 2
print(a + b)
```
Результат: `7`

3. Сложение чисел с плавающей точкой:
```python
print(1.5 + 5.5)
```
Результат: `7.0`

#### Полезные советы
- Убедитесь, что вы складываете числа, а не строки. Например:
```python
print("5" + "2")  # Это не сложение, а конкатенация строк!
```
Результат: `52`

- Если нужно сложить числа, введенные пользователем, преобразуйте строки в числа с помощью `int()` или `float()`.

#### Связь с практикой
Ваша задача — написать код, который складывает два числа так, чтобы результат был `7`, и вывести этот результат с помощью `print()`. Например, вы можете использовать `5 + 2`.
        """,
        "expected_output": "7"
    },
    {
        "id": 3,
        "title": "Цикл for",
        "description": "Выведите числа от 0 до 4 с помощью цикла for",
        "theory": """
### Циклы for в Python

#### Что такое цикл for?
Цикл `for` — это конструкция в Python, которая позволяет повторять действия для каждого элемента в последовательности. Например, вы можете перебрать числа, список или строку.

#### Как работает цикл for?
Цикл `for` использует функцию `range()` для создания последовательности чисел. Например:
```python
for i in range(5):
    print(i)
```
Этот код выведет:
```
0
1
2
3
4
```

Здесь `range(5)` создает последовательность чисел от `0` до `4` (5 чисел, но последнее не включается).

#### Синтаксис
```python
for переменная in последовательность:
    # Код, который выполняется для каждого элемента
```
- `переменная` — это имя, которое принимает каждое значение из последовательности.
- `последовательность` — это, например, `range(5)` или список `['a', 'b', 'c']`.

#### Примеры
1. Вывод чисел от 1 до 3:
```python
for i in range(1, 4):
    print(i)
```
Результат:
```
1
2
3
```

2. Вывод четных чисел с шагом 2:
```python
for i in range(0, 6, 2):
    print(i)
```
Результат:
```
0
2
4
```

3. Перебор списка:
```python
fruits = ['яблоко', 'банан', 'груша']
for fruit in fruits:
    print(fruit)
```
Результат:
```
яблоко
банан
груша
```

#### Полезные советы
- `range(start, stop, step)`:
  - `start` — начальное число (по умолчанию `0`).
  - `stop` — конечное число (не включается).
  - `step` — шаг (по умолчанию `1`).
- Циклы можно вкладывать друг в друга для более сложных задач.
- Используйте понятные имена переменных, например, `i` для индексов или `item` для элементов списка.

#### Связь с практикой
Ваша задача — использовать цикл `for` с `range(5)`, чтобы вывести числа от `0` до `4`, каждое на новой строке. Это поможет вам понять, как работает перебор последовательностей.
        """,
        "expected_output": "0\n1\n2\n3\n4"
    },
    {
        "id": 4,
        "title": "Функции",
        "description": "Создайте функцию, которая возвращает квадрат числа 3",
        "theory": """
### Функции в Python

#### Что такое функция?
Функция — это блок кода, который выполняет определенную задачу и может быть использован повторно. Функции помогают сделать код организованным и избежать дублирования.

#### Как определить функцию?
Функции в Python создаются с помощью ключевого слова `def`. Например:
```python
def square(n):
    return n * n
```
- `def` — начало определения функции.
- `square` — имя функции.
- `n` — параметр (входное значение).
- `return` — возвращает результат.

#### Как вызвать функцию?
Чтобы использовать функцию, просто укажите ее имя и передайте аргументы:
```python
result = square(3)
print(result)
```
Результат: `9`

#### Зачем нужны функции?
- **Повторное использование**: Напишите код один раз и используйте его многократно.
- **Читаемость**: Функции делают код понятнее, разбивая его на логические блоки.
- **Модульность**: Легче тестировать и изменять отдельные части программы.

#### Примеры
1. Функция для удвоения числа:
```python
def double(n):
    return n * 2

print(double(5))
```
Результат: `10`

2. Функция с несколькими параметрами:
```python
def add(a, b):
    return a + b

print(add(3, 4))
```
Результат: `7`

3. Функция без параметров:
```python
def say_hello():
    return 'Hello!'

print(say_hello())
```
Результат: `Hello!`

#### Полезные советы
- Давайте функциям понятные имена, описывающие их назначение (например, `square`, а не `f`).
- Используйте `return` для возврата результата. Без `return` функция вернет `None`.
- Проверяйте типы входных данных, чтобы избежать ошибок (например, `square('2')` вызовет ошибку).

#### Связь с практикой
Ваша задача — создать функцию, которая принимает число `3` и возвращает его квадрат (`9`). Используйте `def`, `return` и `print()`, чтобы вывести результат.
        """,
        "expected_output": "9"
    },
    {
        "id": 5,
        "title": "Условие if",
        "description": "Проверьте, больше ли 5 чем 3 и выведите 'True'",
        "theory": """
### Условные операторы в Python

#### Что такое условный оператор?
Условный оператор `if` позволяет программе принимать решения, выполняя код только при определенных условиях. Например, вы можете проверить, больше ли одно число другого.

#### Как работает `if`?
Синтаксис условного оператора:
```python
if условие:
    # Код, который выполняется, если условие истинно
```
- `условие` — выражение, которое возвращает `True` или `False`.
- После `:` идет блок кода, который выполняется, если условие истинно.

#### Операторы сравнения
Python поддерживает следующие операторы сравнения:
- `>` — больше
- `<` — меньше
- `>=` — больше или равно
- `<=` — меньше или равно
- `==` — равно
- `!=` — не равно

Пример:
```python
if 5 > 3:
    print('True')
```
Результат: `True`

#### Дополнительные конструкции
- `else`: Выполняется, если условие `if` ложно.
```python
if 2 > 5:
    print('Истина')
else:
    print('Ложь')
```
Результат: `Ложь`

- `elif`: Проверяет дополнительные условия.
```python
x = 10
if x > 15:
    print('Больше 15')
elif x > 5:
    print('Больше 5')
else:
    print('5 или меньше')
```
Результат: `Больше 5`

#### Примеры
1. Проверка равенства:
```python
if 3 == 3:
    print('Равно')
```
Результат: `Равно`

2. Проверка с `else`:
```python
age = 16
if age >= 18:
    print('Взрослый')
else:
    print('Ребенок')
```
Результат: `Ребенок`

3. Использование `and` и `or`:
```python
if 5 > 3 and 2 < 4:
    print('Оба условия истинны')
```
Результат: `Оба условия истинны`

#### Полезные советы
- Условия должны возвращать `True` или `False`. Например, `if 5` — неверно, нужно `if 5 > 0`.
- Используйте отступы (обычно 4 пробела) для блока кода внутри `if`, `else`, `elif`.
- Избегайте сложных условий — разбейте их на части для читаемости.

#### Связь с практикой
Ваша задача — использовать `if`, чтобы проверить, больше ли `5` чем `3`, и вывести `True`. Это базовый пример использования условных операторов.
        """,
        "expected_output": "True"
    }
]

@app.route('/')
def index():
    return render_template('index.html', lessons=lessons)

@app.route('/lesson/<int:lesson_id>/theory')
def lesson_theory(lesson_id):
    lesson = next((l for l in lessons if l['id'] == lesson_id), None)
    if not lesson:
        return "Урок не найден", 404
    # Преобразуем Markdown в HTML
    lesson_theory_html = markdown.markdown(lesson['theory'], extensions=['fenced_code'])
    return render_template('theory.html', lesson=lesson, lesson_theory_html=lesson_theory_html)

@app.route('/lesson/<int:lesson_id>/practice')
def lesson_practice(lesson_id):
    lesson = next((l for l in lessons if l['id'] == lesson_id), None)
    if not lesson:
        return "Урок не найден", 404
    return render_template('lesson.html', lesson=lesson)

@app.route('/check', methods=['POST'])
def check():
    code = request.form['code']
    expected = request.form['expected']

    # Захват вывода
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            exec(code, {})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

    result = output.getvalue().strip()
    if result == expected:
        return jsonify({"success": True, "output": result})
    else:
        return jsonify({"success": False, "output": result, "expected": expected})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)