# 🔑 Método 2: Autenticação por SSH

O método por SSH utilza um par de chaves criptográficas (uma pública cadastrada no GitHub e uma privada salva no seu computador). É uma opção muito segura e bastante utilizada no mercado.

### 1. Verificar se você já possui uma chave SSH
Abra o terminal e execute:
```Bash
cat ~/.ssh/id_ed25519.pub
```
Se o terminal exibir um texto começando com ssh-ed25519 ..., você já tem uma chave. Caso contrário, crie uma no passo a seguir.

### 2. Gerar uma nova chave SSH
No terminal, execute o comando abaixo substituindo pelo e-mail da sua conta do GitHub:
```Bash
ssh-keygen -t ed25519 -C "seu-email@exemplo.com"
```
O terminal fará algumas perguntas durante o processo:

* *Enter file in which to save the key...* -> Pressione Enter para aceitar o local e nome padrão do arquivo.
  
* *Enter passphrase (empty for no passphrase):* -> Digite uma senha segura da sua escolha e pressione Enter.
  
(Nota: O terminal não exibirá asteriscos ou caracteres enquanto você digita por questões de segurança. Apenas digite a  senha e aperte Enter).

* *Enter same passphrase again:* -> Digite a mesma senha novamente para confirmar e pressione Enter.

### 3. Copiar e Adicionar a Chave ao GitHub
Exiba e copie o conteúdo da sua chave pública:
```Bash
cat ~/.ssh/id_ed25519.pub
```
1. Vá ao GitHub, clique na sua foto de perfil (canto superior direito) -> Settings.
2. Na barra lateral esquerda, clique em SSH and GPG keys.
3. Clique no botão verde New SSH key.
4. No campo Title, dê um nome para o seu computador (ex: Notebook Pessoal).
5. Cole a chave copiada no campo Key e clique em Add SSH key.

### 4. Clonando o Repositório
Com a chave cadastrada, clone o repositório utilizando a URL SSH do seu fork:
```Bash
git clone git@github.com:SEU-USUARIO/python-curso-em-video-community.git
```

