# import tokenizer and class
from typing import Any
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration


# download and install the model
model_name = "facebook/blenderbot-400M-distill"
tokenizer: Any = BlenderbotTokenizer.from_pretrained(model_name)
model: tuple = BlenderbotForConditionalGeneration.from_pretrained(model_name)


async def get_bot_answer(input: str) -> Any:
    # utterance is the input that the chatbot take
    UTTERANCE = input
    # tokenize the utterance(user input)
    inputs = tokenizer([UTTERANCE], return_tensors="pt")  # pt is pytorch tensors
    # passing in the inputs and getting the output of the chatbot
    results: Any = model.generate(**inputs)
    # decoding the results
    answer_txt = tokenizer.batch_decode(results)
    return answer_txt[0]
