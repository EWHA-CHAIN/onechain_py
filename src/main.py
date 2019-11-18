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


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        note = Note(request.form['title'], request.form['content'])
        db.session.add(음표)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/mineBlock',methods=['POST'])
def mining():
    if request.method == 'POST':
        data = request.form['body'].data
        newBlock = bc.mineBlock(data)
        if(newBlock==null){
            return 'Bad Request'
        }
        else{
            return newBlock
        }

@app.route('/version',methods=['GET'])
def checkVersion:


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        note = Note(request.form['title'], request.form['content'])
        db.session.add(음표)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add.html')

def blockVersion(/blockVersion/:number):
    tempBlock = bc.getBlockchain()
    targetBlock
    for i in tempBlock:
        temp = tempBlock.header
        if temp.index == number:
            targetBlock = temp
    return temp.version 

    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='3001')