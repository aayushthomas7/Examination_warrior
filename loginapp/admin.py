from django.contrib import admin
from .models import Quiz, Questions, Score

# admin.site.register(Quiz)


# class AnswersInline(admin.TabularInline):
#     model = Answers


# class QuestionAdmin(admin.ModelAdmin):
#     inline = [AnswersInline]

class QuestionInline(admin.TabularInline):
    model = Questions
    ordering = ("question_no",)


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Quiz, QuizAdmin)
# class AnswersAdmin(admin.ModelAdmin):
#     list_display = ['question', 'user', 'submitted_ans']


admin.site.register(Questions)
# admin.site.register(Answers, AnswersAdmin)


class ScoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'quiz']
    ordering = ['user']


admin.site.register(Score, ScoreAdmin)
