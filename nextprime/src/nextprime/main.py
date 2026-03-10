from fastapi import FastAPI , Request , Response , Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path


BASE_DIR= Path(__file__).resolve().parent
app = FastAPI()

templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))
app.mount("/static" , StaticFiles(directory=str(BASE_DIR/"static")) , name="static")


@app.get("/" , response_class=HTMLResponse)
def Home(request : Request):
    return templates.TemplateResponse(
        "index.html" , 
        {"request" : request}
    )


def isPrime(n):
    if n < 2:
        return "need bigger than 2"
    
    for i in range(2 , int(n ** 0.5) + 1):
        if n%i == 0:
            return False
    return True
    
def getNextPrime(number , limit):
    primeList = []
    count = 0
    while count < limit:
        if isPrime(number):
            primeList.append(number)
            count+= 1
        number+=1

    return primeList



@app.post("/calc" , response_class=HTMLResponse)
def getPrime(request: Request , number_input : int = Form() , limit_input :int = Form()):
    result = getNextPrime(number=number_input , limit=limit_input)
    return templates.TemplateResponse(
        "index.html" , 
        {"request" : request ,
         "prime_numbers" : result
         }
    )


@app.get("/about" , response_class=HTMLResponse)
def Home(request : Request):
    return templates.TemplateResponse(
        "about.html" , 
        {"request" : request}
    )