from sqlalchemy import String, Text, Integer, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from database import Base
from datetime import datetime


class Rent(Base):
    __tablename__ = 'rent'
    id = mapped_column(Integer, primary_key=True)
    client_id = mapped_column(Integer, ForeignKey('client.id'))
    product_id = mapped_column(Integer, ForeignKey('product.id'))
    duration = mapped_column(Integer, nullable=False)
    date = mapped_column(DateTime, default=datetime.now())


class Client(Base):
    __tablename__ = 'client'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), nullable=False)
    date_registration = mapped_column(DateTime, default=datetime.now())
    phone = mapped_column(String(20))

    product = relationship('Product', secondary='rent', back_populates='client')


class ProductType(Base):
    __tablename__ = 'product_type'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), nullable=False)

    product = relationship('Product', back_populates='type')


class Product(Base):
    __tablename__ = 'product'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), nullable=False)
    type_id = mapped_column(Integer, ForeignKey('product_type.id'))
    description = mapped_column(Text)

    type = relationship('ProductType', back_populates='product')
    client = relationship('Client', secondary='rent', back_populates='product')
