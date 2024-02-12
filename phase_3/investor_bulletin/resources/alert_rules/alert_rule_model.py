""" Alert Rule Model """
from uuid import UUID
from db.models.model_base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class AlertRule(Base):
    __tablename__ = "alert-rules"
    """
    This is the primary key, I prefered to use the Integer as the primary key: because Integer keys are generally more performant. They take up less space (4 bytes for an integer vs 16 bytes for a UUID)

    In our case: Integer as the primary key is a good choice if I do not need the global uniqueness of UUIDs, and I want to take advantage of auto-incrementing and better performance.
    """

    id = Column(Integer, primary_key=True)
    name = Column(String)
    threshold_price = Column(Float)
    symbol = Column(String, ForeignKey('alerts.symbol'))

    alert = relationship('Alerts', back_populates='rule_alerts')
