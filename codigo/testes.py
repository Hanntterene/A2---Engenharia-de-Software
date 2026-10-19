import unittest

from classes import Agenda, Horario, Monitor


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


if __name__ == "__main__":
    unittest.main()
