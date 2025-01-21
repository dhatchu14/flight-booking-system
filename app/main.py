from fastapi import FastAPI
from api.routes import router  # Import the combined routes

app = FastAPI()

# Include all the routes in the app
app.include_router(router, prefix="/api", tags=["Library Management"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Library Management System API"}
