from database.db import db 
from datetime import datetime 
import uuid 
 
class Member(db.Model): 
    __tablename__ = 'members' 
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4())) 
    first_name = db.Column(db.String(100)) 
    last_name = db.Column(db.String(100)) 
    email = db.Column(db.String(100)) 
 
    def full_name(self): 
        return f"{self.first_name} {self.last_name}" 
