import pytest
from django.contrib.auth.models import User

from sport_ml_djavue.predicts.models import Data


@pytest.mark.django_db
def test_cria_um_usuario():
    user = User.objects.create_user(
        username='testuser',
        password='testpassword'
    )
    assert user.id is not None


@pytest.mark.django_db
def test_data_save():
    data = Data(name='John', age=20, height=1.80, sex=1)
    data.save()

    assert data.predictions == ['Soccer'], (
        print(f"The output is {data.predictions}")
        )


def test_api_list(client, db):
    user = User.objects.create_user(
        username='testuser',
        password='testpassword'
    )

    client.login(username='testuser', password='testpassword')

    resp = client.get('/api/predicts/list')
    assert resp.status_code == 200


