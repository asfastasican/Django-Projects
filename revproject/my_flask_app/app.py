from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    greeting = None
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            greeting = f"Hello, {name} Thank you for Visiting!"
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    print("Inside the finc")
    app.run(debug=True, port=8000)