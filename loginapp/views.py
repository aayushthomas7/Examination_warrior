from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Quiz, Questions, Score, User
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


def signupPage(request):
    return render(request, "signup.html")


def loginPage(request):
    return render(request, 'adminlogin.html')


def performLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = authenticate(request, username=username, password=password)
        # return HttpResponse('Everything okn(admin.ModelAdmin):
#     inline = [AnswersInline]')
        if user_obj is not None:
            login(request, user_obj)
            return HttpResponseRedirect(reverse('student-dashboard'))
            # return redirect(request, 'afterlogin')
            # return HttpResponse('logged in')
        else:
            return HttpResponse("mistake2")
    else:
        return HttpResponse("mistake1")
        # return HttpResponseRedirect(reverse('afterlogin'))
        # return render(request, "afterlogin.html")


def studentDashboard(request):
    courses = Quiz.objects.all()
    context = {"courses": courses}
    return render(request, "student_dashboard.html", context)


def logoutPage(request):
    logout(request)
    # return redirect(request,'login/')
    return HttpResponseRedirect(reverse('index'))


def quizPage(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = Questions.objects.filter(quiz=quiz)
    question_ct = questions.count()
    print("q ct is ", question_ct)
    context = {"quiz": quiz, "questions": questions, "n": range(
        question_ct), "total_questions": question_ct}
    return render(request, "quiz_page.html", context)


# questions = []
selected_anslst = []
correct_anslst = []
status_lst = []
score = 20
correct_ansct = 0
attempted = 0
# global selected_anslst
# global correct_anslst
# global status_lst
# global score


def save_quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)

    if request.is_ajax():
        global selected_anslst
        global correct_anslst
        global status_lst
        global score
        global correct_ansct
        global attempted
        questions = []
        selected_anslst = []
        correct_anslst = []
        status_lst = []
        score = 0
        correct_ansct = 0
        attempted = 0
        data = request.POST
        # data = request.GET['data']
        # data_ = dict((data).lists())

        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')
        # print("pk is ", pk)
        # quiz = Quiz.objects.get(name = )
        for (k, v) in data_.items():
            k = int(k[6:])
            # v = int(v[3:])

            if v[0] != '':
                val = int((v[0])[3:])
                selected_ans = val

            # print('key: ', k, " value: ", v)
            # question = Questions.objects.filter(quiz=quiz, question_no=k).correct_ans
            correct_ans = Questions.objects.get(
                quiz=quiz, question_no=k).getcorrectAns()
            if v[0] == '':
                selected_ans = "---"
                status = "N/A"
            elif selected_ans == correct_ans:
                score += 1
                correct_ansct += 1
                status = "CORRECT"
                attempted += 1
            else:
                status = "WRONG"
                attempted += 1
            correct_anslst.append(correct_ans)
            status_lst.append(status)
            selected_anslst.append(selected_ans)

            # print("Woah answers ", correct_ans)
            # questions.append(question)
        # print(questions)

        # user = request.user
        # quiz = Quiz.objects.get(pk=pk)

        # score = 0
        # multiplier = 100 / quiz.number_of_questions
        # results = []
        # correct_answer = None

        # for q in questions:
            # a_selected = request.POST.get(q.text)

            #     if a_selected != "":
            #         question_answers = Answer.objects.filter(question=q)
            #         for a in question_answers:
            #             if a_selected == a.text:
            #                 if a.correct:
            #                     score += 1
            #                     correct_answer = a.text
            #             else:
            #                 if a.correct:
            #                     correct_answer = a.text

            #         results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            #     else:
            #         results.append({str(q): 'not answered'})

            # score_ = score * multiplier
            # Result.objects.create(quiz=quiz, user=user, score=score_)
        # return JsonResponse({'passe': 23})
        print("Attempted ", attempted)
        print("Correct ans list ", correct_anslst)
        print("Status list", status_lst)
        print("Selected ans list ", selected_anslst)
        print("Score ", score)
        print("pk", pk)
        return JsonResponse({'correctAnsLst': correct_anslst, 'selectedAnsLst': selected_anslst,
                             'statusLst': status_lst, 'score': score, 'pk': pk})
        # if score_ >= quiz.required_score_to_pass:
        #     return JsonResponse({'passed': True, 'score': score_, 'results': results})
        # else:
        #     return JsonResponse({'passed': False, 'score': score_, 'results': results})


def resultPage(request, pk):
    # score_obj = Score()
    quiz = Quiz.objects.get(pk=pk)
    questions = Questions.objects.filter(quiz=quiz)
    question_ct = questions.count()
    # score_obj.user = User(request.user.id)
    # score_obj.quiz = Quiz(pk)
    # score_obj.score_val = score
    # print(request.user.username, " ", request.user.id)
    score_obj = Score(user=request.user, quiz=quiz, score_val=score)
    print("Score obj ", score_obj)
    score_obj.save()
    print("Score from results", score)
    context = {'quiz': quiz, 'correctAnsLst': correct_anslst, 'attempted': attempted,
               'selectedAnsLst': selected_anslst, 'statusLst': status_lst, 'score': score, 'correct_ansct': correct_ansct, 'question_ct': question_ct}
    return render(request, "result.html", context)


def scorePage(request):
    # scores_obj = Score.objects.filter(user=request.user)
    scores = Score.objects.filter(user=request.user).values()
    # scores_se = set(scores)
    print(scores)
    scores_lst = []
    quiz_lst = []
    for score in scores:
        print("Sc ", score)
        scores_lst.append(score['score_val'])
        print(" Quiz id ", score['quiz_id'])
        quiz = Quiz.objects.get(id=score['quiz_id']).name
        print("hey ,", quiz)
        # for (k, v) in dict(quiz).items():
        #     print("q k ", k)
        #     print("q v", v)
        quiz_lst.append(quiz)
    print("Score lst is ", scores_lst)
    print("Quiz ", quiz_lst)
    context = {"score_lst": scores_lst, "quiz_lst": quiz_lst}
    return render(request, 'student_marks.html', context)
