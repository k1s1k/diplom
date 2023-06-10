from sqlalchemy import Column,ARRAY, Float ,create_engine, DateTime, ForeignKey, Text, Boolean, String, BigInteger, UUID
from sqlalchemy import func, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
import hashlib
# import main.config as config
#
Base = declarative_base()

class Roles(Base):
    __tablename__ = 'Roles'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(length=30), nullable=False)
    delete = Column(Boolean, default=False)

class Users(Base):
    __tablename__ = 'Users'
    id = Column(BigInteger, primary_key=True)
    email = Column(String(length=250), nullable=False)
    password = Column(String(length=255), nullable=False)
    phone = Column(String(length=17), nullable=False)
    name = Column(String(length=250), nullable=False)
    gender = Column(Boolean, default=False)
    role_id = Column(BigInteger, ForeignKey(Roles.id), nullable=False)

class Catalogs(Base):
    __tablename__ = 'Catalogs'
    id = Column(BigInteger, primary_key=True)
    gender = Column(Boolean, default=False)
    name = Column(String(length=250), nullable=False)
    attachmeant_id = Column(ARRAY(BigInteger), default=list())
    delete = Column(Boolean, default=False)

class Clothes(Base):
    __tablename__ = 'Clothes'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(length=250), nullable=False)
    size = Column(String(length=2), nullable=False)
    price = Column(Float, nullable=False)
    attachmeant_id = Column(ARRAY(BigInteger), default=list())
    discription = Column(String(length=250), nullable=False)
    catalog_id = Column(BigInteger, ForeignKey(Catalogs.id), nullable=False)
    delete = Column(Boolean, default=False)

class Type_servise(Base):
    __tablename__ = 'Type_servise'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(length=250), nullable=False)
    attachmeant_id = Column(ARRAY(BigInteger), default=list())
    delete = Column(Boolean, default=False)

class Servise(Base):
    __tablename__ = 'Servise'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(length=250), nullable=False)
    discription = Column(String(length=250), nullable=False)
    Type_servise = Column(BigInteger, ForeignKey(Type_servise.id), nullable=False)
    attachmeant_id = Column(ARRAY(BigInteger), default=list())
    castom_discription = Column(String(length=250), nullable=False)
    servise_prise = Column(Float, nullable=False)
    delete = Column(Boolean, default=False)

class Status(Base):
    __tablename__ = 'Status'
    id = Column(BigInteger, primary_key=True)
    title_status = Column(String(length=250), nullable=False)

class Baskets(Base):
    __tablename__ = 'Baskets'
    id = Column(BigInteger, primary_key=True)
    Users_id = Column(BigInteger, ForeignKey(Users.id), nullable=False)
    status_id = Column(BigInteger, ForeignKey(Status.id), nullable=False)
    data_time_create = Column(DateTime)

class Backets_collections(Base):
    __tablename__ = 'Backets_collections'
    id = Column(BigInteger, primary_key=True)
    baskets_id = Column(BigInteger, ForeignKey(Baskets.id), nullable=False)
    clothes_id = Column(BigInteger, ForeignKey(Clothes.id), nullable=False)
    servise_id = Column(BigInteger, ForeignKey(Servise.id), nullable=False)
    status_id = Column(BigInteger, ForeignKey(Status.id), nullable=False)

class Attachmeants(Base):
    __tablename__ = 'Attachmeants'
    id = Column(BigInteger, primary_key=True)
    type = Column(String(length=250), nullable=False)
    path = Column(String(length=250), nullable=False)
    delete = Column(Boolean, default=False)




