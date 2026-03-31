import uuid
from ..extensions import db

class Equipment(db.Model):
  __tablename__ = 'equipments'

  id = db.Column(
    db.String(36),
    primary_key=True,
    default=lambda: str(uuid.uuid4())
  )

  name = db.Column(
    db.String(120),
    nullable=False
  )

  ip = db.Column(
    db.String(15),
    nullable=False
  )

  mac = db.Column(
    db.String(17),
    nullable=False
  )

  type = db.Column(
    db.Enum(
      'laptop',
      'desktop',
      'server',
      'tablet',
      'smartphone',
      'printer',
      'camera',
      'other'
    ),
    nullable=False
  )

  company_id = db.Column(
    db.String(36),
    db.ForeignKey('companies.id'),
    nullable=False
  )

  state = db.Column(
    db.Enum('active', 'inactive', 'maintenance'),
    nullable=False,
    default='active'
  )

  priority = db.Column(
    db.Integer,
    nullable=False,
    default=1
  )
