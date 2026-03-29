import uuid
from extensions import db

class Company(db.Model):
  __tablename__ = 'companies'

  id = db.Column(
    db.String(36),
    primary_key=True,
    default=lambda: str(uuid.uuid4())
  )

  name = db.Column(
    db.String(120),
    nullable=False
  )

  description = db.Column(
    db.Text,
    nullable=False
  )

  owner_id = db.Column(
    db.String(36),
    db.ForeignKey('users.id'),
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