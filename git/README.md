# Comandos Básicos de Git

## Configuração Inicial
Esses comandos são usados para configurar o Git no seu sistema:

```bash
# Configura o nome de usuário
git config --global user.name "Seu Nome"

# Configura o e-mail do usuário
git config --global user.email "seu.email@example.com"

# Verifica a configuração
git config --list


# Inicializa um novo repositório Git
git init

# Clona um repositório remoto
git clone https://github.com/user/repo.git


# Mostra o status atual dos arquivos no repositório
git status

# Exibe o histórico de commits
git log

# Adiciona arquivos para o próximo commit
git add nome_do_arquivo

# Adiciona todos os arquivos modificados
git add .

# Realiza um commit com uma mensagem
git commit -m "Mensagem do commit"

# Adiciona e faz commit diretamente (atalho)
git commit -am "Mensagem do commit"


# Adiciona um repositório remoto
git remote add origin https://github.com/user/repo.git

# Envia alterações para o repositório remoto (branch principal)
git push origin main

# Puxa as alterações do repositório remoto
git pull origin main

# Cria uma nova branch
git branch nome_da_branch

# Troca para uma branch existente
git checkout nome_da_branch

# Cria e troca para uma nova branch
git checkout -b nome_da_branch

# Mescla uma branch com a branch atual
git merge nome_da_branch

# Deleta uma branch
git branch -d nome_da_branch

# Desfaz alterações locais em um arquivo (não confirmadas)
git checkout -- nome_do_arquivo

# Reseta um commit (mantém as mudanças locais)
git reset nome_do_commit

# Reseta um commit permanentemente (desfaz as mudanças)
git reset --hard nome_do_commit

# Guarda temporariamente mudanças não commitadas
git stash

# Aplica mudanças guardadas no stash
git stash apply

# Remove mudanças guardadas no stash
git stash drop

# Exibe as branches remotas e locais
git branch -a

# Renomeia uma branch
git branch -m novo_nome_da_branch

# Lista os arquivos modificados em cada commit
git log --stat

# Mostra as diferenças entre arquivos modificados e o último commit
git diff


