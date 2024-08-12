from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Execute the instructions from the chinook db 
db = create_engine("postgresql://localhost/chinook")

Base = declarative_base()

# Create a class-based model for the programmer table 
class Programmer(Base):
    __tablename__ = "Programmer"

    programmer_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# Build a sessionmaker object to establish a session with the database
Session = sessionmaker(bind=db)
session = Session()

# Create the database using declarative_base subclasses
Base.metadata.create_all(db)

# Create a new programmer
ada_lovelace = Programmer(
    first_name="Ada", 
    last_name="Lovelace", 
    gender="F", 
    nationality="British", 
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan", 
    last_name="Turing", 
    gender="M", 
    nationality="British", 
    famous_for="Turing Machine"
)

grace_hopper = Programmer(
    first_name="Grace", 
    last_name="Hopper", 
    gender="F", 
    nationality="American", 
    famous_for="COBOL"
)

margaret_hamilton = Programmer(
    first_name="Margaret", 
    last_name="Hamilton", 
    gender="F", 
    nationality="American", 
    famous_for="Apollo Guidance Software"
)

tim_berners_lee = Programmer(
    first_name="Tim", 
    last_name="Berners-Lee", 
    gender="M", 
    nationality="British", 
    famous_for="World Wide Web"
)

linus_torvalds = Programmer(
    first_name="Linus", 
    last_name="Torvalds", 
    gender="M", 
    nationality="Finnish", 
    famous_for="Linux Kernel"
)

bill_gates = Programmer(
    first_name="Bill", 
    last_name="Gates", 
    gender="M", 
    nationality="American", 
    famous_for="Microsoft"
)

steve_jobs = Programmer(
    first_name="Steve", 
    last_name="Jobs", 
    gender="M", 
    nationality="American", 
    famous_for="Apple Inc."
)

katherine_johnson = Programmer(
    first_name="Katherine", 
    last_name="Johnson", 
    gender="F", 
    nationality="American", 
    famous_for="NASA Calculations"
)

dennis_ritchie = Programmer(
    first_name="Dennis", 
    last_name="Ritchie", 
    gender="M", 
    nationality="American", 
    famous_for="C Programming Language"
)

hasibullah_fathi = Programmer(
    first_name="Hasibullah", 
    last_name="Fathi", 
    gender="M",
    nationality="Afghan", 
    famous_for="Machine Learning"
)

# ================================================================
# Add all the new programmers to the session
session.add_all([
    # ada_lovelace,
    # alan_turing,
    # grace_hopper,
    # margaret_hamilton,
    # tim_berners_lee,
    # linus_torvalds,
    # bill_gates,
    # steve_jobs,
    # katherine_johnson,
    # dennis_ritchie,
    # hasibullah_fathi,
])

# Add the new programmer to the session
# session.add(ada_lovelace)
# session.commit()
# ================================================================
# # update a single record 
# programmer = session.query(Programmer).filter_by(programmer_id=17).first()
# programmer.famous_for = "Software Engineering"

# # Commit the changes to the database
# session.commit()
# ============================================================
# # update a multiple record
# people = session.query(Programmer)

# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Unknown Gender")
#     session.commit()

# ============================================================
# delete a record
# fname = input("Enter the first name: ")
# lname = input("Enter the last name: ")

# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming 
# if programmer is not None:
#     print(f"Programmer found {programmer.first_name} {programmer.last_name}")
#     confirmation = input("Are you sure you want to delete this record? y/n: ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer deleted successfully")
#     else:
#         print("Deletion cancelled")
# else:
#     print(f"No programmer found with first name {fname} and last name {lname}")


# ================================================================
# delete all records 
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()



# Query the database to find the programmers
programmers = session.query(Programmer).all()

# Iterate over the results and print them
for programmer in programmers:
    print(
        f"{programmer.programmer_id} | "
        f"{programmer.first_name} {programmer.last_name} | "
        f"{programmer.gender} | "
        f"{programmer.nationality} | "
        f"{programmer.famous_for}"
    )

# Close the session
session.close()
