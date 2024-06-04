from flask import Flask, request, render_template
from warnings import filterwarnings
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/') #importando o template
def index():
    return render_template('index.html')

@app.route('/resposta_index',methods=['GET']) #importando o template
def predict():
    return render_template('resposta_index.html')



if __name__ == '__main__':
    app.run()