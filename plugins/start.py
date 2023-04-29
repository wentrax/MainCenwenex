# @alex0980
from script import Script 
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
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
                        InlineKeyboardButton("Help", callback_data="helpbutton_data"),  
                        InlineKeyboardButton("About", callback_data="about_data")
                    ],[                    
                        InlineKeyboardButton(
                            "Developer", url="https://t.me/Lx0980AI")
                    ]
                ]
            )
      )


 
@Cenwenex.on_callback_query()
async def button(bot, cmd: CallbackQuery):
    cb_data = cmd.data
    if "helpbutton_data" in cb_data:
        await cmd.message.edit(
             text = "Help: <b>Buttons</b>",
             parse_mode = enums.ParseMode.MARKDOWN, 
             disable_web_page_preview=True, 
             reply_markup=InlineKeyboardMarkup(
                 [
                     [
                      InlineKeyboardButton("Auto Filter", callback_data="autofilter_data"),
                      InlineKeyboardButton("Media Clone", callback_data="mediaclone_data")
                     ],[
                      InlineKeyboardButton("Developer", url="https://t.me/Lx0980AI")
                     ],[
                      InlineKeyboardButton("⬇️ Back", callback_data="start_data"),
                      InlineKeyboardButton("🔐 Close", callback_data="close_data")
                     ]
 
                 ] 
             ) 
        )
    elif "mediaclone_data" in cb_data:
          await cmd.message.edit(
               text=Script.MEDIACLONE_TXT,
               parse_mode = enums.ParseMode.HTML, 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                       [                                             
                        InlineKeyboardButton("⬇️ Back", callback_data="helpbutton_data"),
                        InlineKeyboardButton("🔐 Close", callback_data="close_data")                                               InlineKeyboardButton("Auto Filter", url="https://t.me/Lx0980AI")
                       ] 
                   ] 
               ) 
          )
    elif "autofilter_data" in cb_data:
          await cmd.message.edit(
               text=Script.AUTOFILTER_TXT,
               parse_mode = enums.ParseMode.MARKDOWN, 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [                      
                       [
                        InlineKeyboardButton("⬇️ Back", callback_data="helpbutton_data"),
                        InlineKeyboardButton("🔐 Close", callback_data="close_data")
                       ]
                   ]
               )
          )
    elif "about_data" in cb_data:
          await cmd.message.edit(
               text=Script.ABOUT_TXT,
               parse_mode = enums.ParseMode.MARKDOWN, 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [                      
                       [
                        InlineKeyboardButton("⬇️ Back", callback_data="start_data"),
                        InlineKeyboardButton("🔐 Close", callback_data="close_data")
                       ]
                   ]
               )
          )

    elif "start_data" in cb_data:
          await cmd.message.edit(
               text=Script.START_TXT.format(cmd.from_user.first_name), 
               parse_mode = enums.ParseMode.MARKDOWN, 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                      
                       [
                        InlineKeyboardButton("Help", callback_data="helpbutton_data"),
                        InlineKeyboardButton("About", callback_data="about_data")
                       ],[
                        InlineKeyboardButton("Developer", url="https://t.me/Lx0980AI")                                               
                       ]
                   ]
               )
          )
    elif "close_data" in cb_data:
          await cmd.message.delete()
          await cmd.message.reply_to_message.delete()
