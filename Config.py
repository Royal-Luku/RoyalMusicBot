import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "13708534"))
    API_HASH = os.environ.get("API_HASH", "51b384fee3c86840ee2ba7938f0beff4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6018772129:AAH2K-WK1nDW1n9IXL_gB6jbgzPl_xUIrcc")
    STRING_SESSION = os.environ.get("STRING_SESSION", " 1BVtsOLYBu5WQvywDoWyg1mRL3p4sTGsAj3GmU67uvdLyC7I2WNYr6BxTZlBYShkRsq-eE8vixRHZOWiesWwc7XZwkq6GEnKEee9CctHwzRvLZ6dHyArubhrQ9aL9vnj4QT3w09gcEilwPypOL5ur-zq-TfN9caPQiasqNbSIbfYSfIV7h91Dt3bekmH959u--cpxtRQurJ5hBHbEtVaydAy2hECeXS9PVDL6T3-2g_1yu7EyfhexSaRZ_yTuVwy3-dZlAn3qkbid-8X2pucZEp7Xzsju87v9oOCDwm1q_UyesY83YcpxpxVASQ_y_VbQzkBnSmy4Lb7X32sbU7mc6Gwy_y85xYg=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", True)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "RoyalMusicRobot")
    SUPPORT = os.environ.get("SUPPORT", "Royaldwip") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Wombackup") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5196437706")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "10800")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
