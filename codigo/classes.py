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
        existeHorario = False
        for monitor in self.monitores:
            if horario in monitor.horarios:
                existeHorario = True
        if not existeHorario:
            raise ValueError("Nao existe esse horario")

        #Ve se ainda tem horario livre, se nao tiver, dá erro
        if not horario.livre:
            raise ValueError("Esse horario esta ocupado!")

        #Salva a reserva
        horario.livre = False
        reserva = Reserva(aluno, horario)
        self.reservas.append(reserva)       #Adiciona a reserva de horario
        return reserva

    def sugerir_monitor(self, monitor):
        for outroMonitor in self.monitores:    #Para cada monitor cadastrado na agenda
            if outroMonitor is monitor:    #Se outroMonitor é o mesmo monitor que o aluno escolheu
                continue        #Pula o monitor escolhido
            if outroMonitor.disciplina != monitor.disciplina:      #Se a disciplina for diferente da solicitada
                continue        #Pula monitores de outra disciplina
            if self.listar_horarios_livres(outroMonitor):      #Se algum outro monitor estiver com algum horario livre
                return outroMonitor        #Ai sim retorna ele
        return None     #Se ninguem tiver disponivel, retorna ninguem
