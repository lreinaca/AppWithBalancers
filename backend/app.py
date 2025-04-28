from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
 return """ <h1>Hola desde el Backend</h1><br>
    <h1>Aprendiendo a Usar Balanceadores de Carga</h1><br>
    <h2>Este es un ejemplo de una aplicación Flask que se ejecuta en un contenedor de Docker.</h2><br>
    <h3>Para ejecutar esta aplicación, primero debes construir la imagen de Docker y luego ejecutar el contenedor.</h3>"""
 


@app.route("/health")
def health():
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)