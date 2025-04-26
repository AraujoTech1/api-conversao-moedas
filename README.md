<h1 align="center">💱 API de Conversão de Moedas</h1>


## Descrição do Projeto

O projeto é uma aplicação desenvolvida com Python e FastAPI, que permite converter valores entre diferentes moedas de maneira simples, rápida e eficiente. Seu principal objetivo é facilitar integrações com sistemas que necessitam de valores convertidos em tempo real, sendo útil para desenvolvedores, estudantes e sistemas de simulação.

### Funcionalidades do Projeto

- ✅ Conversão entre moedas (ex: USD para BRL)
- ✅ Rota com documentação interativa automática
- ✅ Validação automática de parâmetros
- ✅ Retorno estruturado em JSON

## Testes de Software

Foram realizados os seguintes testes:

- **Teste de funcionamento da rota `/converter`**:
  - `GET /converter?valor=100&de=USD&para=BRL`
    - Resultado esperado: conversão correta com status 200
- **Teste de depuração**:
  - Envio de parâmetros inválidos para verificar mensagens de erro da API
  - Exemplo: `GET /converter?valor=abc&de=USD&para=BRL`
    - Resultado esperado: API retorna erro 422 com validação clara

## Tecnologias e Linguagens Utilizadas

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-blue?logo=fastapi&logoColor=blue)
![JSON](https://img.shields.io/badge/JSON-Format-blue?logo=json&logoColor=blue)

## Bibliotecas e Frameworks

![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-blue?logo=uvicorn)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-blue?logo=python)

## Documentação Oficial

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Swagger UI](https://swagger.io/tools/swagger-ui/)

## Licença

Este projeto está sob a Licença MIT.  

Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<p align="center">
  🔹 Desenvolvido por <a href="https://github.com/AraujoTech1">Fernanda Araujo</a> 🔹
</p>
