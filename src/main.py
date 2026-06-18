"""
Main FastAPI application.
Learning: Python, FastAPI, async programming
Author: Sebastian
"""

from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI(
    title="Item Comparison API v2",
    description="Learning FastAPI with real projects",
    version="0.1.0"
)


# Test endpoint
@app.get("/")
async def root():
    """Root endpoint - health check"""
    return {"message": "API is running", "status": "healthy"}


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)