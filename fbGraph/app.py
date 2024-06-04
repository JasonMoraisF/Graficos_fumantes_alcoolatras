from flask import Flask, request, render_template
from warnings import filterwarnings
import pickle
from flask import Flask, render_template, request


def import_model():  # abre o modelo treinado
    modelo = pickle.load(open('./fbGraph/modelo.sav', 'rb'))
    return modelo


modelo = import_model()

app = Flask(__name__)


@app.route('/') #importando o template
def index():
    return render_template('index.html')

@app.route('/resposta_index',methods=['GET']) #importando o template
def respostaPag():
    return render_template('resposta_index.html')

@app.route('/predict',methods=['POST']) #mandando seus dados
def predict():
     
    parametros = [float(request.form['genero']),
        float(request.form['Idade']), 
    float(request.form['Peso']), 
    float(request.form['Cintura']), 
    float(request.form['Colesterol_Total']), 
    float(request.form['PAS']), 
    float(request.form['PAD']),
    float(request.form['BLDS']), 
    float(request.form['HDL_colesterol']), 
    float(request.form['Triglicerídio']), 
    float(request.form['Hemoglobina']), 
    float(request.form['Proteina_da_urina']),
    float(request.form['soro_creatinina']), 
    float(request.form['SGOT_AST']), 
    float(request.form['SGOT_ALT']), 
    float(request.form['gamma_GTP']), 
    float(request.form['Voce fuma'])]
    
    resultado = modelo.predict([ parametros ])[0]
    
    if resultado == 0: 
        resultado = 'Você não é alcóolatra'
    else:
        resultado = 'Você é alcóolatra'


    return render_template('resposta_index.html', resultado=resultado)


if __name__ == '__main__':
    app.run()