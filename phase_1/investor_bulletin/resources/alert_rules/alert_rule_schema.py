""" Alert Rule Schema """
"""_summary_
This file to abstract any validation logic for the Alert Rules
"""
from pydantic import BaseModel
from typing import Optional

class AlertRuleCreate(BaseModel):
    name: str
    threshold_price: float
    symbol: str

class AlertRuleUpdate(BaseModel):
    name: Optional[str] = ""
    threshold_price: Optional[float] = 0.0
    symbol: Optional[str] = ""
