import model_pb2
from typing import Iterable

class ValidationError(Exception):
    pass

def features_to_dict(features: Iterable[model_pb2.Feature]) -> dict[str, float]:
    data = {}
    for f in features:
        if f.name in data:
            raise ValidationError(f'Дубликат признака: {f.name}')
        if not f.name:
            raise ValidationError('Пустое наименование признака')
        data[f.name] = float(f.value)
    if not data:
        raise ValidationError('Признаки не предоставлены')
    return data