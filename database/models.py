from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True)
    email = Column(String(150), unique=True)
    password = Column(String(150))
    date_created = Column(DateTime, default=func.now())

    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password

class BlogEntry(Base):
    __tablename__ = 'blogentries'
    id = Column(Integer, primary_key=True)
    date_created = Column(DateTime, default=func.now())
    title = Column(String(150), unique=True)
    entry_text = Column(String(10000))
    author = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=True)

    def __init__(self, title=title, entry_text=None, author=None):
        self.title = title
        self.entry_text = entry_text
        self.author = author
