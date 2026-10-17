    ## História 1 ##

Como aluno, eu quero escolher uma disciplina, ver os horários livres de um monitor e reservar um deles, para ser atendido sem precisar trocar mensagens e sem conflito de horário. - Prioridade: Mais Alta - Justificativa: A reserva de horários é o núcleo do pedido e evita o conflito que gera a confusão atual (vários alunos no mesmo horário e monitores sem ninguém). As demais funções dependem de ela existir. - Trecho do e-mail do cliente: “A ideia é que o aluno escolha a disciplina, veja os horários livres e reserve um atendimento.” “Se a reserva de horários funcionar, já ajuda muito.”

Critério 1: Ao escolher uma disciplina, o sistema lista os monitores dessa disciplina.
Cenário 1: Dado que sou um aluno logado e existem monitores cadastrados em Cálculo, quando escolho a disciplina Cálculo, então o sistema lista os monitores dessa disciplina.
Critério 2: Ao escolher um monitor, o sistema retorna apenas os horários ainda livres, cada um com dia, hora de início e hora de fim.
Cenário 2: Dado que sou um aluno logado e o monitor X tem 5 horários livres (seg 14:00-14:30, seg 14:30-15:00, ter 10:00-10:30, ter 10:30-11:00, qua 16:00-16:30), quando escolho o monitor X, então o sistema exibe os 5 horários, cada um com dia, hora de início e hora de fim.
Critério 3: Ao escolher um horário, o sistema solicita que o aluno diga qual é a área da dúvida naquela matéria.
Cenário 3: Dado que sou um aluno logado e o monitor X, de Cálculo, tem o horário seg 14:00-14:30 livre, quando escolho esse horário, então o sistema me pergunta qual é a área da dúvida em Cálculo, com as opções Limites, Derivadas e Integrais para eu selecionar.
Critério 4: Horários já reservados por outro aluno não aparecem na lista de horários livres.
Cenário 4: Dado que sou um aluno logado e o horário seg 14:00-14:30 do monitor X já foi reservado por outro aluno, quando escolho o monitor X, então o sistema exibe apenas os horários seg 14:30-15:00, ter 10:00-10:30, ter 10:30-11:00 e qua 16:00-16:30.
Critério 5: Ao reservar um horário livre, o sistema registra a reserva e o horário passa a ficar indisponível para os demais alunos.
Cenário 5: Dado que sou um aluno logado e o horário seg 14:00-14:30 do monitor X está livre, quando reservo esse horário, então o sistema registra a reserva e o horário deixa de aparecer como livre para os demais alunos.
Critério 6: Dado que sou um aluno logado, estou vendo o horário seg 14:00-14:30 do monitor X como livre e outro aluno o reserva antes de eu confirmar, quando tento confirmar a minha reserva, então o sistema recusa a reserva e informa que o horário está indisponível.
Cenário 6: Dado um horário já reservado por outro aluno, quando tento reservá-lo, então o sistema recusa a reserva e informa que o horário está indisponível.
Critério 7: Se o monitor escolhido não tiver horários livres, o sistema informa isso e sugere outro monitor da mesma disciplina que tenha horários livres.
Cenário 7: Dado que sou um aluno logado, o monitor X, de Cálculo, não tem horários livres e o monitor Y, também de Cálculo, tem horários livres, quando escolho o monitor X, então o sistema informa que não há horários livres e sugere o monitor Y.
Critério 8: Ao escolher um horário de um monitor que aceita atendimento em grupo, o sistema deve perguntar ao aluno se a monitoria será em grupo ou individual.  
Cenário 8: Dado que sou um aluno logado e o monitor X, que aceita atendimento em grupo, tem o horário seg 14:00-14:30 livre, quando escolho esse horário, então o sistema me pergunta se a monitoria será em grupo ou individual, com as duas opções para eu selecionar.  
Critério 9: Ao escolher um horário de um monitor que não aceita atendimento em grupo, o sistema não deve exibir a pergunta sobre grupo e deve registrar a reserva como individual.  
Cenário 9: Dado que sou um aluno logado e o monitor Y, que atende apenas individualmente, tem o horário ter 10:00-10:30 livre, quando escolho esse horário e confirmo a reserva, então o sistema não exibe a pergunta sobre atendimento em grupo e registra a reserva como individual.  
Critério 10: O sistema deve indicar, para cada monitor listado, se ele aceita atendimento em grupo ou apenas individual.  
Cenário 10: Dado que sou um aluno logado e, em Cálculo, o monitor X aceita atendimento em grupo e o monitor Y atende apenas individualmente, quando escolho a disciplina Cálculo, então o sistema lista o monitor X com a indicação “aceita grupo” e o monitor Y com a indicação “individual”.

--------------------antigo atualizar----------------------- 2. Como coordenação, eu quero consultar as horas de monitoria realizadas por cada monitor em um período, para calcular o pagamento das bolsas.

- Critérios de aceitação:
  1. O sistema permite à coordenação informar um período (data inicial e data final) e considera apenas as monitorias dentro dele.
  2. O sistema retorna, para cada monitor, o total de horas das monitorias realizadas no período.
  3. O sistema não conta monitorias canceladas nem monitorias ainda não realizadas.
  4. Se nenhum monitor tiver horas no período, o sistema informa isso.
  5. O sistema permite essa consulta apenas à coordenação e recusa qualquer outro tipo de usuário.
- Cenários de teste:
  1. Dado o período de 01/10 a 31/10, quando a coordenação consulta, então o sistema considera apenas as monitorias realizadas nesse período.
  2. Dado que um monitor realizou 4 monitorias de 30 minutos no período, quando a coordenação consulta, então o sistema mostra 2 horas para esse monitor.
  3. Dado que há uma monitoria cancelada e outra ainda não realizada no período, quando a coordenação consulta, então nenhuma das duas entra na soma.
  4. Dado que nenhum monitor realizou monitorias no período, quando a coordenação consulta, então o sistema informa que não há horas no período.
  5. Dado um usuário que é aluno, quando ele tenta fazer a consulta, então o sistema recusa o acesso.
- Prioridade: Média
- Justificativa: É necessária para o pagamento das bolsas e lida com informação restrita, mas depende de a reserva já existir, e o cliente deixa claro que a reserva é a prioridade.
- Trecho do e-mail do cliente: "A coordenação precisa de um relatório mensal com as horas atendidas por cada monitor, porque isso conta para o pagamento da bolsa. Essas informações de bolsa não podem ficar visíveis para todo mundo."
