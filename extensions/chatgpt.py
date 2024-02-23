from openai import OpenAI
import lightbulb
import hikari
from env import *

plugin = lightbulb.Plugin("chatgpt")


def load(bot):
    bot.add_plugin(plugin)

    global client
    client = OpenAI(
        # This is the default and can be omitted
        api_key=CHATGPT_TOKEN,
    )


def chatgpt_response(prompt):

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Reply to the following prompt with UwU speak and typing :3 in between words rarely: "
                + prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion.choices[0].message.content


@plugin.listener(hikari.MessageCreateEvent)
async def reply(event: lightbulb.events) -> None:
    if not event.is_human or event.message.content is None:
        return
    if BOT_ID in event.message.user_mentions_ids:
        message = event.message.content

        message = message.replace("<@" + str(BOT_ID) + ">", "")

        await event.message.respond(chatgpt_response(message))
