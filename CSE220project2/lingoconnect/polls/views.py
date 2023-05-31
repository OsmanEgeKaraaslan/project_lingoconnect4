from django.shortcuts import render, redirect
from .models import Question, Choice, UserAnswer
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def home(request):
    return render(request, 'home.html')



class CustomLoginView(LoginView):
    template_name = 'polls/quiz.html'


def login_view(request):
    if request.user.is_authenticated:
        return redirect('polls:home')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                return redirect('polls:home')  # Redirect to home page after successful login
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})



@login_required
def question(request):
    if request.method == 'POST':
        # Process form submission
        questions = Question.objects.all()
        for question in questions:
            choice_id = request.POST.get(str(question.id))
            if choice_id:
                choice = Choice.objects.get(id=choice_id)
                UserAnswer.objects.create(
                    user=request.user,
                    question=question,
                    choice=choice
                )
        return redirect('polls:quiz_result')  # Redirect to quiz result page after submitting answers
    else:
        # Display the questions
        questions = Question.objects.all()
        return render(request, 'question.html', {'questions': questions})


@login_required(login_url='login')
def quiz(request):
    if request.method == 'POST':
        # Process form submission
        questions = Question.objects.all()
        for question in questions:
            choice_id = request.POST.get(str(question.id))
            if choice_id:
                choice = Choice.objects.get(id=choice_id)
                UserAnswer.objects.create(
                    user=request.user,
                    question=question,
                    choice=choice
                )
        return redirect('polls:quiz_result')  # Redirect to quiz result page after submitting answers
    else:
        # Display the questions
        questions = Question.objects.all()
        return render(request, 'quiz.html', {'questions': questions})



@login_required
def quiz_result(request):
    user_answers = UserAnswer.objects.filter(user=request.user)
    return render(request, 'quiz_result.html', {'user_answers': user_answers})


def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('polls:home')  # Redirect to home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'custom_login.html', {'form': form})