from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index(): # ngầm định là có đối tượng request rồi, lưu toàn cục
    return render_template('index.html',msg='Welcome to app')


if __name__ == '__main__':
    app.run(debug=True)


