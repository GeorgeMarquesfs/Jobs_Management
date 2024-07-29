
## Aplicação de Gerenciamento de Vagas de Emprego e Candidaturas

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
   
   *venv\Scripts\activate* ~ Windows
   
   *source venv/bin/activate* ~ IOS
   
3. **Caso você não tenha o Django instalado, instale-o utilizando pip:**

    *pip install django*

4. **Execute as migrações:**
   
   *python manage.py migrate*

5. **Crie um superusuário (opcional, para acessar o admin):**

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

  * Página de login possui dois usuários (Empresa e Candidato)

![login](https://github.com/user-attachments/assets/59ae4d87-f1a2-44f2-b358-1f866a38bee8)

### Área da Empresa

  * A empresa pode cadastrar novas vagas:
    
![CadastroVagas](https://github.com/user-attachments/assets/e3862699-2020-4997-a7b1-16d07eee9af4)

  * Ao fazer o cadastro de uma nova vaga, mostrará uma lista de todas as vagas que estao ativas, a empresa pode editar ou até mesmo excluir a vaga.
    
![ListaVagasAtivas](https://github.com/user-attachments/assets/ff158090-dbe5-4236-882c-5e8294470316)

  * Ao clicar em "Ver Candidatos (i)", irá visualizar todos os candidatos a vaga com as suas respectivas informações (Pretensão salarial, Experiência, Última Escolaridade)
  * Possui também o "Score" onde:
    * Se dentro da faixa salarial, adiciona 1 ponto
    * Se dentro ou acima da escolaridade, adiciona 1 ponto
      
![ListaCandidatosVagas](https://github.com/user-attachments/assets/5ac34fcb-7349-4d65-bf64-f378f72ce4cb)

  * Ao clicar em "Relatório", verá:
    * Relatório de Vagas Criadas por Mês
    * Relatório de Candidatos Recebidos por Mês e por Vaga

![RelatorioVagasPorMes](https://github.com/user-attachments/assets/f9c84952-6d89-4945-85a6-56c0f08f5251)

![RelatorioCandidatosMesEAno](https://github.com/user-attachments/assets/57c9edbe-87c2-4061-bc46-8d9ac5ca3d66)

**Para esta situação hipotética e de teste, eu modifiquei o mês no computador para criar vagas e me candidatar a vagas em meses diferentes.**

### Área Usuário

  * Na área do usuário / candidato, ele vera todas as vagas disponíveis

![ListaVagasDisponiveis](https://github.com/user-attachments/assets/20015243-5105-49b2-96df-32eb6f143951)

  * Ao clicar em "Candidatar" ele colocará suas informações, seu nome, pretensão salarial, experiência e última escolaridade.

![CandidatarAVaga](https://github.com/user-attachments/assets/c873dd43-1954-4909-9f00-39fd2e1658ac)

