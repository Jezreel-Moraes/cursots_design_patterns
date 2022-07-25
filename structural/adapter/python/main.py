from validations import Validations

if __name__ == '__main__':
   email = 'jezreel.aluno@gmail.com'
   if (response:= Validations.is_email(email)):
      print(response)