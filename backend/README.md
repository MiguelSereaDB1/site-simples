# FastAPI CI/CD Smoke Test

Aplicacao minima para validar pipeline e deploy no FastAPI Cloud.

## Endpoints

- `GET /` retorna um payload simples de ola mundo.

## Execucao local

```bash
uv run fastapi dev app/main.py
```

## Escopo

Sem stack de banco de dados (alembic/asyncpg/sqlalchemy) nem dev-toolchain (pytest/ruff/mypy/testcontainers) por enquanto — o app atual e so o smoke test acima. Essas dependencias entram junto com os tickets 02/03 (`.scratch/clothing-management/issues/`) quando houver codigo real para testar/tipar/persistir.
