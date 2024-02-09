""" Alert Rule Service"""
"""_summary_
this file to write any business logic for the Alert Rules
"""
from resources.alert_rules.alert_rule_schema import AlertRuleCreate
from resources.alert_rules.alert_rule_dal import create_alert_rule, update_alert_rule, delete_alert_rule, get_all_alert_rule

def create_new_rule( rule: AlertRuleCreate, session ):
    return create_alert_rule(rule=rule, session=session)

def update_rule(rule_id: int, rule: AlertRuleCreate, session ):
    return update_alert_rule(rule_id=rule_id, rule=rule, session=session)

def delete_rule(rule_id: int, session):
    return delete_alert_rule(rule_id=rule_id, session=session)

def get_all_rule(session):
    return get_all_alert_rule(session=session)
