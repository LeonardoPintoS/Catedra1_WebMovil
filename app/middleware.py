from fastapi import Request
import time
import logging

logger = logging.getLogger("uvicorn.info")

async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"Ruta: {request.url.path} | Tiempo de proceso: {process_time:.4f}s")
    return response