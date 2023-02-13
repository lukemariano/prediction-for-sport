import joblib
from django.db import models
from sklearn.tree import DecisionTreeClassifier

from ..accounts.models import User


class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser", on_delete=models.CASCADE)
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Data(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    age = models.PositiveIntegerField(blank=False)
    height = models.DecimalField(max_digits=3, decimal_places=2, blank=False)
    sex = models.IntegerField(blank=False)
    predictions = models.CharField(max_length=30, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load("model/ml_sport_model.joblib")
        self.predictions = ml_model.predict([[self.age, self.height, self.sex]])
        return super().save(*args,  **kwargs)

    class Meta:
        ordering = ['-date']

    def to_dict_json_add(self):
        return {
            'name': self.name,
            'age': self.age,
            'height': self.height,
            'sex': self.sex,
            'predictions': self.predictions.tolist()
        }
    
    def to_dict_json_list(self):
        return {
            'name': self.name,
            'age': self.age,
            'height': self.height,
            'sex': self.sex,
            'predictions': self.predictions
        }
