from flask import Flask, jsonify, request

app = Flask(__name__)

headers = {'Content-Type': 'application/json'}

@app.route('/example-get-static', methods=['GET'])
def getEndpointStatic():
    staticResponse = {
        "num-example" : 25,
        "string-example" : "example string",
        "list example" : [1,3,5],
        "dict-example" : {
            "thing1" : 1,
            "thing2" : 2
        }
    }
    # returns the json version if the dictionary
    return jsonify(staticResponse), 200


@app.route('/example-get-dynamic', methods=['GET'])
def getEndpointDynamic():
    # will need the ?name=string param here (although string is not enforced)
    name = request.args.get("name")

    if not name:
        return jsonify({'message': 'Name not provided in request as param'}), 400

    dynamicResponse = {
        "user name" : name
    }

    return jsonify(dynamicResponse), 200


@app.route('/example-post', methods=['POST'])
def postEndpoint():
    """ The format to make a request is 
    {
        "age" : some num,
        "name" : string
    }
    """

    data = request.get_json()
    if not data:
        return jsonify({'message': 'JSON not provided in request as param'}), 400
        
    try:
        name = data["name"]
        age = data["age"]

    except:
        return jsonify({'message': 'JSON is incorrect'}), 400

    response_string = name + " is " + str(age) + " years old."

    response = {
        "string" : response_string
    }

    return jsonify(response), 200



if __name__ == '__main__':
    # run app in debug mode on port 5000
	app.run(debug=True, port=5000) 