import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


class DBManager:
    def __init__(self, db_name):
        self.__db_name = db_name

    def __execute_query(self, query):
        conn = psycopg2.connect(dbname=self.__db_name, user=os.getenv("user"), password=os.getenv("password"),
                                host=os.getenv("host"), port=os.getenv("port"))

        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
        conn.close()
        return result

    def all_employers(self):
        return self.__execute_query("select * from employer")

    def get_companies_and_vacancies_count(self):
        pass

    def get_all_vacancies(self):
        pass

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self):
        pass
