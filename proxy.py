from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'DELETE'])
def catch_all(path):
    print(f'Received {request.method} request for path: /{path}')
    print('Headers:')
    for header, value in request.headers:
        print(f'  {header}: {value}')
    
    # No need to process JSON payload here, as we're not expecting one with GET or DELETE
    # However, you can still access query parameters or other relevant request data if needed
    
    return jsonify({"message": "Request received and processed."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',  port=443)
