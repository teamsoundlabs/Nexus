# Type imports
from beanie import Document

# Import all your Beanie ODM documents here
from .server import Server

__all__: list[Document] = [
    Server
]  # Make sure to put all of your imported **documents** in this list or they may not be initialized.
