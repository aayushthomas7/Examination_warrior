from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginPage, name="login"),
    path('performlogin/', views.performLogin, name="performlogin"),
    path('student-dashboard/', views.studentDashboard, name="student-dashboard"),
    path('logout', views.logoutPage, name="logout"),
    path('quiz-page/<str:pk>', views.quizPage, name="quiz-page"),
    path('sign-up', views.signupPage, name="sign-up"),
    path('quiz-page/<str:pk>/save/', views.save_quiz_view, name="save-quiz"),
    path('result/<str:pk>/', views.resultPage, name="result-page"),
    path('score-page/', views.scorePage, name="score-page")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
