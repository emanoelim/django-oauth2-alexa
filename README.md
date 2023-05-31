Projeto criado para testar a integração com uma skill da Alexa. Foi baseado neste tutorial:
https://www.youtube.com/watch?v=NrBBM9XhzG0.

Como testar:

- Instalar as dependências do requirements: `pip install -r requirements.txt`.
- Rodar as migrations: `python manage.py migrate`.
- Criar um user admin: `python manage.py createsuperuser`.
- Rodar o projeto: `python manage.py runserver`.
- Criar um usuário para a skill da Alexa em: http://127.0.0.1:8000/admin/auth/user/.
- Na skill que está desenvolvendo, acessar o menu "account linking".
- Ativar a opção "Do you allow users to create an account or link to an existing account with you?".
- Em "Select an authorization grant type" selecionar a opção "Implicit Grant".
- Vão aparecer 3 urls em "Alexa Redirect URLs", para o Brasil é a "pitangui". Copiar ela.
- Criar um novo provider no django: http://127.0.0.1:8000/admin/oauth2_provider/application/.
  - Client id: será gerado automaticamente.
  - Redirect uris: colar a url que você copiou antes.
  - Client type: confidential.
  - Authorization grant type: implicit.
  - Client secret: será gerado automaticamente.
  - Name, Skip authorization e Algorithm: não alterei.

- Instalar o ngrok e rodar o comando `ngrok http 8000`.`
- Copiar o link gerado pelo ngrok.
- Na tela de account linking da skill:
  - Your Web Authorization URI: link_ngrok/o/authorize/.
  - Your Client ID: cliend id do provider criado no django.
  - Salvar.
  
- Acessando o app da Alexa no celular, a skill aparecerá nas skills em desenvolvimento.
- Ao clicar em "configurações" vai aparecer a opção de vincular conta.
- Você será redirecionado para uma página de login do django.
- Preencher com usuário e senha do usuário que você criou.
- Deve aparecer uma mensagem dizendo que a conta foi vinculada com sucesso.