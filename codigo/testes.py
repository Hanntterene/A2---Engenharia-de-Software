import unittest
from classes import Horario, Monitor, Agenda

# critério 1 - sussesso
def teste_listar_monitores_da_diciplina_sucesso(self):
    # Dado: Monitores exemplo:
    agenda = Agenda()
    monitores = [
        Monitor("Alice", "a2669994", "Calculo"),
        Monitor("Bob", "a222222", "Física"),
        Monitor("Charlie", "a333333", "Calculo"),
        Monitor("David", "a444444", "Calculo"),
        Monitor("Eve", "a555555", "Calculo"),
        Monitor("Frank", "a666666", "Física"),
        Monitor("Grace", "a777777", "Calculo"),
        Monitor("Heidi", "a888888", "POO"),
        Monitor("Ivan", "a999999", "Física"),
        Monitor("Judy", "a101010", "POO")
    ]
    for Monitor in monitores:
        agenda.cadastrar_monitor(monitor)


    # Quando: Listar monitores da disciplina "Calculo"
    resultado = agenda.listar_monitores_da_disciplina("Calculo")

     # Então: aparecem só os 5 monitores de Cálculo
             self.assertEqual(len(resultado), 5)
        for monitor in resultado:
            self.assertEqual(monitor.disciplina, "Cálculo")

# criterio 1 - falha
def teste_disciplinas_sem_monitores(self):
    # Dado agenda sem monitores de fisica
    agenda = Agenda()
    monitores = [
            Monitor("Alice", "a2669994", "Calculo"),
            Monitor("Charlie", "a333333", "Calculo"),
            Monitor("David", "a444444", "Calculo"),
            Monitor("Eve", "a555555", "Calculo"),
            Monitor("Grace", "a777777", "Calculo"),
            Monitor("Heidi", "a888888", "POO"),
            Monitor("Judy", "a101010", "POO")
        ]
        for Monitor in monitores:
            agenda.cadastrar_monitor(monitor)

        #quando: Listar monitores da disciplina "Física"
        resultado = agenda.listar_monitores_da_disciplina("Física")

        # Então: não aparecem monitores de Física
        self.assertEqual(len(resultado), 0)

    # criterio 2 - sucesso
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


    #criterio 2 - falha
    def teste_monitor_sem_horarios_cadastrados(self):
         #dado: um monitor sem horários cadastrados
        agenda = Agenda()
        agenda.cadastrar_monitor(Monitor("Bob", "a222222", "Física"))
        # Quando: escolho o monitor
        resultado = agenda.listar_horarios_livres(agenda.monitores[0])
        # Então: não aparecem horários livres 
         self.assertEqual(len(resultado), 0)


  if __name__ == "__main__":
    unittest.main() 