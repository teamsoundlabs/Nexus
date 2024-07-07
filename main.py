# Guilded imports
import guilded
from guilded.ext import commands

# Database imports
from beanie import init_beanie
from documents import __all__, Server
from motor.motor_asyncio import AsyncIOMotorClient

# Utility imports
from yaml import safe_load

# Pull config
with open("config.yaml" or "config.yml", "r") as f:
    config = safe_load(f)

# Initialize clients
motor = AsyncIOMotorClient(config["database"]["uri"])
bot = commands.Bot()
