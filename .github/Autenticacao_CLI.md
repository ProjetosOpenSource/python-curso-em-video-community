## 🟢 Método 1: GitHub CLI (Recomendado para Iniciantes)

O **GitHub CLI** (`gh`) é a ferramenta oficial de linha de comando do GitHub. Ele gerencia as credenciais de forma automática e segura, dispensando o uso de senhas ou chaves complexas.

### 1. Instalação

* **Windows:**
Abra o Terminal/PowerShell e execute:
```powershell
winget install --id GitHub.cli
```

* **Linux (Debian/Ubuntu):**
```Bash
sudo apt install gh
```

* **macOS:**
```Bash
brew install gh
```

### 2. Autenticação
Abra o terminal e execute:
```
gh auth login
```

Siga os passos na tela:
* What is your preferred protocol for Git operations? -> Escolha HTTPS
* Authenticate Git with your GitHub credentials? -> Escolha Yes
* How would you like to authenticate GitHub CLI? -> Escolha Login with a web browser
* Copie o código de 8 dígitos exibido no terminal, pressione Enter e cole o código na página do navegador que se abrirá.

### 3. Clonando o Repositório
Após o login, execute o comando de clone usando a URL HTTPS do seu fork:
```
gh repo clone SEU-NOME/python-curso-em-video-community
```
