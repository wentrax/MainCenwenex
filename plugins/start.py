from script import Script 
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot as Cenwenex

@Cenwenex.on_message(filters.command("start") & filters.private)
async def start(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Script.START_TXT.format(cmd.from_user.first_name), 
          reply_to_message_id = cmd.message.id,
          parse_mode = enums.ParseMode.MARKDOWN,
          disable_web_page_preview = True, 
          reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Help", callback_data="help_data"),
                        InlineKeyboardButton("About", callback_data="about_data"),
                    ],[                    
                        InlineKeyboardButton(
                            "Developer", url="https://t.me/Lx0980AI")
                    ]
                ]
            )
      )


 
