from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to process form data
@app.route('/result', methods=['POST'])
def result():
    animal = request.form.get('animal')
    return render_template('result.html', animal=animal)

if __name__ == "__main__":
    app.run(debug=True)
