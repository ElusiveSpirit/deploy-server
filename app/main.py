from subprocess import check_output

from app import app
from flask import request, render_template, json, jsonify
from config import SCRIPT

from app.utils import get_token_list


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            data = json.loads(request.data)
        except:
            return jsonify({"error": "Post data is not in json"})
        if "token" not in data:
            return jsonify({"error": "No token data in request"})
        token = data["token"]

        if token not in get_token_list():
            return jsonify({"error": "Token is invalid"})

        return check_output(SCRIPT.split(" "))
    else:
        return render_template('index.html')
