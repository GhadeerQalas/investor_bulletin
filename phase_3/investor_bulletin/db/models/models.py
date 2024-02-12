from db.models.model_base import Base
from sqlalchemy import create_engine
from resources.alerts.alert_model import Alerts
from resources.alert_rules.alert_rule_model import AlertRule
import os
from dotenv import load_dotenv
import urllib.parse as urlparse
from sqlalchemy.orm import sessionmaker

# Load the .env file
load_dotenv()

# Parse the original DATABASE_URL
url = urlparse.urlparse(os.environ["DATABASE_URL"])

# Change the query parameter for sslmode
query = dict(urlparse.parse_qsl(url.query))
query.update({'sslmode': 'require'})

# Construct the new DATABASE_URL
new_url = urlparse.urlunparse(
    (url.scheme, url.netloc, url.path, url.params, urlparse.urlencode(query), url.fragment)
)

engine = create_engine(new_url)

Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
