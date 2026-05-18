#Nas views crio “funções” ou classes que controlam o que aparece na tela e o que acontece quando o usuário acessa uma URL.

# render → monta o HTML e retorna pro navegador
# redirect → redireciona o usuário pra outra página

from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Task

def index(request): #index pq é convenccional chamar assi a pág principal
    filtro = request.GET.get('filtro', 'todas')

    if filtro == 'concluidas':
        tasks = Task.objects.filter(completed = True) 
    elif filtro == 'pendentes':
        tasks = Task.objects.filter(completed = False)
    else:
        tasks = Task.objects.all() #Esse all() busca todas as tarefas do banco sem nenhuma condição e guarda na variável tasks.

    return render (request, 'tasks/index.html', {
        'tasks': tasks,
        'filtro': filtro
    }) #isso q ta em {} é o contexto

#filter ja vem no django
# render(request, 'nome_do_template', contexto)
#request -> requisição em si
#'tasks/index.html' → qual template usar
#{'tasks': tasks} → envia as tarefas pro HTML, aí você consegue usar {{ tasks }} lá no template

def create_task(request):
    if request.method == 'POST': #verifica se o formulário foi enviado (POST = envio de dados)
        title = request.POST.get('title') # pega o texto que o usuário digitou no input de nome title
        if title: #"Se o usuário digitou alguma coisa no input..."
            Task.objects.create(title=title) #cria a tarefa no banco
    return redirect('index') #manda o user p pag principal

def delete_task(request, task_id): #task_id → o id da tarefa que chegou pela URL
    task = Task.objects.get(id=task_id) # busca uma tarefa específica pelo id.
    task.delete()
    return redirect('index')

#OBS: esse objects eu nao criei, vem no DJANGO. Isso que me da acesso ao banco de dados
# delete vem do django tb

#alterna estados
def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id) #Busca a tarefa específica no banco pelo id.
    task.completed = not task.completed
    task.save()
    return redirect('index')

#Esse completed veio dda classe Task do Models que EU criei
