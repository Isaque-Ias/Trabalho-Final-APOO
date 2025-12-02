# Adicionar Amizade

# Atores:

> Usuário

# Pré-condições
> 1. O usuário deve estar autenticado no sistema

# Pos-condições
> 1. O usuário é redirecionado para a tela de cursos
> 2. A pontuação do usuário no sistema para o respectivo curso é aumentada
> 3. O progresso do usuário no curso é atualizado

# Fluxo principal
> 1. O usuário acessa o perfil de um usuário
> 2. O usuário pede para adicionar um perfil em suas amizades
> 3. O sistema envia o pedido para o perfil

# Fluxos alternativos
> A1 - O usuário adiciona um amigo por meio de um amigo

>> ## passo 1
>> 2. O usuário acessa as amizades de um perfil adicionado
>> 3. O pede para adicionar uma dessas amizades em suas amizades
>> 4. O sistema envia o pedido para essa amizade

# Exceções
> E1 - O perfil acessado é do próprio usuário 
>> ## Passo 1
>> 2. O sistema impede que o usuário seja adicionado

> E2 - A mensagem não chega no perfil
>> ## Passo 4
>> 5. O usuário é informado que o pedido não foi enviado