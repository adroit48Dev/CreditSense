from flask import Flask
from Savoir import Savoir
import json

api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)
api.getinfo()

app = Flask(__name__)

multichain = connect()

def connect():
    with open('credentials.json') as json_data:
        credentials = json.loads(json_data)
        json_data.close()
    rpcuser = credentials.rpcuser
    rpcpasswd = credentials.rpcpasswd
    rpchost = credentials.rpchost
    rpcport = credentials.rpcport
    chainname = credentials.chainname
    return Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/add_loan_applicant_data',methods=['POST'])
def add_loan_applicat_data():
    if request.method == 'POST':
        data = request.form
        return 'Success'

@app.route('/get_all_applicant_data',methods=['GET'])
def get_all_applicant_data():
    if request.method == 'GET':
        data =
    return 'choddiya tarun69 ko'

if __name__ == "__main__":

    app.run(debug=True)
