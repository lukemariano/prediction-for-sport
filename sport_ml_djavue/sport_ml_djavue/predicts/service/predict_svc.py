from ..models import Data


def add_predict(new_predict, request):
    predict = Data(
        user=request.user,
        name=new_predict['name'],
        age=new_predict['age'],
        height=float(new_predict['height']),
        sex=new_predict['sex']
        )
    predict.save()
    return predict.to_dict_json_add()


def list_predicts(request):
    predicts = Data.objects.filter(user=request.user)
    return [predict.to_dict_json_list() for predict in predicts]

def delete_predict(new_predict, request):
    predict = Data.objects.get(
        user=request.user,
        name=new_predict['name'],
        age=new_predict['age'],
        height=new_predict['height'],
        sex=new_predict['sex']
        )
    predict.delete()
    return {"status": "deletado"}


