import os
import logging

class InfoMTN:    
    API_ID = 17571849
    API_HASH = "fd96389b0d258e9adfbd52219582064a"
    BOT_TOKEN = "5672381870:AAHD0oGNxsBT_DAoa64calR7IjVQcl-t2u4"
    BOT_SESSION = "bot"     
    FROM_CHANNEL = -1001667023505 # channel username 
    TO_CHANNEL = -1001820965189 # your channel id
    OWNER_ID = "1903280447"
    FILTERCHANNEL_ID = -1001820965189
    SESSION = "AgAhksdbWyZWg0c7gJrBQCdr_pv40Kr11hG82925DPQQ4sso9H4nQDTWbnIsxDaf_kFuK3VULwLjOPL7h-dF5abqNLSii1vFB-O8izutF7VIg6HAc77no2HrHRQDj5V9IWFND6_gTJndGS4nagfJWTM_9ixHh8O3i0bKs2QBj3r9iMe7jOv3TUaRfA-sdowvPckdyGLTbchbWReJHfI7EQW1jgGi4Xzfx9vwsPkF8yOkUhqFpZywfLfwpxhishz51ykc_y9nDrkPP2QmQ45CgtdDhEl-nt5n3xOapdfgDl1n9qKXUbiQtzbKtUGCgrlJhIeFIpxVHsf9Z1dnOS_FdajvAAAAATPH6AEA"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
