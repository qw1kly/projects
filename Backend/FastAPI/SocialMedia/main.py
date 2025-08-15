from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn

from routes import GET, POST, DELETE


app = FastAPI()


app.include_router(GET.router)
app.include_router(POST.router)
app.include_router(DELETE.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["*"]
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")