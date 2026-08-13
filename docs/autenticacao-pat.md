# 🌐 Método 3: HTTPS com Personal Access Token (PAT)

O método HTTPS tradicional não aceita mais a senha comum da sua conta do GitHub por razões de segurança. Em vez disso, você deve criar um Personal Access Token (PAT) que funciona como uma senha de acesso restrito.

### 1. Criando o Personal Access Token

  1. No GitHub, clique na sua foto de perfil → Settings.

  2. No final do menu da esquerda, clique em Developer settings.

  3. Acesse Personal access tokens → Tokens (classic).

  4. Clique em Generate new token → Generate new token (classic).

  5. No campo Note, digite um nome identificador (ex: Acesso Terminal Curso em Video).

  6. Defina a expiração (Expiration) para o prazo desejado (ex: 90 dias ou No expiration).

  7. Marque a caixinha principal repo (concede acesso total aos repositórios).

  8. Role a página até o final e clique em Generate token.

  9. Copie e guarde o token gerado! (O GitHub só exibirá esse código uma única vez).

### 2. Clonando o Repositório

Clone o repositório utilizando a URL HTTPS do seu fork:
```Bash
git clone https://github.com/SEU-NOME/python-curso-em-video-community.git
```

### 3. Autenticando no Terminal

Quando você executar o comando git push para enviar suas alterações:

* **Username:** Digite seu nome de usuário do GitHub.

* **Password:** Cole o Personal Access Token gerado (não digite sua senha normal da conta).
