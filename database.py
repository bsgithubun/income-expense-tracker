import os

from deta import Deta
from dotenv import load_dotenv

# Load the enfironment variables
load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")

# Load the data
data = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.csv')

# Load the detail variables
detail = Deta(data)

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("monthly_reports")


def insert_period(period, incomes, expenses, comment):
    """Returns the report on a successful create, otherwise raises an error"""
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})

def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items

def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)
