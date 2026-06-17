from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from presentation.student_routes import router
from presentation.auth_routes import router as auth_router
from infrastructure.connection import engine
from infrastructure.connection import Base

Base.metadata.create_all(engine)

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)
app.include_router(auth_router)