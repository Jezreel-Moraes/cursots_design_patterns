from classes.validations import Validations


def main():
    email = 'email@gmail.com'
    if (response := Validations.is_email(email)):
        print(email, 'is email:', response)


if __name__ == '__main__':
    main()
