from classes import Agenda, Monitor, Horario, Aluno

#Criando a agenda e os monitores
agenda = Agenda()
monitorAlice = Monitor("Alice", "a2669994", "Cálculo")
monitorBob = Monitor("Bob", "a222222", "Cálculo")

#Colocando um horario para o Bob
h1 = Horario("Segunda", "14:00", "14:30")
monitorBob.horarios.append(h1)

agenda.cadastrar_monitor(monitorAlice)
agenda.cadastrar_monitor(monitorBob)

#Mostra os monitores de calculo
print("Monitores de calculo: ")
for monitor in agenda.listar_monitores("Cálculo"):  #Ve se os monitores cadastrados como materia de calculo
    print(monitor.nome)     #Printa todos, neste caso, a Alice e o Bob

#Mostra os horarios livres do Bob
print("Horarios livres do Bob: ")
for horario in agenda.listar_horarios_livres(monitorBob):    #Percorre por todos os horarios livres do bob, que nesse caso so tem um
    print(horario.dia, horario.inicio, horario.fim)     #Mostra o dia e os horarios de inicio e fim


#Sugerindo monitor
monitorSugerido = agenda.sugerir_monitor(monitorAlice)
if monitorSugerido is not None:     #Se tiver algum monitor da mesma materia que a Alice com horario vago que nao seja ela, cai aqui
    print("Alice esta sem horarios para atender. Monitor sugerido: ", monitorSugerido.nome)
else:   #Se nao, cai aqui
    print("No momento, nao temos monitores disponiveis")

#Fazendo um aluno reservar o horario disponivel do Bob
alunoS = Aluno("Sally", "a2263058")     #Cadastra o aluno
agenda.reservar(alunoS, h1) #Faz a reserva
print("Reserva feita para: ", alunoS.nome )
print("Data da reserva:", h1.dia, h1.inicio, "-", h1.fim)

#Tentando reservar o mesmo horario da Sally
alunoC = Aluno("Carlos", "a2456098")    #Cadastra mais um aluno
try:    #Tenta reservar
    agenda.reservar(alunoC, h1)
except ValueError as erro:  #Se der erro, ele cai aqui
    print("Reserva recusada: ", erro)
