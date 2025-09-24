from flask import Flask 

#__name__= "__main__"
app = Flask(__name__)

@app.route("/")
def olha_mundo():
    return "eu não aguento mais Olá, Mundo!"

@app.route("/about") #=sobre
def about():
    return "Pagina sobre"

if __name__ == "__main__":
    app.run(debug=True) #e usado para desenvolvimento local (ou seja na minha maquina )