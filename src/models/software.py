import uuid
from ..extensions import db

class Software(db.Model):
  __tablename__ = 'softwares'

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
    nullable=True
  )

  url = db.Column(
    db.String(200),
    nullable=True
  )

  pricing = db.Column(
    db.Float,
    default=0.0,
  )

  renew_date = db.Column(
    db.DateTime,
    nullable=True
  )

  company_id = db.Column(
    db.String(36),
    db.ForeignKey('companies.id'),
    nullable=False
  )

  support_contact = db.Column(
    db.String(80),
    nullable=True
  )

  equipment_id = db.Column(
    db.String(36),
    db.ForeignKey('equipments.id'),
    nullable=False
  )

  users_id = db.Column(
    db.String(36),
    db.ForeignKey('users.id'),
    nullable=True
  )
