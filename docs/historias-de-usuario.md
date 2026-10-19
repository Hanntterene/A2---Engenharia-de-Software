    ## História 1 ##

Como aluno, eu quero escolher uma disciplina, ver os horários livres de um monitor e reservar um deles, para ser atendido sem precisar trocar mensagens e sem conflito de horário.

- Prioridade: Mais Alta
- Justificativa: A reserva de horários é o núcleo do pedido e evita o conflito que gera a confusão atual (vários alunos no mesmo horário e monitores sem ninguém). As demais funções dependem de ela existir.
- Trecho do e-mail do cliente: “A ideia é que o aluno escolha a disciplina, veja os horários livres e reserve um atendimento.” “Se a reserva de horários funcionar, já ajuda muito.”

> Critério 1: Ao escolher uma disciplina, o sistema lista os monitores dessa disciplina.
> Cenário 1: Dado que sou um aluno logado e existem monitores cadastrados em Cálculo, quando escolho a disciplina Cálculo, então o sistema lista os monitores dessa disciplina.

> Critério 2: Ao escolher um monitor, o sistema retorna apenas os horários ainda livres, cada um com dia, hora de início e hora de fim.
> Cenário 2: Dado que sou um aluno logado e o monitor X tem 5 horários livres (seg 14:00-14:30, seg 14:30-15:00, ter 10:00-10:30, ter 10:30-11:00, qua 16:00-16:30), quando escolho o monitor X, então o sistema exibe os 5 horários, cada um com dia, hora de início e hora de fim.

> Critério 3: Horários já reservados por outro aluno não aparecem na lista de horários livres.
> Cenário 3: Dado que sou um aluno logado e o horário seg 14:00-14:30 do monitor X já foi reservado por outro aluno, quando escolho o monitor X, então o sistema exibe apenas os horários seg 14:30-15:00, ter 10:00-10:30, ter 10:30-11:00 e qua 16:00-16:30.

> Critério 4: Ao reservar um horário livre, o sistema registra a reserva e o horário passa a ficar indisponível para os demais alunos.
> Cenário 4: Dado que sou um aluno logado e o horário seg 14:00-14:30 do monitor X está livre, quando reservo esse horário, então o sistema registra a reserva e o horário deixa de aparecer como livre para os demais alunos.

> Critério 5: Dado que sou um aluno logado, estou vendo o horário seg 14:00-14:30 do monitor X como livre e outro aluno o reserva antes de eu confirmar, quando tento confirmar a minha reserva, então o sistema recusa a reserva e informa que o horário está indisponível.
> Cenário 5: Dado um horário já reservado por outro aluno, quando tento reservá-lo, então o sistema recusa a reserva e informa que o horário está indisponível.

> Critério 6: Se o monitor escolhido não tiver horários livres, o sistema informa isso e sugere outro monitor da mesma disciplina que tenha horários livres.
> Cenário 6: Dado que sou um aluno logado, o monitor X, de Cálculo, não tem horários livres e o monitor Y, também de Cálculo, tem horários livres, quando escolho o monitor X, então o sistema informa que não há horários livres e sugere o monitor Y.

    ## História 2 ##

Como coordenação, eu quero consultar as horas de monitoria realizadas por cada monitor em um período, para calcular o pagamento das bolsas. - Prioridade: Média - Justificativa: É necessária para o pagamento das bolsas e lida com informação restrita, mas depende de a reserva já existir, e o cliente deixa claro que a reserva é a prioridade. - Trecho do e-mail do cliente: “A coordenação precisa de um relatório mensal com as horas atendidas por cada monitor, porque isso conta para o pagamento da bolsa. Essas informações de bolsa não podem ficar visíveis para todo mundo.”

> Critério 1: O sistema permite à coordenação informar um período (data inicial e data final) e considera apenas as monitorias dentro dele.
> Cenário 1: Dado que a coordenação está logada, há uma monitoria realizada em 15/10 e outra realizada em 02/11, quando ela consulta o período de 01/10 a 31/10, então o sistema considera apenas a monitoria de 15/10.

