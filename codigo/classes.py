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
        #Precisa so do nome do monitor para cadastrar
        pass

    def listar_monitores(self, disciplina):
        #Precisa da disciplina para mostrar o monitor
        pass

    def listar_horarios_livres(self, monitor):
        #Precisa do monitor para ver o horario disponivel do mesmo
        pass

    def reservar(self, aluno, horario):
        #Precisa do aluno pra saber quem vai agendar e o horario que ele quer
        pass

    def sugerir_monitor(self, monitor):
        #Precisa de um monitor sem nenhum horario livre para ai sim recomendar outro
        pass


