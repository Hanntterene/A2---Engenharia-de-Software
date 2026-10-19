import unittest
from classes import Horario, Monitor, Agenda

def teste_listar_monitores_da_diciplina(self):
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

if __name__ == "__main__":
    unittest.main()