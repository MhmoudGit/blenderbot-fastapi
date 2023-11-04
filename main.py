from fastapi import FastAPI, Form
from ai import get_bot_answer  # importing ai blenderbot
from bot import route


app = FastAPI()


@app.post("/chat")
async def talk(text: str = Form(...)):
    answer = get_bot_answer(text)
    return answer


app.include_router(route.router)

# main function
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
