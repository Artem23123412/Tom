from g4f.client import AsyncClient
import asyncio


def get_prompt(text):
    prompt = f"""
    Помоги мне определить, правильный ли фразиологизм я использовал в тексте?
    Если правильно, то просто ответь фразой "Всё верно" и с объяснениями.
    Если неправильно, то максимально коротко опиши что именно неверно.
    Отвечай только на сообщения, которые связаны с фразеологизмами. Если будет что-то другое, то отвечай "На такие вопросы я не могу ответить"
    Вот сам текст: {text}
    """
    return prompt


async def check_phraseological(text):
    client = AsyncClient()
    prompt = get_prompt(text)
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        web_search = False
    )
    return response.choices[0].message.content
