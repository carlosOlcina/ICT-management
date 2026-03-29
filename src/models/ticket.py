import uuid

from ..extensions import db

class Ticket(db):
  __tablename__ = 'tickets'

  id = db.Column(
    db.String(36),
    primary_key=True,
    default=lambda: str(uuid.uuid4())
  )

  name = db.Column(
    db.String(80),
    nullable=False
  )

  description = db.Column(
    db.Text,
    nullable=False
  )

  company_id = db.Column(
    db.String(36),
    db.ForeignKey('companies.id'),
    nullable=False
  )

  solvet_at = db.Column(
    db.DateTime,
    nullable=True
  )

  solved_by = db.Column(
    db.String(36),
    db.ForeignKey('users.id'),
  )

  software_id = db.Column(
    db.String(36),
    db.ForeignKey('softwares.id'),
    nullable=True
  )

  equipment_id = db.Column(
    db.String(36),
    db.ForeignKey('equipments.id'),
  )

  users_id = db.Column(
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

