from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config.config import DATABASE_URL


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    redirect_uris = Column(String)
    client_name = Column(String)
    logo_url = Column(String)
    application_type = Column(String)
    grant_types = Column(String)
    response_type = Column(String)


class App(Base):
    __tablename__ = "apps"

    id = Column(String, primary_key=True, index=True)
    is_staging = Column(Boolean)
    is_verified = Column(Boolean)
    logo_url = Column(String)
    name = Column(String)
    verified_app_logo = Column(String)
    engine = Column(String)
    sign_in_with_world_id = Column(Boolean)
    can_user_verify = Column(String)
    action_id = Column(Integer, ForeignKey('actions.id'))
    action = relationship('Action', back_populates='app')


class Action(Base):
    __tablename__ = "actions"

    id = Column(Integer, primary_key=True, index=True)
    external_nullifier = Column(String)
    name = Column(String)
    action = Column(String)
    description = Column(String)
    max_verifications = Column(Integer)
    max_accounts_per_user = Column(Integer)
    app_id = Column(String, ForeignKey('apps.id'))
    app = relationship('App', back_populates='action')
