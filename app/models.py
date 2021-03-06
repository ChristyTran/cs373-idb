#!user/bin/env python3
"""
Models.py file that contains all of the 
database models.
"""
from loader import db
from flask_sqlalchemy import SQLAlchemy, BaseQuery
import re
# -------------------
# @Artists
# -------------------
class Artist(db.Model):
    """    
    Model for Artists Database
    """
    __tablename__ = 'artists'
    id = db.Column(db.String(22), primary_key=True)
    name = db.Column(db.String)
    genres = db.Column(db.String)
    url = db.Column(db.String)
    followers = db.Column(db.Integer)
    popularity = db.Column(db.Integer)
    image_url = db.Column(db.String)

    def to_json(self): 
        json_artist = {
            'id' : self.id,
            'name' : self.name,
            'genres' : self.genres,
            'url' : self.url,
            'followers' : self.followers,
            'popularity' : self.popularity,
            'image_url' : self.image_url
        }
        return json_artist
    def to_list(self):
        genres = str(self.genres)
        genres = genres.replace('{', '')
        genres = genres.replace('}', '')
        genres = genres.replace('\"', '')
        return [self.id, self.name, genres, str(self.followers), str(self.popularity)]
    def __repr__(self):
        return '%s' % self.name
    def __str__ (self):
        return self.name


class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.String(22), primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    main_artist = db.Column(db.String)
    main_artist_id = db.Column(db.String(22))
    all_artists = db.Column(db.String)
    type = db.Column(db.String)
    image_url = db.Column(db.String)
    duration = db.Column(db.String)
    release_date = db.Column(db.String)
    record_label = db.Column(db.String)
    popularity = db.Column(db.Integer)
    number_of_tracks = db.Column(db.Integer)

    def to_json(self): 
        json_albums = {
            'id' : self.id,
            'name' : self.name,
            'url' : self.url,
            'main_artist' : self.main_artist,
            'main_artist_id' : self.main_artist_id,
            'all_artists' : self.all_artists,
            'type' : self.type,
            'image_url' : self.image_url,
            'duration' : self.duration,
            'release_date' : self.release_date,
            'record_label' : self.recodr_label,
            'popularity' : self.popularity,
            'number_of_tracks' : self.number_of_tracks
        }
        return json_albums

    def to_list(self):
        #artist_list = self.all_artists[1:-1]
        #artist_list = artist_list.split(",")
        #all_artists_names = ''
        #for id in artist_list:
        #    if Artist.query.filter_by(id=id).first() != None:
        #        all_artists_names += Artist.query.filter_by(id=id).first().name + ', '
        #all_artists_names = all_artists_names[0:-2]
        return [self.id, self.name, self.main_artist, self.release_date, self.record_label, self.number_of_tracks, self.popularity]
    
    def get_all_artists(self):
        all_artists_names = ''
        for id in artist_list:
            if Artist.query.filter_by(id=id).first() != None:
                all_artists_names += Artist.query.filter_by(id=id).first().name + ', '
        all_artists_names = all_artists_names[0:-2]
        return all_artists_names
    def __repr__(self):
        return 'Album %r' % self.name
    def __str__(self):
        return self.name


class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.String(22), primary_key=True)
    name = db.Column(db.String)
    main_artist_id = db.Column(db.String(22))
    all_artists = db.Column(db.String)
    track_no = db.Column(db.Integer)
    album_id = db.Column(db.String)
    duration = db.Column(db.String)
    duration_ms = db.Column(db.Integer)
    explicit = db.Column(db.Boolean)
    popularity = db.Column(db.Integer)
    preview_url = db.Column(db.String)
    direct_url = db.Column(db.String)

    def to_json(self): 
        json_albums = {
            'id' : self.id,
            'name' : self.name,
            'main_artist_id' : self.main_artist_id,
            'all_artists' : self.all_artists,
            'track_no' : self.track_no,
            'album_id' : self.album_id,
            'duration' : self.duration,
            'duration_ms' : self.duration_ms,
            'explicit' : self.explicit,
            'popularity' : self.popularity,
            'preview_url' : self.preview_url,
            'direct_url' : self.direct_url
        }
        return json_albums
    def to_list(self):
        album_name = Album.query.filter_by(id=self.album_id).first().name
        artist_name = Artist.query.filter_by(id=self.main_artist_id).first().name
        return [self.id, self.name, str(self.track_no), album_name, artist_name, self.duration, str(self.explicit), str(self.popularity)]

    def __repr__(self):
        return 'Track %r' % self.name
    def __str__(self):
        return self.name


if __name__ == "__main__":
	createTables()
	populateData()
