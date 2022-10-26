from fastapi import APIRouter, HTTPException , Depends
from fastapi.responses import JSONResponse , RedirectResponse
from services import shortUrlService
from sqlalchemy.orm import Session
from schemas import LongUrlInput
from config.dependency import get_db


router = APIRouter(
    # prefix="/",
    tags=["shortUrl"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{encoded_str}")
async def open_shortUrl(encoded_str: str):
    try:
        res = await shortUrlService.open_shortUrl(encoded_str)
        return RedirectResponse(res)
  
    
    except Exception as ex:
        raise HTTPException(status_code=418, detail=ex)

@router.post("/create-shortUrl")
async def create_shortUrl(body: LongUrlInput , db: Session = Depends(get_db)):
    try:
        res = await shortUrlService.create_shortUrl(body.longUrl , db)
        if res:
            return JSONResponse(
            status_code=200,
            content={"status_code": "200" , "message": "success" , "data": res})

    except Exception as ex:
        raise HTTPException(status_code=418, detail=ex)
