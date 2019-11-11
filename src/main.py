from flask import flask

import network as nw
import wallet as wl
import utils as ut
import blockchain as bc 


app = Flask(__name__)


@app.route('/')
def start():
    return None


def initHttpServer(/blocks):
    return bc.getBlockchain()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='3001')