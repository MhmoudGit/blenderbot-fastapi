from fastapi import FastAPI, Form
from ai import get_bot_answer  # importing ai blenderbot


app = FastAPI()


@app.post("/chat")
async def talk(text: str = Form(...)):
    answer = await get_bot_answer(text)
    return answer


# main function
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
