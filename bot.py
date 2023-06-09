
from pyrogram import Client, enums, __version__
from info import InfoMTN, LOGGER
from CLIENT import User

class Bot(Client):
#    USER: User = None
#    USER_ID: int = None

    def __init__(self):
        super().__init__(
            "filebot",
            api_hash=InfoMTN.API_HASH,
            api_id=InfoMTN.API_ID,
            plugins={
                "root": "plugins"
            },
            workers=200,
            bot_token=InfoMTN.BOT_TOKEN            
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        bot_details = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{bot_details.username}  started! "
        )
#        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")



