""" Alert Model """
from db.models.model_base import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Alerts(Base):
    __tablename__ = 'alerts'

    symbol = Column(String, primary_key=True)
    rule_alerts = relationship('AlertRule', back_populates='alert')
