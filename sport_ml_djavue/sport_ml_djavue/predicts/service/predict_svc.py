from ..models import Data


def add_predict(new_predict):
    predict = Data(
        name=new_predict['name'],
        age=new_predict['age'],
        height=float(new_predict['height']),
        sex=new_predict['sex']
        )
    predict.save()
    return predict.to_dict_json_add()


def list_predicts():
    predicts = Data.objects.all()
    return [predict.to_dict_json_list() for predict in predicts]
