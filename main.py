from flask import Flask
from flask_restful import Resource, Api, reqparse
import base64

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

class StudentsList(Resource):
  def get(self):
      return STUDENTS
  def post(self):
      parser.add_argument("Text")
      parser.add_argument("Key")
      args = parser.parse_args()
      student_id = int(max(STUDENTS.keys())) + 1
      student_id = '%i' % student_id

      msg = args["Text"]
      key = args["Key"]

      enc = []
      for i in range(len(msg)):
          key_c = key[i % len(key)]
          enc_c = chr((ord(msg[i]) +
                       ord(key_c)) % 256)
          enc.append(enc_c)
          print("enc:", enc)
      encoded = base64.urlsafe_b64encode("".join(enc).encode()).decode()

      STUDENTS[student_id] = {
          "Secret": encoded,
          "Key": args["Key"]
      }
      return STUDENTS[student_id], 201



STUDENTS = {
  '1': {'Text': 'Mark', 'Key': 23, 'spec': 'math', 'Secret': 'Mirai Nikki'}
}

api.add_resource(StudentsList, '/')

if __name__ == "__main__":
  app.run(debug=True)