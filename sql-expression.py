from sqlalchemy import(
    create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Float
)

# excecuting instructions form localhost chinook database 
db = create_engine("postgresql://localhost/chinook")


# db = create_engine("Postgresql:///chinook")

meta = MetaData(db)

artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String),
    )


# create variable for album table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("Artist.ArtistId"))
    )


# create variable for track table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("Album.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
    )

# making the connection to the database
with db.connect() as connection:
    # query 1 select all the records from the artist table
    # select_query = artist_table.select()

    # query 2 select name column from artist_table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # query 3 select all records from artist_table where name is queen
    # select_query = select(artist_table).where(artist_table.c.Name == "Queen")

    # query 4 select all records from artist_table where artistid is 51
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # query 5 select all records from album_table where artistid is 51
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # query 6 select all records from track_table where composer is queen
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    # execute the query and print the results
    # print(connection.execute(select_query).fetchall())  # for multiple results

    # print(connection.execute(select_query).fetchone())

    results = connection.execute(select_query)

    for result in results:
        print(result)

