<h1>Energia Livre Api</h1>
<p>A Energia Livre Api é um sistema desenvolvido para pessoas encontrarem fornecoderos de energia.</p>
<p>Ao utilizar essa API, é possível criar um usuário, fazer login com o usuário e encontrar fornecedores de energia.</p>
<p>A integração com o fron-end pode ser encontrada em: https://clarke-challenge-frontend-igorpetersson.vercel.app/</p>
<p>O repositório do front-end pode ser encontrado em https://github.com/IgorPetersson/clarke_challenge_frontend</p>
<h2>Como instalar e rodar?</h2>
<p>Para instalar o sistema, é necessário seguir alguns passos, como baixar o projeto e fazer instalação das dependências. Para isso, é necessário abrir uma aba do terminal e fazer o seguinte: <p>
<p>É preciso fazer o fork e clonar o projeto.</p>
<p>Entrar na pasta: cd clarke_challenge_backend</p>
<p>Criar um ambiente virtual: python -m venv venv</p>
<p>Entrar no ambiente virtual: source venv/bin/activate</p>
<p>Intalar todas as dependências: pip install -r requirements.txt</p>
<p>Rodar as migrations: flask db init </p>
<p>Criar as tabelas: flask db upgrade </p>
<p>Para rodar o projeto: gunicorn "app:create_app()" </p>
<h6> O sistema estará rodando em http://localhost:8000</h6>
<h2>Utilização</h2>
<p>Para utilizar este sistema, é necessário utilizar um API Client, como o Insomnia</p>
<h4>Rotas</h4>
<h5>GET /api/users</h5>
<p>Essa rota irá retornar todas as informações do usuário. É necessário um token para utilizar a rota.</p>
<h5>POST /api/users/login</h5>
<p>Essa rota fará o login do usuário na plataforma.</p>
<h5>POST /api/users</h5>
<p>Essa rota é resonsável pela criação do usuário.</p>
<h5>GET /api/electric/limit/(int:kwh)</h5>
<p>Essa rota retorna todos os fornecedores com limite minimo de kwh menores ou igual ao kwh do parametro. É necessário um token para utilizar a rota. </p>
