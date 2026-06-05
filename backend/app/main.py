from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.incidents import router as incident_router
from backend.app.api.monitoring import router as monitoring_router
from backend.app.core.config import settings
from backend.app.core.init_db import init_db
import asyncio

from backend.app.monitoring.scheduler import MonitoringScheduler
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="AI-Powered Autonomous Self-Healing Platform",
    version=settings.PROJECT_VERSION
)
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(
        MonitoringScheduler.start()
    )
# Initialize Database
init_db()

# ADD THIS LINE HERE
app.include_router(incident_router)
app.include_router(monitoring_router)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": f"{settings.PROJECT_NAME} Backend Running Successfully"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION
    }