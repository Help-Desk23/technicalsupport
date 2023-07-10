from flask import Flask, jsonify, request, send_file
from database import get_connection

app = Flask(__name__)


@app.route('/branch', methods=['GET'])
def obtain_branch():
    cnn = get_connection()
    cur = cnn.cursor()
    cur.execute("SELECT * FROM branch")
    registros = cur.fetchall()
    list_branch = []
    for registro in registros:
        people = {
            "id": registro[0],
            "name_branch": registro[1],
            "direction": registro[2],
            "province": registro[3]
        }
        list_branch.append(people)

    return jsonify({"people": list_branch})

if __name__ == '__main__':
    app.run(debug=True, port=8000)