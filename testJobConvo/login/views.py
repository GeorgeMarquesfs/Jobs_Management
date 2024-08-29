from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse

def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
        # Aqui você pode usar um método para autenticar o usuário
        user = authenticate(request, username=email, password=senha)
        
        if user is not None:
            auth_login(request, user)
            if email == 'usuario@example.com':
                return redirect('users_home')
            elif email == 'empresa@example.com':
                return redirect('companies_home')
        else:
            return HttpResponse("Credenciais inválidassss")
    
    return render(request, 'login/login.html')