#
# def hash_password(password: str) -> str:
#     h = hashlib.new('sha256')
#     h.update(password.encode('utf-8'))
#     return h.hexdigest()
#
#
# Base = declarative_base()
#
#
# class Users(Base):
#     __tablename__ = 'Users'
#     id = Column(BigInteger, primary_key=True)
#     username = Column(String(length=30), nullable=False)
#     password = Column(String(length=255), nullable=False)
#     email = Column(String(length=100), nullable=False)
#     avatar = Column(String(length=255), nullable=True)
#     online = Column(Boolean, default=False)
#     is_active = Column(Boolean, default=False)
#
#     def verify_password(self, password):
#         return self.password == hash_password(password)
#
#
# class Tokens(Base):
#     __tablename__ = 'Tokens'
#     id = Column(BigInteger, primary_key=True)
#     type = Column(String(length=100), nullable=False, default='regular')
#     token = Column(UUID(as_uuid=False), unique=True, nullable=False, index=True,
#                    server_default=text('uuid_generate_v4()'))
#     datetime_create = Column(DateTime, default=func.now(), nullable=False)
#     expires = Column(DateTime, nullable=False)
#
#     # Foreign Key
#     user_id = Column(BigInteger, ForeignKey(Users.id), nullable=False)
#
#
# class UserData(Base):
#     __tablename__ = 'UserData'
#     id = Column(BigInteger, primary_key=True)
#     last_readed_message_id = Column(BigInteger, nullable=True)
#     last_user_from_readed = Column(BigInteger, nullable=True)
#     another = Column(String(length=255), nullable=True)
#     # Сюда можно всякий хлам накидать что можно использовать в будущем
#
#     # Foreign Key
#     user_id = Column(BigInteger, ForeignKey(Users.id), nullable=False)
#
#
# class PlayLists(Base):
#     __tablename__ = 'PlayLists'
#     id = Column(BigInteger, primary_key=True)
#     name = Column(String(length=30), nullable=False)
#     cover = Column(String(length=255), nullable=True)
#
#     # Foreign Key
#     user_id = Column(BigInteger, ForeignKey(Users.id), nullable=False)
#
#
# class Musics(Base):
#     __tablename__ = 'Musics'
#     id = Column(BigInteger, primary_key=True)
#     name = Column(String(length=30), nullable=False)
#     author = Column(String(length=30), nullable=False)
#     genre = Column(String(length=50), default=False)
#     picture = Column(String(length=255), nullable=True)
#     path = Column(String(length=255), nullable=False)
#     time_duration = Column(String(length=20), default=False)
#     datetime_add = Column(DateTime, nullable=False, default=func.now())
#
#     # Foreign Key
#     user_id_add = Column(BigInteger, ForeignKey(Users.id), nullable=False)
#
#
# class Collections(Base):
#     __tablename__ = 'Collections'
#     id = Column(BigInteger, primary_key=True)
#
#     # Foreign Key
#     music_id = Column(BigInteger, ForeignKey(Musics.id), nullable=False)
#     playlist_id = Column(BigInteger, ForeignKey(PlayLists.id), nullable=False)
#
#
# class Messages(Base):
#     __tablename__ = 'Messages'
#     id = Column(BigInteger, primary_key=True)
#     text = Column(Text, nullable=True)
#
#     # Foreign Key
#     user_id_from = Column(BigInteger, ForeignKey(Users.id), nullable=False)
#     user_id_to = Column(BigInteger, nullable=False)
#     message_reply_id = Column(BigInteger, nullable=True)
#     playlist_id = Column(BigInteger, ForeignKey(PlayLists.id), nullable=False)
#     music_id = Column(BigInteger, ForeignKey(Musics.id), nullable=False)
#
#
# engine = create_engine(
#     f'postgresql+psycopg2://{config.DATABASE_USER}'
#     f':{config.DATABASE_PASSWORD}'
#     f'@{config.DATABASE_IP}'
#     f'/{config.DATABASE_NAME}',
#     echo=False,
#     pool_recycle=300,
#     query_cache_size=0,
#     pool_pre_ping=True,
#     client_encoding="utf8",
#     pool_size=10,
#     max_overflow=2,
#     pool_use_lifo=True
# )
#
# Base.metadata.create_all(engine)
# Session = scoped_session(sessionmaker())
# Session.configure(bind=engine)
# Footer
# © 2023 GitHub, Inc.
# Footer navigation
# Terms
# Privacy
# Security
# Stat