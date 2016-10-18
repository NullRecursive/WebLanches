#WebLanches
_Application web_

### Intro
Django é um framework gratuito e de código aberto para a criação de aplicações web, escrito em Python. É um framework web, ou seja, é um conjunto de componentes que ajuda a desenvolver sites de forma mais rápida e mais fácil.

###Instalação
- Instale o python no Ubuntu e seus derivados  
``` sudo apt install python3.5 ```  

- Para saber a versao do python  
``` python3 --version ```  

- Editor de código
	- IDE
		- PyCharm
		- Spyder
	- Outros
		- [Atom](atom.io) (Recomendado)
		- Sublime Text 
		- Gedit

- Configurar o ambiente virtual(tambem chamado de virtualenv)  
``` python3 -m venv myvenv ```  
	- Em caso de erro execute:  
	``` sudo apt install python-virtualenv ```  
	``` virtualenv --python=python3.5 myvenv ```  
	- Agora ative o virtualvenv
	 ``` . myvenv/bin/activate  ```  
	 Apos isso seu terminal devera se parecer com isso: ```  (myvenv) ~/local_do_arquivo$ ```

- Instale o Django
``` pip install django==1.8.5 ```  
	- Em caso de erro instale o pip  
	``` sudo apt install pip ```  

### Uso
- Para criar sua aplicacao, use:
``` django-admin startproject nome_projeto ```  

- Faça as configurações iniciais
	- Mude a TIME_ZONE para seu local
	- Adicione ao final do arquivo, abaixo de STATIC_URL:
	``` STATIC_ROOT = os.path.join(BASE_DIR, 'static') ```

- Instale o banco de dados:
	- Se for SQLite, ele ja é o padrao
	- Se for outro, tera que procurar na documentacao e ir em settings.py coloca a definicao do banco em DATABASES
	- Para executar a criação do banco de dados:
	``` python manage.py migrate ```
- Pronto, agora so iniciar o server local ou externo
	- Server Externo, recomendado o [PythonAnywhere](www.pythonanywhere.com)
	- Para iniciar o local:
	``` python manage.py runserver ```
	- Para acessar local:
	``` http://127.0.0.1:8000/ ```
- Para criar um app 
 ``` python manage.py startapp nome_app ```
- Para criar migraçoes dos apps
 ``` python manage.py makemigrations nome_app ```

