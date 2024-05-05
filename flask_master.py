from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('giro.html')

@app.route('/contacts/')
def contacts():
    developer_name = 'Pavel Durov'
    return render_template('contacts.html', name = developer_name)

if __name__ == "__main__":
    app.run(debug = True)