from info import InfoMTN, LOGGER
from pyrogram import Client, __version__

class User(Client):
    def __init__(self):
        super().__init__(
            "botClient",
            api_hash=InfoMTN.API_HASH,
            api_id=InfoMTN.API_ID,
            session_string=InfoMTN.SESSION,
            workers=20
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
