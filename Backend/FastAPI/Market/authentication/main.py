from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn

from authentication.routes import GET, POST

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(GET.router)
app.include_router(POST.router)