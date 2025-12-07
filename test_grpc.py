import json
import subprocess

cmd_health = [
    "grpcurl",
    "-plaintext",
    "localhost:50052",
    "mlservice.v1.PredictionService.Health",
]

subprocess.run(cmd_health, check=True)

request = {
    "features": [
        {"name": "sepal_length", "value": 5.1},
        {"name": "sepal_width",  "value": 3.5},
        {"name": "petal_length", "value": 1.4},
        {"name": "petal_width",  "value": 0.2}
    ]
}

data = json.dumps(request)

cmd_predict = [
    "grpcurl",
    "-plaintext",
    "-d", data,
    "localhost:50052",
    "mlservice.v1.PredictionService.Predict",
]

subprocess.run(cmd_predict, check=True)