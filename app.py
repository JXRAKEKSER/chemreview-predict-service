from flask import Flask, request, jsonify
import pandas

app = Flask(__name__)

@app.route('/predict/smiles', methods=['POST'])
def predict():
    requestJson = request.get_json()
    print(requestJson['smiles'])
    return jsonify({ 'smiles': requestJson['smiles'] })
  
@app.route('/predict/file', methods=['POST'])
def predict_post():
    fileData = request.files.get('file')
    csvFile = pandas.read_csv(fileData.stream.read())
    print(csvFile)
    return 'hello'


if __name__ == '__main__':
    app.run(port=8002)