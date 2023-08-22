from sqlalchemy import String, Text, Integer, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped
from app.db.database import Base
from datetime import datetime


class Rent(Base):
    __tablename__ = 'rent'
    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    duration: Mapped[int] = mapped_column()
    date: Mapped[datetime] = mapped_column(default=datetime.now())


class Client(Base):
    __tablename__ = 'client'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    date_registration: Mapped[datetime] = mapped_column(default=datetime.now())

    product: Mapped[list['Product']] = relationship(secondary='rent', back_populates='client')


class ProductType(Base):
    __tablename__ = 'product_type'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)

    product: Mapped[list['Product']] = relationship(back_populates='type')


class Product(Base):
    __tablename__ = 'product'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    type_id: Mapped[int] = mapped_column(ForeignKey('product_type.id'))
    description: Mapped[str] = mapped_column(nullable=True)

    type: Mapped['ProductType'] = relationship(back_populates='product')
    client: Mapped[list['Client']] = relationship(secondary='rent', back_populates='product')
