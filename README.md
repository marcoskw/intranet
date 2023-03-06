# intranet
Intranet Empresarial feita com Django

ACESSO:
    http://127.0.0.1:8000/

DADOS DE LOGIN DO SUPERUSER:
    http://127.0.0.1:8000/admin/
    user: admin
    password: admin

# Instalando
    sudo apt install python3-pip 
    sudo apt install python3 
    sudo apt install python3-dev 
    sudo apt install python3-venv 
    sudo apt install gcc 
    sudo apt install default-libmysqlclient-dev 
    sudo apt install libssl-dev 
    sudo apt install nginx 
    sudo apt install curl
    sudo apt install git
    sudo apt install django-summernote

# Atualizando pip e demais
    python3 -m pip install --upgrade pip setuptools wheel --user
    export PATH="/home/$USER/.local/bin:$PATH"
    python3 -m pip install pipenv --user

# Criar pasta no diretorio: /home/*****usuario*****/intranet
    git clone https://github.com/marcoskw/
    chmod -R 777 intranet/.
# atenção para as permissoes que você der... (estou em servidor teste)

# Criando o ambiente virtual
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install django gunicorn pillow python-decouple
    chmod -R 777 intranet/.
# atenção para as permissoes que você der... (estou em servidor teste)    
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    


# Criando o arquivo
    sudo nano /etc/systemd/system/gunicorn.socket
    
# COLAR (SEM EDIÇÃO)
    [Unit]
    Description=gunicorn socket

    [Socket]
    ListenStream=/run/gunicorn.sock

    [Install]
    WantedBy=sockets.target


# Criando outro arquivo
    sudo nano /etc/systemd/system/gunicorn.service

# Editar, depois Colar
    [Unit]
    Description=gunicorn daemon
    Requires=gunicorn.socket
    After=network.target

    [Service]
    User=*****usuario*****
    Group=www-data
    WorkingDirectory=/home/*****usuario*****/intranet
    ExecStart=/home/*****usuario*****/intranet/venv/bin/gunicorn \
            --access-logfile - \
            --workers 3 \
            --bind unix:/run/gunicorn.sock \
            intranet.wsgi:application

    [Install]
    WantedBy=multi-user.target

# Ativando
    sudo systemctl start gunicorn.socket
    sudo systemctl enable gunicorn.socket

# Checando
    sudo systemctl status gunicorn.socket
    sudo systemctl status gunicorn
    curl --unix-socket /run/gunicorn.sock localhost
    sudo systemctl status gunicorn

    sudo nano /etc/nginx/sites-enabled/sitedjango

# Configurando o nginx server block
    server {
        listen 80;
        server_name localhost;

        location = /favicon.ico { access_log off; log_not_found off; }
        
        location /static/ {
            root /home/*****usuario*****/intranet;
        }

        location /media {
            alias /home/*****usuario*****/intranet/media/;
        }

        location / {
            include proxy_params;
            proxy_pass http://unix:/run/gunicorn.sock;
        }
    }

# start
    sudo rm /etc/nginx/sites-enabled/default
    sudo systemctl restart nginx
    sudo systemctl restart gunicorn


# AJUSTE FINAL:
# ubuntu
    sudo usermod -a -G "*****usuario*****" www-data

# cent-os
    sudo usermod -a -G "*****usuario*****" nginx

