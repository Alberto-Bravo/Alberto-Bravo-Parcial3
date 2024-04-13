from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id":1, "nombre":"zer", "enable":True},
    {"id":2, "nombre":"tank", "enable":True},
    {"id":3, "nombre":"op", "enable":True},
    {"id":4, "nombre":"deal", "enable":True}
]

@app.route('/tasks', methods={'GET'})
def get_tasks():
        return jsonify(tasks)

if __name__ == '__main__':
        app.run(debug=True)