""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from resources.alert_rules.alert_rule_schema import AlertRuleCreate
from resources.alert_rules.alert_rule_model import AlertRule

"""
Purspose: Create a new alert rule
@param rule: AlertRuleCreate
@param session: Session
@return: AlertRule
"""
def create_alert_rule(rule: AlertRuleCreate, session):
     new_rule = AlertRule(name=rule.name, threshold_price=rule.threshold_price, symbol=rule.symbol)

     # Add the new alert rule to the session
     session.add(new_rule)

     # Commit the session to save the alert rule to the database
     session.commit()

     # Return the new alert rule
     return new_rule

"""
Purpose: Update an existing alert rule
@param rule_id: int
@param rule: AlertRuleCreate
@param session: Session
@return: AlertRule
"""
def update_alert_rule(rule_id: int, rule: AlertRuleCreate, session):
     # Fetch the existing alert rule from the database
     update_rule = session.query(AlertRule).get(rule_id)

     if update_rule is None:
        raise ValueError("AlertRule with id {} not found".format(rule_id))

     # Update the alert rule's attributes
     if rule.name:
          update_rule.name = rule.name
     if rule.threshold_price:
          update_rule.threshold_price = rule.threshold_price
     if rule.symbol:
          update_rule.symbol = rule.symbol

     # Commit the session to save the changes to the database
     session.commit()

     # Return the updated alert rule
     return update_rule

"""
Purpose: Delete an existing alert rule
@param rule_id: int
@param session: Session
@return: None
"""
def delete_alert_rule(rule_id: int, session):
    # Fetch the existing alert rule from the database
    rule_to_delete = session.query(AlertRule).get(rule_id)

    if rule_to_delete is None:
        raise ValueError("AlertRule with id {} not found".format(rule_id))

    # Delete the alert rule
    session.delete(rule_to_delete)

    # Commit the session to save the changes to the database
    session.commit()

"""
Purpose: Get all alert rules
@param session: Session
@return: List[AlertRule]
"""
def get_all_alert_rule(session):
    return session.query(AlertRule).all()
