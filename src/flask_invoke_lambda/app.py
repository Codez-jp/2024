import os
import json

import boto3
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def check():
    return "<p>root is OK!</p>"


@app.route('/lambda')
def call_lambda():
    lambda_client = boto3.client('lambda')

    response = lambda_client.invoke(
        FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
        InvocationType='RequestResponse',
        Payload=json.dumps({
            "pk": "user#1",
            "sk": "company-1#section-1#group-1",
            "data": {
                "firstName": "Test1",
                "lastName": "Person"
            }
        })
    )

    _byte = response['Payload'].read()
    _str = _byte.decode('utf-8')
    _json = json.loads(_str)

    return _json["body"]
