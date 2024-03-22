from operator_db import create_table, fetch_random_sentence
import os

from flask import Flask
app = Flask(__name__)

@app.route('/api')
def hello():
    return fetch_random_sentence()

if __name__ == '__main__':
    if not os.path.exists('hitokoto.db'):
        create_table()
    # app.run(debug=True)

    from waitress import serve
    serve(app, host="127.0.0.1", port=8080)
    
    

