from utils.utils import create_db, create_table, insert_data
from classes.db_manager import DBManager


db_name = "course_test"

create_db(db_name)
create_table(db_name)
insert_data(db_name)


db_manager = DBManager(db_name)

print(db_manager.all_employers())