> Critério 2: O sistema retorna, para cada monitor, o total de horas das monitorias realizadas no período.
> Cenário 2: Dado que a coordenação está logada e o monitor X tem 4 monitorias de 30 minutos marcadas como realizadas entre 01/10 e 31/10, quando ela consulta o período de 01/10 a 31/10, então o sistema mostra 2 horas para o monitor X.

> Critério 3: O sistema não conta monitorias canceladas nem monitorias ainda não realizadas.
> Cenário 3: Dado que a coordenação está logada e o monitor X tem, em outubro, 2 monitorias de 30 minutos marcadas como realizadas, 1 cancelada e 1 ainda não realizada, quando ela consulta o período de 01/10 a 31/10, então o sistema mostra 1 hora para o monitor X.

> Critério 4: Se nenhum monitor tiver horas no período, o sistema informa isso.
> Cenário 4: Dado que a coordenação está logada e nenhum monitor realizou monitorias entre 01/10 e 31/10, quando ela consulta esse período, então o sistema informa que não há horas no período.

> Critério 5: O sistema permite essa consulta apenas à coordenação e recusa qualquer outro tipo de usuário.
> Cenário 5: Dado que sou um aluno logado, quando tento consultar as horas de monitoria dos monitores, então o sistema recusa o acesso.

    ## História 3 ##

Como monitor, eu quero cadastrar os horários em que posso atender, para que os alunos reservem direto pelo sistema, sem precisar combinar cada atendimento por mensagem. - Prioridade: Alta - Justificativa: Sem os horários cadastrados pelos monitores, o aluno não tem o que reservar. Esta história alimenta a reserva de horários, que é o núcleo do pedido, e substitui o PDF no Moodle. - Trecho do e-mail do cliente: “Hoje os horários das monitorias são divulgados em um PDF no Moodle, e os alunos combinam o atendimento direto com os monitores, por mensagem.”

> Critério 1: O sistema deve permitir que o monitor logado cadastre um horário de atendimento informando dia e hora de início.
> Cenário 1: Dado que sou o monitor X, de Cálculo, logado e sem nenhum horário cadastrado, quando cadastro o horário de segunda-feira às 14:00, então o sistema salva o horário e o exibe na minha lista de horários cadastrados.

> Critério 2: O sistema deve registrar cada horário com duração de 30 minutos.
> Cenário 2:Dado que sou o monitor X logado, quando cadastro o horário de segunda-feira às 14:00, então o sistema registra o horário como seg 14:00-14:30.

> Critério 3: O sistema não deve permitir cadastrar um horário que se sobreponha a outro já cadastrado pelo mesmo monitor.
> Cenário 3: Dado que sou o monitor X logado e já tenho cadastrado seg 14:00-14:30, quando tento cadastrar um horário na segunda-feira às 14:15, então o sistema recusa o cadastro e informa que o horário conflita com outro já cadastrado.

> Critério 4: O sistema deve exibir os horários cadastrados como livres para os alunos da disciplina do monitor.
> Cenário 4: Dado que o monitor X, de Cálculo, cadastrou seg 14:00-14:30 e sou um aluno logado, quando escolho a disciplina de Cálculo e o monitor X, então o sistema exibe seg 14:00-14:30 como horário livre.

> Critério 5: O sistema deve permitir que o monitor informe se aceita atendimento em grupo ou apenas individual, valendo essa escolha para todos os seus horários.
> Cenário 5: Dado que sou o monitor X logado e tenho os horários seg 14:00-14:30 e ter 10:00-10:30 cadastrados, quando informo que aceito atendimento em grupo, então o sistema salva essa escolha e os dois horários passam a aceitar atendimento em grupo.

> Critério 6: O sistema deve permitir o cadastro de horários apenas a usuários com perfil de monitor.
> Cenário 6: Dado que sou aluno apenas, logado, quando tento acessar a tela de cadastro de horários de atendimento, então o sistema nega o acesso e não exibe a tela de cadastro.
