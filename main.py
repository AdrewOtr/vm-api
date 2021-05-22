from fastapi import FastAPI
from schemas import Object


app = FastAPI()


app = FastAPI(title="Virtual Microscope API",
              description="API for thesis by student Andrey Otroshchenko",
              docs_url="/docs", redoc_url=None)


@app.get('/')
def home():
    return {"key": "Hello"}


@app.get('/{pk}')
def get_item(pk: int, q: str = None):
    return {"key": pk, "q": q}


@app.post('/object')
def create_entity(item: Object):
    return item



# if __name__ == '__main__':
