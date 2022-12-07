from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    name = models.CharField(max_length=200)
    time_limit = models.IntegerField()

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.questions_set.all()

    class Meta:
        verbose_name_plural = "Quizes"


class Questions(models.Model):
    question_no = models.IntegerField()
    image = models.ImageField(upload_to="", null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    correct_ans = models.IntegerField(null=True)

    def getcorrectAns(self):
        return self.correct_ans

    def __str__(self):
        return self.quiz.name + " Question " + str(self.question_no) + ": "

    class Meta:
        ordering = ('quiz', 'question_no',)
        verbose_name_plural = "Questions"


class Score(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score_val = models.IntegerField(null=True)

    def __str__(self):
        return self.quiz.name
    # def getquizes(self):
    #     retu
