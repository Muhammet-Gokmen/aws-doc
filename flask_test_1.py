from flask import Flask  # module

app = Flask(__name__)    # obje

@app.route('/')          # decoratyr
def hello():
    return "iste flask budur"

@app.route('/second')          # decoratyr
def second():
    return "iste flask budur.bu ikinci decoratyr"   

@app.route('/third/<string:id>')          # decoratyr. url de dinamik olarak bir degisken nasil calisir onu gosterir.
def third(id):
    return f'iste flask budur.dinamik {id}'  

if __name__ == '__main__':  # control mecanism
    app.run(debug=True, port=3000)    