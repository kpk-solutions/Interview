from ast import List

data = {
    "employees": [
      {
        "employee_id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "1985-05-15",
        "salary": 75000.0,
        "skills": {
          "programming": ["Java", "Python", "C++"],
          "languages": ["English", "Spanish"]
        }
      },
      {
        "employee_id": 2,
        "first_name": "Jane",
        "last_name": "Smith",
        "date_of_birth": "1990-09-20",
        "salary": 80000.0,
        "skills": {
          "programming": ["JavaScript", "HTML", "CSS"],
          "languages": ["English", "French"]
        }
      },
      {
        "employee_id": 3,
        "first_name": "Michael",
        "last_name": "Johnson",
        "date_of_birth": "1978-12-10",
        "salary": 90000.0,
        "skills": {
          "programming": ["Python", "SQL", "JavaScript"],
          "languages": ["English", "German"]
        }
      },
      {
        "employee_id": 4,
        "first_name": "Sarah",
        "last_name": "Williams",
        "date_of_birth": "1989-06-25",
        "salary": 82000.0,
        "skills": {
          "programming": ["C#", "Java", "Ruby"],
          "languages": ["English", "Spanish"]
        }
      },
      {
        "employee_id": 5,
        "first_name": "David",
        "last_name": "Clark",
        "date_of_birth": "1992-02-18",
        "salary": 77000.0,
        "skills": {
          "programming": ["JavaScript", "HTML", "CSS"],
          "languages": ["English", "Mandarin"]
        }
      }
  ]
}


# You need to validate every employee record before saving into DB. Validations are as follows
#
#
# Every field is mandatory.
# An employee should be aware of at least 1 Programming and communication Language
# Note: The Employee contract may grow and become more complex in the future
class skillModel(BaseModel):
    programming: List[str] = []
    languages: List[str] = []

class EmployeeModel(BaseModel):
    employee_id: int
    first_name: str
    last_name: str
    skills: skillModel

def data_load(data):
    for i, j in data.items():
        'db logic'
        if j["programming"] and j["languages"] :
            employee = EmployeeModel(**j)
            employee.employee_id = j if j else ''
            employee.first_name = j["first_name"]
            employee.last_name = j["last_name"]
            skillModel.programming = j["programming"] if j["programming"] != "" else ''
            skillModel.languages = j["languages"]

@app.post("api/v1/employee/", response_model=paylaod)
def dbInsert(payload:data):
    data_load(payload)


