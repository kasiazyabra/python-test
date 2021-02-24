import application.salary
import application.db.people
from datetime import datetime, date, time

if __name__ == '__main__':
    application.salary.calculate_salary()
    application.db.people.get_employees()
    print(datetime.today())
