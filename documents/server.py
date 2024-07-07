# Type imports
from beanie import Document


# Create server document
class Server(Document):
    """

    Args:
        serverId (str): The server's corresponding Guilded ID
        prefix (str): The server's prefix
    """

    serverId: str

    prefix: str
