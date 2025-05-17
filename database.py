from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/mshiyanepay")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    phone_number = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    credit_score = Column(Float, default=0.0)
    is_business = Column(Boolean, default=False)

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    account_number = Column(String, unique=True)
    balance = Column(Float, default=0.0)
    account_type = Column(String)  # savings, checking, business
    created_at = Column(DateTime, default=datetime.utcnow)
    last_activity = Column(DateTime, default=datetime.utcnow)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    transaction_type = Column(String)  # deposit, withdrawal, transfer
    amount = Column(Float)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String)  # pending, completed, failed
    fraud_score = Column(Float, default=0.0)

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    interest_rate = Column(Float)
    term_months = Column(Integer)
    status = Column(String)  # pending, approved, rejected, active, paid
    created_at = Column(DateTime, default=datetime.utcnow)
    last_payment_date = Column(DateTime)
    next_payment_date = Column(DateTime)
    credit_score_at_application = Column(Float)

class BusinessProfile(Base):
    __tablename__ = "business_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    business_name = Column(String)
    business_type = Column(String)
    registration_number = Column(String)
    annual_revenue = Column(Float)
    years_in_operation = Column(Float)
    industry = Column(String)
    risk_score = Column(Float, default=0.0)

# Create all tables
Base.metadata.create_all(bind=engine)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 