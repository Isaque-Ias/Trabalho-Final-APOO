# Autenticar Usuário

# Atores:

> Usuário

> Administrador

# Pré-condições
> O usuário não está autenticado

# Pos-condições
> 1. O usuário deve estar autenticado dentro do sistema
> 2. 1. O usuário deverá estar na página do curso em que ele possui mais progresso
> 2. 2. O administrador deverá estar na página de visão geral do sistema

# Fluxo principal
> 1. O usuário preenche o formulário com as credenciais de sua conta
> 2. Os dados do formulário são enviados para o sistema
> 3. O sistema autentica os dados
> 4. O usuário é liberado para usar as funcionalidades do sistema

# Fluxos alternativos
> *Não há fluxos alternativos*

# Exceções
> E1 - O usuário informa credenciais inválidas

>> ## Passo 2
>> 3. O usuário é informado da inválidade de suas credenciais