import uuid
from extensions import db

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(
    db.String(36),
    primary_key=True,
    default=lambda: str(uuid.uuid4())
  )

  name = db.Column(
    db.String(80),
    nullable=False
  )

  email = db.Column(
    db.String(120),
    unique=True,
    nullable=False
  )

  password = db.Column(
    db.Text,
    nullable=False
  )

  company_id = db.Column(
    db.String(36),
    db.ForeignKey('companies.id'),
    nullable=False
  )

  created_at = db.Column(
    db.DateTime,
    default=db.func.now()
  )

  updated_at = db.Column(
    db.DateTime,
    default=db.func.now(),
    onupdate=db.func.now()
  )

  def __init__(self, name, email, password, company_id):
    self.name = name
    self.email = email
    self.password = password
    self.company_id = company_id

  def __repr__(self):
    return f"<User {self.name}>"