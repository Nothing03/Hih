import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
if os.path.exists("Internal"):
    load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
admins = {}
que = {}

API_ID = int(getenv("API_ID", "26762870"))
API_HASH = getenv("API_HASH", "34a77673138edb133ff15f4ad075708c")
BOT_TOKEN = getenv("BOT_TOKEN", "6070135717:AAFl9wqj9BZqdhavxUsjgZvvhrBX3RKsoEU")
STRING_SESSION = getenv("STRING_SESSION", "BQBXDotLVem6oRg_r11PFz5POs9YFhgrPUPeVdu2wjZe58BI2Eq7G8nT1ZrtSDW6uXHdXpJWeToog1SwEDwznbDkcRMymISNAKqgfenciyqFieiWmHheEygLF1wZz8soKP0TwDtZsCK4Z5dx5gJQYeNdi8L_F4xGByhl337tCEKFwDMYeIY9GqJ39ddhXwca5UQnTEKJv9llCDx4L1xmPmcARltBBSNXXHATQP7vez2E3CADJbDkSwYhb6V4qchIDjyk5rm0ZLvX6zhM6M9iJdR8uHD_Y-8Sk5sijBpXR7LJe8vAOhpe1hOlXuL4E5ZGt5sn68S5jBCmMkA-dur_zIlPAAAAAWjUa8oA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split())
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://jinkun:raizel9783@cluster0.yyayi.mongodb.net/myfirstdatabase?retrywrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6053718986").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001942569130"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6053718986").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Nothing03/Hih")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "aditya")
