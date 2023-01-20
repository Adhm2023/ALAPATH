from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "20543992"))
API_HASH = getenv("API_HASH", "93fb093637866a6a054c54ade94a7eff")
BOT_TOKEN = getenv("BOT_TOKEN", "5555731081:AAHASdvJZNBOMxTfmNByhq-9tyQZvsgKxZU")
SESSION_NAME = getenv("SESSION_NAME", "BACax2utFvvCLXcdj9EzyJuJNrW37GT-v0IQ5Uw7OvTMK9R7a1BZ2sGu1xkfzGPYuOdDbPE6kNCSI_RRUTkj2Z9YF_AZAa-ij8YwGhuHxI4geuJNgsjTQm4Ylp-tnB7N5VgzhY5VNFKOPu3dEic15_Yetjel3_IW7p_1pEx_vdcLizIffphAxNlcVj7cFPNoSdIhdVdAArq-K9b9vu_iugR6xmlxl9Z4OVEY4xvivam2LDT3UCKNkcYfeAsFoH8ALjxyh1nYY4ELwPaQ4WI63qaaE1A8GObgy_vV9MftkVSy3oSb1F4yHt-HShBY6PPolG0ponmFx1fQgeI4BFMDgEsgAAAAAWPfkSEA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "ALAPATH")
ALIVE_NAME = getenv("ALIVE_NAME", "ALAPATH")
BOT_USERNAME = getenv("BOT_USERNAME", "CASBAR_1BoT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ioewoi")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "I_R_S_A_I")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5093806483").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5093806483").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
