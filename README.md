É uma aplicação para gerenciamento de vagas de emprego e candidaturas. O sistema permite que empresas publiquem vagas, candidatos se inscrevam, e empresas visualizem e avaliem as candidaturas com base em critérios pré-definidos.

## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Testes](#testes)
- [Imagens](#Imagens)


## Instalação

1. **Clone o repositório:**

   *git clone [link do repositorio...]*

2. **Crie um ambiente virtual e ative-o:**

   *python -m venv venv*
   *venv\Scripts\activate  #para IOS use: source venv/bin/activate*

3. **Execute as migrações:**
   
   *python manage.py migrate*

4. **Crie um superusuário (opcional, para acessar o admin):**

   *python manage.py createsuperuser*

## Uso

1. **Inicie o servidor de desenvolvimento:**

   *python manage.py runserver*

2. **Acesse a aplicação no navegador:**

   * Página principal: http://127.0.0.1:8000/

3. **Funcionalidades:**

   * Empresas: Criar e gerenciar vagas de emprego.
   * Candidatos: Inscrever-se em vagas e visualizar a lista de candidaturas.

## Testes

1. **Para rodar os testes automatizados:**

   *python manage.py test*

   * Os testes garantirão que a aplicação está funcionando conforme o esperado. Certifique-se de que todas as dependências de teste estão instaladas.



## Imagens

   * Aqui estão algumas capturas de tela da aplicação para mostrar como ela está:

### Página Login 

![login](https://github.com/user-attachments/assets/59ae4d87-f1a2-44f2-b358-1f866a38bee8)

### Área da Empresa

![Criar vaga](image-1.png)

![Lista de Vagas](image-2.png)

![Candidados](image-3.png)

### Área Usuário

![Lista de Vagas para se candidatar](image-4.png)

![Se candidatar a uma vaga](image-5.png)

