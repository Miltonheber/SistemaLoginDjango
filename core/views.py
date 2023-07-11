from django.shortcuts import render
from django.shortcuts import redirect
from core.models import Usuario


def cadastro(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if len(nome.strip()) == 0 or len(senha.strip()) == 0 or len(email.strip()) == 0:
            return redirect('/cadastro/?status=0')
        else:
            try:
                user = Usuario.objects.get(
                        email = email
                        )
            except:
                usuario = Usuario(nome=nome, senha=senha, email=email)
                usuario.save()
                return redirect('/login/?status=0')

            else:
                return redirect('/cadastro/?status=1')

            
    status = request.GET.get('status')
    contexto = {
            'status':status

            }

    return render(request, 'cadastro.html', contexto)


def login(request):

    if request.method == 'POST':
        email = request.POST.get('email').strip()
        senha = request.POST.get('senha').strip()

        try: 
            usuario = Usuario.objects.get(email=email, senha=senha)
            print(usuario)
        except:
            return redirect('/login/?status=2')

        else:
            request.session['login'] = [True, usuario.id]
            return redirect('/login/?status=1')
             
    status = request.GET.get('status')
    return render(request, 'login.html', {'status':status})



def logout(request):
    del request.session['login']
    return redirect('/login/?status=3')
             

        


