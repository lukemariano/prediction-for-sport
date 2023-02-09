import joblib
from django.db import models
from sklearn.tree import DecisionTreeClassifier


class Data(models.Model):
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
