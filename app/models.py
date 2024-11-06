from app import db


class Driver(db.Model):
    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    apartment_suite = db.Column(db.String(50))
    city = db.Column(db.String(100), nullable=False)
    state_province = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(5), nullable=False)
    license_number = db.Column(db.String(50), nullable=False)
    state_of_issuance = db.Column(db.String(50), nullable=False)
    license_class = db.Column(db.String(20), nullable=False)
    license_expiry = db.Column(db.Date, nullable=False)
    availability = db.Column(db.String(255), nullable=False)
    location_preference = db.Column(db.String(100))
    experience = db.Column(db.String(255), nullable=False)
    military_active = db.Column(db.Boolean, default=False)
    military_retired = db.Column(db.Boolean, default=False)
    military_branch = db.Column(db.String(100))
    law_enforcement_active = db.Column(db.Boolean, default=False)
    law_enforcement_retired = db.Column(db.Boolean, default=False)
    law_enforcement_location = db.Column(db.String(100))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
