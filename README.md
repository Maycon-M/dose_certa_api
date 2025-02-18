
# Dose Certa API

![Static Badge](https://img.shields.io/badge/any_text-3.12-blue?style=flat-square&label=Python&labelColor=%232daaff)
![Static Badge](https://img.shields.io/badge/pypi-FastAPI%20v0.115.6-%23038C73?style=flat-square)

O projeto Dose Certa é uma aplicação de lembretes de remedios para pessoas que possuem dificuldades de lembrar dos horários das suas medicações. Essa API compoem o back-end da aplicação.

Esse projeto esta sendo utilizando nas disciplinas de Interface Homem Máquina e Infraestrutura em Nuvem com AWS.

## Autores

- [@Maycon-M](https://github.com/Maycon-M)

## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`POSTGRES_H`

`POSTGRES_USER`

`POSTGRES_PASSWORD`

`POSTGRES_DB`

`POSTGRES_PORT`

## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/Maycon-M/dose_certa_api.git
```

Entre no diretório do projeto

```bash
  cd dose_certa_api
```

Construa uma imagem a partir do docker-compose.yaml

```bash
  docker-compose -f docker/docker-compose.yaml -p backend_dose_certa up --build
```

### Rodando as migrações do banco de dados

Após subir os containers, aplique as migrações para garantir que o banco esteja atualizado:

```bash
    docker exec -it backend_dose_certa-backend-1 alembic upgrade head
```

Caso precise criar uma nova migração ao modificar os modelos:

```bash
docker exec -it backend_dose_certa-backend-1 alembic revision --autogenerate -m "descrição da migração"
docker exec -it backend_dose_certa-backend-1 alembic upgrade head
```

## Documentação da API

A API possui Documentação feita com Swagger. Após construir a imagem no docker acesse:

``` bash
    http://localhost:8000/docs
```
