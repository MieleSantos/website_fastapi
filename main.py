from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def index():

    conteudo = """
        <center>
            <h1>FastApi web na  <u>Geek University</u> </h1>
            <spam>Para mais cursos, visite nosso site clicando
            <a href="https://geekuniversity.com.br"
            target="_blank">aqui</a> </spam>
        </center>
    """
    return HTMLResponse(conteudo)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, log_level="info")
