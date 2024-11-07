from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Keepmesafe90@pre-reg.cluc8o6wyyjf.us-west-1.rds.amazonaws.com:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/driver_registration', methods=['GET', 'POST'])
def driver_registration():
    if request.method == 'POST':
        driver = Driver(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            phone=request.form['phone'],
            email=request.form['email'],
            address=request.form['address'],
            apartment_suite=request.form.get('apartment_suite'),
            city=request.form['city'],
            state_province=request.form['state_province'],
            zip_code=request.form['zip_code'],
            license_number=request.form['license_number'],
            state_of_issuance=request.form['state_of_issuance'],
            license_class=request.form['license_class'],
            license_expiry=request.form['license_expiry'],
            availability=request.form['availability'],
            location_preference=request.form.get('location_preference'),
            experience=request.form['experience'],
            military_active='military_active' in request.form,
            military_retired='military_retired' in request.form,
            military_branch=request.form.get('military_branch'),
            law_enforcement_active='law_enforcement_active' in request.form,
            law_enforcement_retired='law_enforcement_retired' in request.form,
            law_enforcement_location=request.form.get(
                'law_enforcement_location')
        )

        # driver to session and commit to database
        db.session.add(driver)
        try:
            db.session.commit()
            print("Driver added successfully, redirecting to thank_you page.")
            return redirect(url_for('thank_you'))
        except Exception as e:
            db.session.rollback()
            print(f"Error during database commit: {e}")

    return render_template('driver_registration.html')


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
