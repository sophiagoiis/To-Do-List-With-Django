from django.db import models

# Create your models here.
#Models é sobre banco de dados

class Task(models.Model): #ao herdar isso em () o Django entende que essa classe é uma tabela no banco de dados
    title = models.CharField(max_length=200) #crio uma coluna chamada title na tabela, É onde vai ficar o nome da tarefa, ex: "Estudar Django"
    completed = models.BooleanField(default=False) # É o "checkbox" da sua ToDoList. Cria uma coluna chamada completed na tabela. BooleanField = campo que só aceita True ou False e o defoult ta = a false pq vai começar como nao concluida por padrao
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add=True = preenche automaticamente com a data/hora atual no momento em que a tarefa é criada

# "me mostre o MEU título"
def  __str__(self):
    return self.title 

