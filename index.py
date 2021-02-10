from flask import Flask, render_template

app = Flask(__name__)

"""
@app.route('/')
def principal():
    return "Bienvenidos!"

@app.route('/contacto')
def contacto():
    return "Contáctanos!"
"""

@app.route('/')
def principal():
    return render_template('index.html')

@app.route ('/lenguajes')
def mostrarLenguajes():
    misLenguajes = ("PHP","Python","Java","JavaScript","Perl","Ruby","Rust")
    return render_template('lenguajes.html', lenguajes=misLenguajes)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__  == '__main__':
    app.run(debug=True, port=5017) #debug=True hace que se reinicie el servidor automaticamente cuando hay un cambio
