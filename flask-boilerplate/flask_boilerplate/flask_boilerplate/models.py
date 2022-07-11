from flask_boilerplate import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id): # load user to login
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	# uuid = db.Column(db.String, unique=True, nullable=False)
	username = db.Column(db.String(18), unique=True, nullable=False)
	email = db.Column(db.String(60), unique=True, nullable=False)
	# image_file = db.Column(db.String(20), unique=False, nullable=False, default='default.jpg')
	password = db.Column(db.String(30), nullable=False)
	has_website = db.Column(db.String(6), nullable=True)
	wb_data = db.relationship('Website_data', backref='author', lazy=True)


	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.password}')"
