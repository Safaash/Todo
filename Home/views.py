from django.shortcuts import redirect, render
from .models import Todo
# Add Todo 
def add(request):
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        todo=Todo(title=title,desc=desc)
        if(title=='' or desc==''):
            return redirect('/')
        else:
            todo.save()
            return redirect('/')
# home page
def home(request):
   
    data=Todo.objects.all()
    return render (request,'home.html',{'data':data})
# Delete Todo
def delete(request,id):
        pi=Todo.objects.get(pk=id)
        pi.delete()
        return redirect('/')
#Update Todo   
def edit(request,id):
    pi=Todo.objects.get(pk=id)   
    return render(request,'update.html',{'pi':pi})       
def update(request,id):
    pi=Todo.objects.get(pk=id)       
    pi.title=request.POST['title']
    pi.desc=request.POST['desc']
    pi.save()
    return redirect('/')



  