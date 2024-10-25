from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Rule(Base):
    __tablename__ = 'rules'
    id = Column(Integer, primary_key=True)
    rule_string = Column(String)
    ast = Column(JSON)

# SQLite for demo purposes, can be replaced with PostgreSQL or MySQL
engine = create_engine('sqlite:///rules.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def save_rule(rule_string, ast):
    rule = Rule(rule_string=rule_string, ast=ast.__dict__)
    session.add(rule)
    session.commit()

def get_rule_by_id(rule_id):
    rule = session.query(Rule).filter_by(id=rule_id).first()
    if rule:
        return rule.ast
    return None
