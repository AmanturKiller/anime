from django.shortcuts import render
from .models import New


def news_list(request):
    news_queryset = New.objects.all()  # список объектов
    return render(request, 'news_list.html', {'news': news_queryset})

def new_detail(request, id): # id = 8
    # print(id) # 8
    one_new_object = New.objects.get(id=id)  # 1 объект
    
    one_new_object.views += 1  # меняем значение свойства объекта
    
    if request.user.is_authenticated:
        one_new_object.user_views.add(request.user)
    
    one_new_object.save()  # сохраняем в БД
    
    context = {"new": one_new_object} 
    return render(request, 'new.html', context)
