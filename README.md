# intranet
Intranet Empresarial feita com Django

ACESSO:
    http://127.0.0.1:8000/

DADOS DE LOGIN DO SUPERUSER:
    http://127.0.0.1:8000/admin/
    user: admin
    password: admin

INSTALAÇÃO NO SERVIDOR E CONFIGURAÇÕES INICIAIS:
Requisitos:

Preparação do ambiente:
    sudo apt install python3-pip python3 python3-dev python3-venv gcc default-libmysqlclient-dev libssl-dev nginx curl

Atualização dos arquivos
    python3 -m pip install --upgrade pip setuptools wheel --user
    export PATH="/home/$USER/.local/bin:$PATH"
    python3 -m pip install pipenv --user

Criar pasta
    mkdir intranet
Entrar na pasta
    cd intranet

Criando o ambiente virtual
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install django gunicorn pillow
