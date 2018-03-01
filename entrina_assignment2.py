from flask import Flask, jsonify, request

app = Flask(__name__)

BTS = [{'name' : 'Kim Namjoon'},{'name' : 'Kim Seokjin'}, {'name' : 'Min Yoongi'}, {'name' : 'Jung Hoseok'}, {'name' : 'Park Jimin'}, {'name' : 'Kim Taehyung'}, {'name' : 'Jeon Jeongguk'}]


@app.route ('/bts', methods=['GET'])
def returnAll():
    return jsonify({'BTS' : BTS})

@app.route ('/bts/<string:name>', methods=['GET'])
def returnReq(name):
    members = [member for member in BTS if member['name'] == name]
    return jsonify({'member': members[0]})

@app.route ('/bts', methods=['POST'])
def addReq():
    member = {'name' : request.json['name']}
    BTS.append(member)
    return jsonify({'BTS': BTS})


@app.route ('/bts/<string:name>', methods=['PUT'])
def editReq(name):
    members = [member for member in BTS if member['name'] == name]
    members[0]['name'] = request.json['name']
    return jsonify({'member': members[0]})

@app.route('/bts/<string:name>', methods=['DELETE'])
def removeReq(name):
    members = [member for member in BTS if member['name'] == name]
    BTS.remove(members[0])
    return jsonify({'BTS' : BTS})

if __name__ == '__main__':
    app.run(debug=True)