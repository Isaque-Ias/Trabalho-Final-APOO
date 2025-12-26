# Gerenciar Questão

# Atores:

> Administrador

# Pré-condições
> 1. O administrador deve estar autenticado no sistema
> 2. O administrador deve estar na interface de gerenciamento de questões

# Pos-condições
> 1. Os dados da tabela de questões serão atualizados

# Fluxo principal
> 1. O administrador seleciona o tipo de gerenciamento (Adicioanr, editar ou excluir)
> 2. O administrador preenche o formulário de gerenciamento com dados adequados
> 3. O sistema valida os campos do formulário
> 4. O sistema modifica o banco de dados
> 4. O sistema devolve uma mensagem de sucesso

# Fluxos alternativos
> *Não há fluxos alternativos*

# Exceções
> E1 - Usuário não insere alterantivas
>> ## Passo 3
>> 4. O sistema devolve um erro explicando que o usuário deve preencher pelo menos dois campos de alterantiva para cada questão

> E2 - O usuário omite ambos os campos de enunciado e imagem
>> ## Passo 3
>> 4. O sistema devolve um erro indicando que pelo menos um dos dois campos deve conter alguma informação

> E3 - O usuário omite omite o título
>> ## Passo 3
>> 4. O sistema devolve um erro pedindo que o usuário insira um título

> E4 - O sistema não conseguiu criar a informação no banco de dados
>> ## Passo 4
>> 5. O sistema devolve um erro genérico informando que não foi possível realizar o gerenciamento
