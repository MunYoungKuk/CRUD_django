from django.shortcuts import render,redirect
from .models import Question,Comment

# Create your views here.
def index(request):
    questions = Question.objects.all()
    
    return render(request,"question/index.html",{"questions":questions})
    
def new(request):
    return render(request,"question/new.html")
    
def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    
    Question.objects.create(title=title,content=content)
    return redirect("/question/")
    
def read(request,id):
    question = Question.objects.get(pk=id)
    # comments = Comment.objects.filter(question.id= id)
    return render(request,"question/read.html",{"question":question})
    
def edit(request,id):
    question = Question.objects.get(pk=id)
    return render(request,"question/edit.html",{"question":question})

def update(request,id):
    question = Question.objects.get(pk=id)
    
    title= request.POST.get("title")
    content = request.POST.get("content")
    
    question.objects.create(question=question,content=content)
    
    return redirect(f"/question/{id}")
    
def delete(request,id):
    question = Question.objects.get(pk=id)
    question.delete()
    
    return redirect("/question")
    
def comment_create(request,id):
    question =Question.objects.get(pk=id)
    content = request.POST.get("content")
    
    Comment.objects.create(question=question,content=content)
    return redirect(f"/question/{id}/")