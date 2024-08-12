from sqlalchemy import(
    create_engine, Column, Integer, String, ForeignKey, Float
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# execute the instructions from the chinook db 
db = create_engine("postgresql://localhost/chinook")

base = declarative_base()



# create a class for the Artist table
class Artist(base):
    __tablename__ = "Artist"

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class for the Album table
class Album(base):
    __tablename__ = "Album"

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class for the Track table
class Track(base):
    __tablename__ = "Track"

    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)



# build a sessionmaker object to establish a session with the database
Session = sessionmaker(bind=db)

# create a session object
session = Session()

base.metadata.create_all(db)

# # qurey 1 select all records from the Artist 
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep = " | ")

# # query 2 select only names from the Artist
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)


# # query 3 select all records from the Artist where name is Queen
# artists = session.query(Artist)
# for artist in artists:
#     if artist.Name == "Queen":
#         print(artist.ArtistId, artist.Name, sep = " | ")
# # or alternatively we could use the artist like so
# artist = session.query(Artist).filter_by(Name = "Queen").first()
# print(artist.ArtistId, artist.Name, sep = " | ")


# # query 4 select all records from the Artist where ArtistId is 51
# artist = session.query(Artist).filter_by(ArtistId = 51).first()
# print(artist.ArtistId, artist.Name, sep = " | ")


# # # query 5 select all records from Album where ArtistId is 51
# albums = session.query(Album)
# for album in albums:
#     if album.ArtistId == 51:
#         print(album.AlbumId, album.Title, sep = " | ")
# # or alternatively we could use the album like so
# albums = session.query(Album).filter_by(ArtistId = 51)
# for album in albums:
#     print(album.AlbumId, album.Title, sep = " | ")


# query 6 select all tracks where the composer is "Queen"
tracks = session.query(Track).filter_by(Composer = "Queen")

for track in tracks:
    print(track.TrackId, track.Name, track.AlbumId, track.MediaTypeId, track.GenreId, track.Composer, track.Milliseconds, track.Bytes, track.UnitPrice, sep = " | ")



# Close the session
session.close()