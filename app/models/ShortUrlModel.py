from datetime import date , datetime
from dateutil.relativedelta import relativedelta
from sqlalchemy import  Column , Integer, String, DateTime , DATE

from config.database import Base

class ShortUrl(Base):
    __tablename__ = "shorturl"

    id = Column(Integer, primary_key=True, index=True ,  autoincrement=True)
    long_url = Column(String, unique=True, index=True)
    short_encoded = Column(String, unique=True, index=True)
    expiry_date = Column(DATE, default=date.today() + relativedelta(months=+6))
    created_at = Column(DateTime, default=datetime.utcnow)

