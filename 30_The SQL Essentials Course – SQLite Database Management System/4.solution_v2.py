import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///students_sqlalchemy.db")

connection = engine.connect()

metadata = sqlalchemy.MetaData()

students = sqlalchemy.Table("Students", metadata,
                            sqlalchemy.Column(
                                "student_id", sqlalchemy.Integer, primary_key=True),
                            sqlalchemy.Column("first_name", sqlalchemy.Text),
                            sqlalchemy.Column("last_name", sqlalchemy.Text),
                            sqlalchemy.Column("email_address", sqlalchemy.Text)
                            )

metadata.create_all(engine)

student_records = students.insert().values([
    {"first_name": "Alexander", "last_name": "Hunold",
     "email_address": "alexander.hunold@el.cool"},
    {"first_name": "Nancy", "last_name": "Pelosi",
        "email_address": "nancy.pelosi@el.cool"},
    {"first_name": "Irene", "last_name": "Mikkilineni",
        "email_address": "irene.mikkilineni@el.cool"},
    {"first_name": "Sarah", "last_name": "Bell",
        "email_address": "sarah.bell@el.cool"}
])


connection.execute(student_records)

selection_query = sqlalchemy.select([students.columns.email_address])
selection_result = connection.execute(selection_query)

print(selection_result.fetchall())
