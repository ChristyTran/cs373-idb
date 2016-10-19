from flask import Flask, send_file
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/musicdb'

db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def index():
    return send_file('index.html')


class Artists(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.String(22), primary_key=True)
    name = db.Column(db.String)
    genres = db.Column(db.String)
    url = db.Column(db.String)
    followers = db.Column(db.Integer(22))
    popularity = db.Column(db.Integer(3))
    image_url = db.Column(db.String)

    def __repr__(self):
        return 'Artists %r' % self.title


class Albums(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.String(22), primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    main_artists = db.Column(db.String)
    main_artists_id = db.Column(db.String(22))
    all_artists = db.Column(db.String)
    type = db.Column(db.String)
    image_url = db.Column(db.String)
    
    def __repr__(self):
        return 'Albums %r' % self.title

class Tracks(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.String(22), primary_key=True)
    name = db.Column(db.String)
    main_artists_id = db.Column(db.String(22))
    all_artists = db.Column(db.String)
    track_no = db.Column(db.Integer)
    album_id = db.Column(db.String)
    duration = db.Column(db.String)
    explicit = db.Column(db.Boolean)
    popularity = db.Column(db.Integer(3))
    preview_url = db.Column(db.String)
    direct_url = db.Column(db.String)
    image_url = db.Column(db.String)
    
    def __repr__(self):
        return 'Tracks %r' % self.title



    

if __name__ == "__main__":
    app.run()
