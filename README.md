# Sport Predit

O intuito desse projeto é receber inputs de um usuário e prever qual esporte seria mais adequado para uma pessoa praticar;

# Estruturação do Projeto:

### Estrutura básica:

- O projeto está dividido em três partes: Modelo de Machine Learning, Frontend com Vuejs e Backend com Django.

### Motivações por trás do projeto:

- Tem sido uma aventura incrível aprender cada vez mais sobre Machine Learning, e com essa proposta de projeto poderia aperfeiçoar cada vez mais meu conhecimento sobre o assunto, além de ter a oportunidade de fazer uma integração um pouquinho mais complexa do modelo com um frontend e um backend!

### Detalhes sobre a estrutura do projeto:

- Modelo de Machine Learning:

  - A plataforma utilizada para construir o modelo foi "Jupyter Notebook";
  - O pré processamento dos dados foi feito através da lib "pandas" do python;
  - O modelo foi construído utilizando a lib "sckit-learn", utilizando o modelo de Decision Tree Classifier;
  - O modelo possui uma assertividade de 83%;

    ![Modelo de Ml](/imgs/modelo.png)

- Frontend com Vuejs:

  - O frontend possui como features: Login, Register, Logout, Gerar inputs para o Modelo de ML e exibir os predicts gerados;
  - Por meio do front o usuário pode gerar inputs para o modelo que por sua vez devolve como output um Array Numpy;

![Frontend](/imgs/vue.png)

- Backend com Django:

  - Controla todo o fluxo de login, register e logout;
  - Responsável por manter a comunicação do frontend com o banco de dados;
  - O modelo gera predicts assim que os dados do usuário são salvos no banco, ou seja, o modelo está intrisicamente ligado ao backend --> Um "nice-to-have" aqui seria subir um container separado para o modelo e o servir para o django (em andamento)

![Frontend](/imgs/django.png)

# Instruções para rodar a aplicação:

1º Passo: entre na pasta raiz do projeto

```
$ cd sport_ml_djavue/
```

2º Passo: crie e inicie os containers

```
# Para criar os containers
$ docker compose build
ou
$ docker-compose build

# Para iniciar os containers
$ docker compose up backend frontend -d
ou
$ docker-compose up backend frontend -d
```

3º Passo: Acesse "localhost" no navegador e Pronto, o projeto ja estara rodando localmente!

4º Passo: Registre-se e faça Login para acessar a aplicação corretamente

- Clique em "register"
  ![Registre-se](/imgs/home.png)

- Preencha os dados corretamente e clique em "Create Account"
  ![Criar conta](/imgs/register.png)

- Pronto, agora é so logar com os dados registrados!

# Orientações para rodar o projeto utilizando apimock:

```
$
$ docker compose -f docker-compose.yml -f docker-compose.apimock.yml up frontend

```

# Link para o video:

[Full Stack Project](https://youtu.be/LEMgMOCGBpQ)
