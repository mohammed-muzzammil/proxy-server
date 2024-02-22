from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    print(f'Received {request.method} request for path: /{path}')
    print('Headers:')
    for header, value in request.headers:
        print(f'  {header}: {value}')
    
    print('Body:')
    data = request.get_json() or request.form or {}
    print(data)
    
    return jsonify({"message": "Request details printed in the server console."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
