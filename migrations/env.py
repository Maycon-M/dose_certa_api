# -*- coding: utf-8 -*-
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Importa a configuração do banco e os modelos
from src.configs.database import DATABASE_URL
from src.models.base import Base
from src.models.entities import lembrete 

# Configurando do Alembic
config = context.config

# Configurando dos logs
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Definindo o metadata para autogeração de migrações
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Executa as migrações no modo offline."""

    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executa as migrações no modo online, conectando-se ao banco de dados."""

    connectable = engine_from_config(
        {"sqlalchemy.url": DATABASE_URL},  # Usa a URL diretamente
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
