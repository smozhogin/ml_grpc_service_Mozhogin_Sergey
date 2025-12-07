import grpc
import model_pb2, model_pb2_grpc

def make_stub(addr: str = 'localhost:50052'):
    channel = grpc.insecure_channel(addr)
    return model_pb2_grpc.PredictionServiceStub(channel)

def health(stub):
    res = stub.Health(model_pb2.HealthRequest(), timeout=2.0)
    print(f'Состояние: {res.status}, Версия: {res.model_version}')

def predict(stub):
    req = model_pb2.PredictRequest(features=[
        model_pb2.Feature(name='sepal_length', value=5.1),
        model_pb2.Feature(name='sepal_width', value=3.5),
        model_pb2.Feature(name='petal_length', value=1.4),
        model_pb2.Feature(name='petal_width', value=0.2),
    ])
    res = stub.Predict(req, timeout=3.0)
    print(f'Инференс: {res.prediction}, Уверенность: {round(res.confidence, 4)}, Версия: {res.model_version}')

if __name__ == '__main__':
    stub = make_stub()
    health(stub)
    predict(stub)