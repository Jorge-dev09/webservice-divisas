from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Tipos de cambio fijos (puedes ajustarlos)
EURO_MXN = 18.5
USD_MXN = 17.2
CAD_MXN = 12.7
GBP_MXN = 21.5

@app.route('/')
def home():
    return "Servicio de conversión de divisas activo"

# EURO → MXN
@app.route('/euro-a-mxn')
def euro_mxn():
    cantidad = float(request.args.get('cantidad', 0))
    resultado = cantidad * EURO_MXN
    return jsonify({"conversion": resultado})

# USD → MXN
@app.route('/usd-a-mxn')
def usd_mxn():
    cantidad = float(request.args.get('cantidad', 0))
    resultado = cantidad * USD_MXN
    return jsonify({"conversion": resultado})

# CAD → MXN
@app.route('/cad-a-mxn')
def cad_mxn():
    cantidad = float(request.args.get('cantidad', 0))
    resultado = cantidad * CAD_MXN
    return jsonify({"conversion": resultado})

# GBP → MXN
@app.route('/gbp-a-mxn')
def gbp_mxn():
    cantidad = float(request.args.get('cantidad', 0))
    resultado = cantidad * GBP_MXN
    return jsonify({"conversion": resultado})

# MXN → EURO
@app.route('/mxn-a-euro')
def mxn_euro():
    cantidad = float(request.args.get('cantidad', 0))
    resultado = cantidad / EURO_MXN
    return jsonify({"conversion": resultado})

# MXN → USD
@app.route('/mxn-a-usd')
def mxn_usd():
    cantidad = float(request.args.get('cantidad', 0))
    resultado = cantidad / USD_MXN
    return jsonify({"conversion": resultado})

# MXN → CAD
@app.route('/mxn-a-cad')
def mxn_cad():
    cantidad = float(request.args.get('cantidad', 0))
    resultado = cantidad / CAD_MXN
    return jsonify({"conversion": resultado})

# MXN → GBP
@app.route('/mxn-a-gbp')
def mxn_gbp():
    cantidad = float(request.args.get('cantidad', 0))
    resultado = cantidad / GBP_MXN
    return jsonify({"conversion": resultado})

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

