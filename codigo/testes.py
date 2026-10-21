import unittest

from classes import Agenda, Aluno, Horario, Monitor


class TestAgenda(unittest.TestCase):
    # critério 1 - sucesso
    def teste_listar_monitores_da_diciplina_sucesso(self):
        # Dado: Monitores exemplo:
        agenda = Agenda()
        monitores = [
            Monitor("Alice", "a2669994", "Cálculo"),
            Monitor("Bob", "a222222", "Física"),
            Monitor("Charlie", "a333333", "Cálculo"),
            Monitor("David", "a444444", "Cálculo"),
            Monitor("Eve", "a555555", "Cálculo"),
            Monitor("Frank", "a666666", "Física"),
            Monitor("Grace", "a777777", "Cálculo"),
            Monitor("Heidi", "a888888", "POO"),
            Monitor("Ivan", "a999999", "Física"),
            Monitor("Judy", "a101010", "POO"),
        ]
        for monitor in monitores:
            agenda.cadastrar_monitor(monitor)

        # Quando: Listar monitores da disciplina "Cálculo"
        resultado = agenda.listar_monitores("Cálculo")

        # Então: aparecem só os 5 monitores de Cálculo
        self.assertEqual(len(resultado), 5)
        for monitor in resultado:
            self.assertEqual(monitor.disciplina, "Cálculo")

    # critério 1 - falha
    def teste_disciplinas_sem_monitores(self):
        # Dado agenda sem monitores de Física
        agenda = Agenda()
        monitores = [
            Monitor("Alice", "a2669994", "Cálculo"),
            Monitor("Charlie", "a333333", "Cálculo"),
            Monitor("David", "a444444", "Cálculo"),
            Monitor("Eve", "a555555", "Cálculo"),
            Monitor("Grace", "a777777", "Cálculo"),
            Monitor("Heidi", "a888888", "POO"),
            Monitor("Judy", "a101010", "POO"),
        ]
        for monitor in monitores:
            agenda.cadastrar_monitor(monitor)

        # Quando: Listar monitores da disciplina "Física"
        resultado = agenda.listar_monitores("Física")

        # Então: não aparecem monitores de Física
        self.assertEqual(len(resultado), 0)

    # critério 2 - sucesso
    def teste_listar_horarios_livre(self):
        # Dado: um monitor cadastrado com 3 horários
        agenda = Agenda()
        alice = Monitor("Alice", "a2669994", "Cálculo")
        alice.horarios.append(Horario("Segunda", "14:00", "14:30"))
        alice.horarios.append(Horario("Segunda", "14:30", "15:00"))
        alice.horarios.append(Horario("Terça", "10:00", "10:30"))
        agenda.cadastrar_monitor(alice)

        # Quando: escolho o monitor
        resultado = agenda.listar_horarios_livres(alice)

        # Então: aparecem os 3, cada um com dia, início e fim
        self.assertEqual(len(resultado), 3)
        self.assertEqual(resultado[0].dia, "Segunda")
        self.assertEqual(resultado[0].inicio, "14:00")
        self.assertEqual(resultado[0].fim, "14:30")

    # critério 2 - falha
    def teste_monitor_sem_horarios_cadastrados(self):
        # Dado: um monitor sem horários cadastrados
        agenda = Agenda()
        agenda.cadastrar_monitor(Monitor("Bob", "a222222", "Física"))

        # Quando: escolho o monitor
        resultado = agenda.listar_horarios_livres(agenda.monitores[0])

        # Então: não aparecem horários livres
        self.assertEqual(len(resultado), 0)

    #critério 3 - sucesso
    def teste_horario_resevado_não_aparece_livre(self):
        #dado: monitor com 5 horários cadastrados, sendo 1 reservado
        agenda = Agenda()
        alice = Monitor("Alice", "a2669994", "Cálculo")
        h = [
            Horario("Quarta", "10:00", "10:30"), 
            Horario("Quarta", "10:30", "11:00"), 
            Horario("Quarta", "11:00", "11:30"), 
            Horario("Quarta", "11:30", "12:00"), 
            Horario("Quarta", "12:00", "12:30")]
        for horario in h:
            alice.horarios.append(horario)
        agenda.cadastrar_monitor(alice)

        outro_aluno = Aluno("Carlos", "a123456")
        agenda.reservar(outro_aluno, h[3])  # Reservando o terceiro horário

        #quando: escolho o monitor
        resultado = agenda.listar_horarios_livres(alice)

        #então: só aparecem os 4 horários livres, o reservado não aparece
        self.assertEqual(len(resultado), 4)
        self.assertNotIn(h[3], resultado)  # O horário reservado não deve estar na lista de horários livres

    #critério 4 - sucesso
    def test_reserva_horario_livre_registra_reserva(self):

        #Dado um monitor com 4 horarios registrados
        agenda = Agenda()
        alice = Monitor("Alice", "a2669994", "Cálculo")
        h = [
            Horario("Quarta", "10:00", "10:30"), 
            Horario("Quarta", "10:30", "11:00"), 
            Horario("Quarta", "11:00", "11:30"), 
            Horario("Quarta", "11:30", "12:00")]
        for horario in h:
            alice.horarios.append(horario)
        agenda.cadastrar_monitor(alice)

        #Quando um aluno reserva um horario
        alunoW = Aluno("Willian", "a2260900")
        agenda.reservar(alunoW, h[0])

        #Entao, esse horario registra a reserva dele
        self.assertFalse(h[0].livre)
        self.assertEqual(len(agenda.reservas), 1)
        self.assertEqual(agenda.reservas[0].aluno, alunoW)
        self.assertEqual(agenda.reservas[0].horario, h[0])

    #critério 4 - falha
    def test_reserva_horario_inexistente(self):

        #Dado um monitor com 3 horarios de agendamento cadastrados
        agenda = Agenda()
        heidi = Monitor("Heidi", "a888888", "POO")
        heidi.horarios.append(Horario("Quarta", "15:00", "15:30"))
        heidi.horarios.append(Horario("Quarta", "15:30", "16:00"))
        heidi.horarios.append(Horario("Sexta", "11:00", "11:30"))   
        agenda.cadastrar_monitor(heidi)

        #Quando um aluno tenta reservar um horario inexistente
        alunoJ = Aluno("James", "a1233211")
        horarioInexistente = Horario("Sexta", "13:30", "14:00")
        
        #Entao ele da erro pois nao existe esse horario
        with self.assertRaises(ValueError):
            agenda.reservar(alunoJ, horarioInexistente)
        self.assertEqual(len(agenda.reservas), 0)



        #criterio 5 - falha
        def test_reserva_horario_ocupado(self):
            #Dado um monitor com 4 horarios de agendamento cadastrados e um aluno reserva um horario
            agenda = Agenda()
            heidi = Monitor("Heidi", "a888888", "POO")
            h = [
                Horario("Segunda", "11:00", "11:30"),
                Horario("Segunda", "11:30", "12:00"),
                Horario("Quarta", "13:00", "13:30"),
                Horario("Quarta", "13:30", "14:00")]
            for horario in h:
                heidi.horarios.append(horario) 
            agenda.cadastrar_monitor(heidi)

            alunoP = Aluno("Paul", "a2356000")
            agenda.reservar(alunoP, h[1])

            #Quando outro aluno tenta reservar um horario ocupado
            alunoI = Aluno("Ian", "a2343789")

            #Entao ele da erro pois nao consegue reservar o mesmo horario que outro aluno
            
            with self.assertRaises(ValueError):
                agenda.reservar(alunoI, h[1])
            self.assertEqual(len(agenda.reservas), 1)
            self.assertEqual(agenda.reservas[0].aluno, alunoP)
            self.assertEqual(agenda.reservas[0].horario, h[1])


        #critério 6 - sucesso
    def test_monitor_sem_horarios_sugere_outro_monitor(self):
        #Dado 3 monitores, sendo 2 da mesma materia (com 1 sem horario disponivel) e 1 de outra materia
        agenda = Agenda()
        david = Monitor("David", "a444444", "Cálculo")
        grace = Monitor("Grace", "a777777", "Cálculo")
        judy = Monitor("Judy", "a101010", "POO")
        grace.horarios.append(Horario("Quinta", "15:30", "16:00"))
        judy.horarios.append(Horario("Quinta", "10:00", "10:30"))
        agenda.cadastrar_monitor(david)
        agenda.cadastrar_monitor(grace)
        agenda.cadastrar_monitor(judy)

        #Quando um aluno tenta reservar com um monitor que nao tenha horario disponivel
        alunoK = Aluno("Keidi", "a2683970") #Acabou nem usando o aluno criado
        monitorSugerido = agenda.sugerir_monitor(david)

        #Entao o sistema recomenda alguem da mesma materia que tenha horario disponivel
        self.assertEqual(monitorSugerido, grace)
        

    #critério 6 - falha
    def test_nenhum_monitor_com_horarios_livres(self):
        #Dado 3 monitores da mesma materia, mas o unico que tava com horario livre, foi reservado
        agenda = Agenda()
        alice = Monitor("Alice", "a2669994", "Cálculo")
        charlie = Monitor("Charlie", "a333333", "Cálculo")
        eve = Monitor("Eve", "a555555", "Cálculo")

        h = Horario("Terca", "17:00", "17:30")
        charlie.horarios.append(h)

        agenda.cadastrar_monitor(alice)
        agenda.cadastrar_monitor(charlie)
        agenda.cadastrar_monitor(eve)

        alunoS = Aluno("Sally", "a2356000")
        agenda.reservar(alunoS, h)

        #Quando um aluno tenta reservar com um dos monitores
        monitorSugerido = agenda.sugerir_monitor(alice)

        #Entao nao ha ninguem para sugerir, pois ninguem tem horario disponivel
        with self.assertRaises(ValueError):
            agenda.sugerir_monitor(charlie)
        self.assertEqual(len(agenda.reservas), 1)
        self.assertEqual(agenda.reservas[0].aluno, alunoS)
        self.assertEqual(agenda.reservas[0].horario, h)

if __name__ == "__main__":
    unittest.main()
