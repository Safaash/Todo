from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Todo
from django.db.models import Q 


# Create your views here.


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
        
def home(request):
   
    data=Todo.objects.all()
    return render (request,'home.html',{'data':data})

def delete(request,id):
        pi=Todo.objects.get(pk=id)
        pi.delete()
        return redirect('/')


       
def edit(request,id):
     
    pi=Todo.objects.get(pk=id)
        
    return render(request,'update.html',{'pi':pi})  
        
def update(request,id):
    
    pi=Todo.objects.get(pk=id) 
   
       
    pi.title=request.POST['title']
    pi.desc=request.POST['desc']
    pi.save()
       
    
    return redirect('/')



  
       

 

    # def get_queryset(self): # new
    #     query = self.request.GET.get('q')
    #     object_list = City.objects.filter(
    #         Q(name__icontains=query) | Q(state__icontains=query)
    #     )
    #     return object_list
