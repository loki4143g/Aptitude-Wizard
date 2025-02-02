from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from questions.models import Category
from django.core.paginator import Paginator


def homepage(request):
    return render(request,'main/home.html')


@login_required
def category_view(request, section):
    categories = Category.objects.filter(section=section).all()
    return render(request,'main/categoryview.html', {'categories':categories,'section':section})

@login_required
def load_questions(request, name):
    questions = Category.objects.get(name=name).questions.all()

    paginator = Paginator(questions,1)
    page = request.GET.get('page')
    questions = paginator.get_page(page)

    return render(request, 'main/questions.html', {'questions':questions})