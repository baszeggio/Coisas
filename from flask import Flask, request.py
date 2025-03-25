from flask import Flask, request

app = Flask(_name_)

lista_calculos = []

@app.route("/soma", methods=["POST"])
def somar ():
    dados_recebidos = request.get_json()
    numero1 = dados_recebidos["numero1"]
    numero2 = dados_recebidos["numero2"]
    resultado = numero1 + numero2
    lista_calculos.append({
        "Número1":numero1,
        "Número2":numero2,
        "Resultado":resultado
    })
    return {"Resultado": resultado}
   

@app.route("/calculos", methods=["GET"])
def retomar():
    return (lista_calculos)