# DBマイグレーション
from sqlalchemy import create_engine
from .databases import Base

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root@db:3306/demo?charset=utf8'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == '__name__':
    reset_database()

# 以下のコマンドでマイグレーション実行
# $ docker compose exec app poetry run python -m api.migrate_db

# alembic init実行
# $ poetry run alembic init migrations <- フォルダ名
