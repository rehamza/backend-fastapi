from config.database import SessionLocal
from datetime import date
from utils.UrlShortner import UrlShortner 
from fastapi import HTTPException
from config.config import Settings
from models import ShortUrl
from sqlalchemy.orm.attributes import flag_modified

setting = Settings()

async def get_by_id(id: int):
   db = SessionLocal()
   res = db.query(ShortUrl).filter(ShortUrl.id == id).first()
   return res

async def get_by_shorturl_encoded(short_encoded: str):
    db = SessionLocal()
    res = db.query(ShortUrl).filter(ShortUrl.short_encoded == short_encoded).first()
    return res

   

async def get_by_longurl(long_url: str):
   db = SessionLocal()
   res = db.query(ShortUrl).filter(ShortUrl.long_url == long_url).first()
   return res

async def create(longUrl: str , db):
     shortUrl = ShortUrl()
     shortUrl.long_url = longUrl
     db.add(shortUrl)
     db.commit()
     db.refresh(shortUrl)
     return shortUrl

async def update(longUrl , db):
     flag_modified(longUrl , 'short_encoded')
     db.add(longUrl)
     db.commit()
     db.refresh(longUrl)
     return longUrl


async def create_shortUrl(longUrl , db):

  short_url = await get_by_longurl(longUrl)
  d1 = date.today()
  if (short_url):
    if (short_url.id) or (d1 <  short_url.expiry_date):
      return "{}:{}/{}".format(setting.HOST ,setting.PORT , short_url.short_encoded)

  shorl_url_data = await create(longUrl , db)

  urlShortner = UrlShortner()
  encode_url = urlShortner.encode(shorl_url_data.id)
  shorl_url_data.short_encoded = encode_url
  update_data = await update(shorl_url_data , db)
  return "{}:{}/{}".format(setting.HOST ,setting.PORT , update_data.short_encoded)

async def open_shortUrl(encoded_str: str):
  if encoded_str != "favicon.ico":
    short_url = await get_by_shorturl_encoded(encoded_str)
    d1 = date.today()
    if (d1 <  short_url.expiry_date):
      return short_url.long_url
    else:
      return "url expire"


