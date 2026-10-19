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
        
    def listar_monitores(self, disciplina):

    def listar_horarios_livres(self, monitor):

    def reservar(self, aluno, horario):
