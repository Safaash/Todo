from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),    
    path('add',views.add,name="add"),
    path('delete/<int:id>',views.delete,name="delete") ,  
    path('<int:id>',views.edit,name="edit"),  
    path('update/<int:id>',views.update,name="update"),  
   

   

]
