# Histórias do Usuário:

1. Como aluno, eu quero escolher uma disciplina, ver os horários livres de um monitor e reservar um deles, para ser atendido sem precisar trocar mensagens e sem conflito de horário.

- critérios de aceitação:
  1. Ao escolher uma disciplina, o sistema lista os monitores dessa disciplina.
  2. Ao escolher um monitor, o sistema retorna apenas os horários ainda livres, cada um com data, hora de início e hora de fim.
  3. Horários já reservados por outro aluno não aparecem na lista de horários livres.
  4. Ao reservar um horário livre, o sistema registra a reserva e o horário passa a ficar indisponível para os demais alunos.
  5. Se o aluno tentar reservar um horário já ocupado, o sistema recusa a reserva e informa que o horário está indisponível.
  6. Se o monitor escolhido não tiver horários livres, o sistema informa isso e sugere outro monitor da mesma disciplina que tenha horários livres.
- cenários de teste:
  1. Dado um aluno cadastrado e monitores de Cálculo, quando escolho a disciplina Cálculo, então o sistema lista os monitores dessa disciplina.
  2. Dado que o monitor X tem 5 horários livres (seg 14:00-14:30, seg 14:30-15:00, ter 10:00-10:30, ter 10:30-11:00, qua 16:00-16:30), quando escolho o monitor X, então o sistema exibe os 5 horários, cada um com dia, hora de início e hora de fim.
  3. Dado que 1 dos 5 horários do monitor X já foi reservado por outro aluno, quando escolho o monitor X, então o sistema exibe apenas os 4 horários livres.
  4. Dado um horário livre do monitor X, quando reservo esse horário, então a reserva é registrada e o horário deixa de aparecer como livre.
  5. Dado um horário já reservado por outro aluno, quando tento reservá-lo, então o sistema recusa a reserva e informa que o horário está indisponível.
  6. Dado que o monitor X não tem horários livres e o monitor Y, da mesma disciplina, tem, quando escolho o monitor X, então o sistema informa que não há horários e sugere o monitor Y.
- Prioridade: Alta
- Justificativa: A reserva de horários é o núcleo do pedido e evita o conflito que gera a confusão atual (vários alunos no mesmo horário e monitores sem ninguém). As demais funções dependem de ela existir.
- Trecho do e-mail do cliente: "A ideia é que o aluno escolha a disciplina, veja os horários livres e reserve um atendimento." "Se a reserva de horários funcionar, já ajuda muito."

2. Como coordenação, eu quero consultar as horas de monitoria realizadas por cada monitor em um período, para calcular o pagamento das bolsas.

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
