from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.PositiveIntegerField(blank=False)
    height = models.FloatField(blank=False)
    sex = models.IntegerField(blank=False)
    predictions = models.CharField(max_length=30, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def to_dict_json(self):
        return {
            'name': self.name,
            'age': self.age,
            'height': self.height,
            'sex': self.sex,
            'predictions': self.predictions
        }
