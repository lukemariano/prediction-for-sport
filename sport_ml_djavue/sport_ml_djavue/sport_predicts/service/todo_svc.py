from ..models import Data


def add_todo(new_predict):
    predict = Data(
        name=new_predict['name'],
        age=new_predict['age'],
        height=float(new_predict['height']),
        sex=new_predict['sex'],
        predictions="['hockey']"
        )
    predict.save()
    return predict.to_dict_json()


def list_todos():
    predicts = Data.objects.all()
    return [predict.to_dict_json() for predict in predicts]
