import os

class Config:
    UPLOAD_FOLDER = os.path.join("app", "uploads")
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB limit
    ALLOWED_EXTENSIONS = {"pdf", "docx"}