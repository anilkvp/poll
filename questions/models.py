from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=255)


class Poll(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    yes_count = models.IntegerField(default=0)
    no_count = models.IntegerField(default=0)

    def update_count(self, sel_value):
        if sel_value == 'Y':
            self.yes_count += 1
        else:
            self.no_count += 1

