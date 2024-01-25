# sqlalchemyインポート
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# sqlalchemyへのデータベースURK作成
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root@db:3306/demo?charset=utf8'

# sqlalchemyエンジン作成
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# SessionLocalクラス作成 ← インスタンス化するとデータベースセッションになる
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Baseクラス作成 ← このクラスを継承してORMモデルを作成する
Base = declarative_base()
