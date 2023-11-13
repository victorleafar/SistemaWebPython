# SistemaWebPython CRUD Básico
Configuração Inicial
Criação do Projeto:
Iniciei o projeto Django usando o comando django-admin startproject SistemaWebPython
Criação do Aplicativo: Criei um aplicativo dentro do projeto usando o comando 
python manage.py startapp meu_app.

Executando o Servidor de Desenvolvimento
Iniciar o Servidor de Desenvolvimento:
Iniciei o servidor de desenvolvimento Django usando o comando 
python manage.py runserver.
Acesso ao Site Localmente:
Acessei o site localmente no meu navegador através do endereço http://127.0.0.1:8000/.

### **Passo 1: Instalar o Python**
1. **Baixe o Python:**
   - Acesse [python.org](https://www.python.org/downloads/).
   - Escolha a versão mais recente compatível com o seu sistema operacional.
   - Durante a instalação, marque a opção "Add Python to PATH" ou "Adicionar Python ao PATH".

2. **Verificar a Instalação:**
   - Abra um terminal ou prompt de comando.
   - Digite:
     ```bash
     python --version
     ```
     Isso deve exibir a versão do Python instalada.

### **Passo 2: Clonar o Repositório e Instalar Dependências**
3. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/victorleafar/SistemaWebPython.git
   cd SistemaWebPython
   ```

4. **Instalar Dependências:**
   ```bash
   pip install -r requirements.txt
   ```
   Certifique-se de que o `requirements.txt` inclua as versões corretas das dependências.

### **Passo 3: Configurar o Banco de Dados e Criar um Superusuário**
5. **Configurar o Banco de Dados:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Criar um Superusuário (Opcional):**
   ```
   python manage.py createsuperuser
   ```

### **Passo 4: Executar o Servidor**
7. **Executar o Servidor:**
   python manage.py runserver


8. **Acessar a Administração (Opcional):**
Link visitaveis
URL/admin
URL/produt_list
URL/produt_create
URL/produt_update
URL/produt_delete
URL/

