
import os
import logging

class InfoMTN:    
    API_ID = 16448144
    API_HASH = "1073665850700150caf0e0cbb68216a2"
    BOT_TOKEN = "6032335088:AAHqrUvqR-0rulRNNiesZ-B02iwcSHYSTy8"
    BOT_SESSION = "bot"     
    FROM_CHANNEL = "@Databaseforfiles" # channel username 
    TO_CHANNEL = -1001563098453 # your channel id
    OWNER_ID = "1903280447"
    LIMIT = 2
    SKIP_NO = 0
    SESSION = "BQAbcBp7IplE9_BJIw05yKC7WZIoUDTFbnXfDLGyIYFpq76tfLLDtlqcfRyZ3rTBgtRxKrZhvsxh1DVzdhxekQuX73dmodoLM8WapEGu390jUb5vHP4y73RwgbHYFYiilMx_FFa60LHH6K1DGzhlk0dvnVn1X634zHvdpW0nmXYhMwH0nUghqSzgXPIJaE_AVHx2ZzMBv-XVluDZZJJIg2Tr2eCg8SNifCz22WJWGbM3VcGm-7VJt6S4wgoAyntndgJx9jvRvpCuOGBJ1h2YdypVh-KDRwpak_4CHubx1NTvYtDzgDzA4grO0UaO1JWURvBvl5I0zUWe2jC2IeSBgj0qAAAAAWHA4M8A"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
