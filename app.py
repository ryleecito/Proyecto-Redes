from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Hola desde Flask, Docker en Azure '

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)