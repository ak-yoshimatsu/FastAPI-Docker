from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# Baseクラスからsqlalchemyモデルを作成
from .databases import Base


# usersテーブル
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    # リレーションシップ作成 itemsテーブル
    items = relationship('Item', back_populate='owner')


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    # 外部キー
    owner_id = Column(Integer, ForeignKey('users.id'))
