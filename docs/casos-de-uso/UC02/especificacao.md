# Fazer Questão

# Atores:

> Usuário

# Pré-condições
> 1. O usuário deve estar autenticado no sistema
> 2. O usuário deve ter selecionado uma questão permitida do curso

# Pos-condições
> 1. O usuário é redirecionado para a tela de cursos
> 2. A pontuação do usuário no sistema para o respectivo curso é aumentada
> 3. O progresso do usuário no curso é atualizado

# Fluxo principal
> 1. O usuário responde as perguntas através das alternativas
> 2. O sistema avalia as respostas do usuário e calcula uma pontuação
> 3. A pontuação é matribuida ao usuário
> 4. A pontuação é mostrada para o usuário relatando sua performance

# Fluxos alternativos
> A1 - O sistema se torna indisponível

>> ## passo 2
>> 3. O usuário é informado que o sistema não está disponível no momento
>> 4. O usuário é redirecionado para a tela de login.

# Exceções
> E1 - O usuário omite a resposta para as perguntas

>> ## Passo 1
>> 2. O sistema exige que o usuário insira uma resposta