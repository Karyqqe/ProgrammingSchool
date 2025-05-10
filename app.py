from flask import Flask, render_template, request, jsonify
import io
import contextlib

app = Flask(__name__)

# Пример уроков (в реальности можно хранить в БД или файле)
lessons = [
    {
        "id": 1,
        "title": "Привет, мир!",
        "description": "Напишите программу, которая выводит 'Hello, world!'",
        "expected_output": "Hello, world!"
    },
    {
        "id": 2,
        "title": "Сложение чисел",
        "description": "Сложите два числа и выведите результат",
        "expected_output": "7"
    },
    {
        "id": 3,
        "title": "Цикл for",
        "description": "Выведите числа от 0 до 4 с помощью цикла for",
        "expected_output": "0\n1\n2\n3\n4"
    },
    {
        "id": 4,
        "title": "Функции",
        "description": "Создайте функцию, которая возвращает квадрат числа 3",
        "expected_output": "9"
    },
    {
        "id": 5,
        "title": "Условие if",
        "description": "Проверьте, больше ли 5 чем 3 и выведите 'True'",
        "expected_output": "True"
    }
]

@app.route('/')
def index():
    return render_template('index.html', lessons=lessons)

@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
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
    app.run(debug=True)
