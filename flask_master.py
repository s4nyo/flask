from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    main_data = {
        'Город': 'Чебоксары',
        'Район': 'Московский',
        'Компания': 'Iserv'
    }

    context = {
        'Имя': 'Саня',
        'Возраст': '16',
        'Профессия': 'безработный'
    }
    return render_template('giro.html', main_data = main_data, **context)

@app.route('/contacts/')
def contacts():
    developer_name = 'Pavel Durov'
    return render_template('contacts.html', name = developer_name)

@app.route('/results/')
def results():
    data = ['python', 'js', 'GO', 'C#', 'C++', 'lua', 'React', 'SQL', 'Postgesql']
    return render_template('results.html', data = data)

if __name__ == "__main__":
    app.run(debug = True)