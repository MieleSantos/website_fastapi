from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request, usuario: str = "Felicity JOnes"):
    context = {"request": request, "usuario": usuario}

    return templates.TemplateResponse("index.html", context=context)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:app", host="0.0.0.0", reload=True, port=8000, log_level="info"
    )
