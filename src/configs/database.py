import os


POSTGRES_HOST = os.getenv('POSTGRES_H')
print(f"POSTGRES_HOST: {POSTGRES_HOST}")

DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{POSTGRES_HOST}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}?client_encoding=utf8"

print (f"DATABASE_URL: {DATABASE_URL}")
