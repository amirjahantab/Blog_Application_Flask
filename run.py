from blog import app, db
from blog.models import User, Post


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)