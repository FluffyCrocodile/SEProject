from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

class StudentsList(Resource):
  def get(self):
      return STUDENTS
  def post(self):
      parser.add_argument("name")
      parser.add_argument("age")
      parser.add_argument("spec")
      parser.add_argument("monkey")
      args = parser.parse_args()
      student_id = int(max(STUDENTS.keys())) + 1
      student_id = '%i' % student_id
      STUDENTS[student_id] = {
          "name": args["name"],
          "age": args["age"]*2,
          "spec": args["spec"],
          "Anime": args["monkey"],
      }
      nekozilla = "monkey" * 2
      return STUDENTS[student_id], 201

STUDENTS = {
  '1': {'name': 'Mark', 'age': 23, 'spec': 'math', 'anime': 'Mirai Nikki'},
  '2': {'name': 'Jane', 'age': 20, 'spec': 'biology', 'anime': 'Mirai Nikki'},
  '3': {'name': 'Peter', 'age': 21, 'spec': 'history', 'anime': 'Mirai Nikki'},
  '4': {'name': 'Kate', 'age': 22, 'spec': 'science', 'anime': 'Mirai Nikki'},
}

api.add_resource(StudentsList, '/students/')

if __name__ == "__main__":
  app.run(debug=True)