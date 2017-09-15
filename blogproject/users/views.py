from django.shortcuts import render,redirect

from .forms import RegisterForm

# 带表单的视图函数的经典写法
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',context={'form':form})
