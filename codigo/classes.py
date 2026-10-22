class Horario:
    def __init__(self, dia, inicio, fim):
        self.dia = dia
        self.inicio = inicio
        self.fim = fim
        self.livre = True


class Monitor:
    def __init__(self, nome, matricula, disciplina):
        self.nome = nome
        self.matricula = matricula
        self.disciplina = disciplina
        self.horarios = []


class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


class Reserva:
    def __init__(self, aluno, horario):
        self.aluno = aluno
        self.horario = horario


class Agenda:
    def __init__(self):
        self.monitores = []
        self.reservas = []

    def cadastrar_monitor(self, monitor):
        self.monitores.append(monitor) #Recebe um monitor e guarda na lista da agenda

    def listar_monitores(self, disciplina):
        monitoresEncontrados = [] #Lista de monitores encontrados
        for monitor in self.monitores:  #Vai procurando o monitor na lista de monitores
            if monitor.disciplina == disciplina:        #Se o monitor realmente estiver na disciplina procurada
                monitoresEncontrados.append(monitor)    #Salva o monitor na lista de monitores encontrados 
        return monitoresEncontrados     #Retorna a lista dos monitores encontrados

    def listar_horarios_livres(self, monitor):
        #Mostra os horarios livres dos monitores (se alguem tiver)
        horariosLivres = []     #Lista de horarios livres
        for horario in monitor.horarios:
            if horario.livre:       #Se o monitor tiver horario livre
                horariosLivres.append(horario)      #Ele salva na lista de horarios
        return horariosLivres       #E retorna a lista dos horarios livres

    def reservar(self, aluno, horario):
        #Precisa do aluno pra saber quem vai agendar e o horario que ele quer
        pass

    def sugerir_monitor(self, monitor):
        #Precisa de um monitor sem nenhum horario livre para ai sim recomendar outro
        pass


