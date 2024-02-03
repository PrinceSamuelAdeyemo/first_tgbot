import asyncio
import telegram


async def main():
    bot = telegram.Bot("6810770272:AAF2nwzDOgKwmIYI6uHBFkFLKdZyX1kYphA")
    async with bot:
        #print(await bot.get_me())
        updates = (await bot.get_updates())
        for i in range(len(updates)):
            print(updates[i], end="\n"*4)
            await bot.send_message(text="Received your message", chat_id = updates[i].message.from_user.id, reply_to_message_id=5)
            print("ID",updates[i].message.id)
            print("message id",updates[i].message.message_id)
        #print(updates, end="\n")
        #user_first_name = updates.message.from_user.first_name
        #user_id = updates.message.from_user.id
        #await bot.send_message(text=f"Hello, {user_first_name}", chat_id = user_id)
        


if __name__ == '__main__':
    asyncio.run(main())