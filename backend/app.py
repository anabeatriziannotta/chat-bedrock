from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3
import json
from botocore.exceptions import ClientError

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Configurações do cliente AWS Bedrock
client = boto3.client("bedrock-runtime", region_name="us-east-1")
model_id = "anthropic.claude-3-haiku-20240307-v1:0"

@app.route('/api/invoke', methods=['POST'])
def invoke_model():
    data = request.get_json()
    prompt = data.get('prompt')

    native_request = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "temperature": 0.5,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}],
            }
        ],
    }
    
    request_body = json.dumps(native_request)

    try:
        response = client.invoke_model(modelId=model_id, body=request_body)
        model_response = json.loads(response["body"].read().decode("utf-8"))
        response_text = model_response["content"][0]["text"]
        return jsonify({"response": response_text})

    except (ClientError, Exception) as e:
        return jsonify({"response": f"ERROR: Can't invoke '{model_id}'. Reason: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
