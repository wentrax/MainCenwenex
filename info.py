
import os
import logging

class InfoMTN:    
    API_ID = 16448144
    API_HASH = "1073665850700150caf0e0cbb68216a2"
    BOT_TOKEN = "6032335088:AAHqrUvqR-0rulRNNiesZ-B02iwcSHYSTy8"
    BOT_SESSION = "bot"     
    FROM_CHANNEL = -1001667023505 # channel username 
    TO_CHANNEL = -1001820965189 # your channel id
    OWNER_ID = "1903280447"
    FILTERCHANNEL_ID = -1001820965189
    SESSION = 

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
