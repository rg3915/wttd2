# Eventex

Eventex é um projeto elaborado a partir do curso [Welcome to the Django][0] do [Henrique Bastos][1].

O objetivo é criar um site de eventos usando todos os recursos aprendidos durante o curso.

## Exercícios

Alguns exercícios de Python encontram-se [aqui][3].

## Como desenvolver?

Baixe e rode o `setup.sh`.

```
wget https://raw.githubusercontent.com/rg3915/wttd2/master/setup.sh
source setup.sh
```

Ou siga o passo a passo.

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```bash
git clone https://github.com/rg3915/wttd2.git
cd wttd2
python -m venv .wttd2
source .wttd2/bin/activate # Linux
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Testes com Selenium

Leia [aqui][4].

## Como fazer o deploy?

1. Crie uma instância no Heroku.
2. Envie as configurações para o Heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o Heroku.

```bash
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configure o e-mail
git push heroku master --force
```

[0]: www.welcometothedjango.com.br
[1]: henriquebastos.net
[3]: https://github.com/rg3915/wttd2/tree/master/python_ex
[4]: https://github.com/rg3915/wttd2/blob/master/selenium.md