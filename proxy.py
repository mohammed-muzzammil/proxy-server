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
    # Assuming the body is in JSON format or form data; adjust decoding as necessary
    data = request.get_json() or request.form or {}
    print(data)
    
    return jsonify({"message": "Request details printed in the server console."})

if __name__ == '__main__':
    app.run(debug=True)
