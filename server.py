from fastapi import FastAPI
import uvicorn
from routes.users import router as users_router


app = FastAPI()


app.include_router(users_router)



if __name__ == "__main__":

    @app.get("/")
    async def root():
        return {"message": "Hello World23"}

    uvicorn.run(app, host="0.0.0.0", port=9110)
