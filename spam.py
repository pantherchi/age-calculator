class spam:
    def get_email_address():
        #the code to open up a window that gets the email address
        Email = input("Email: ")
        return Email

    def get_email_username():
        #the code to open up a window that gets email username
        Email_Username = input("username: ")
        return Email_Username

    #same for the email recipient and email password

    def send_email():
        # variables from the other def's
        #email_address = get_email_address()
        #email_username = get_email_username()
        return 'The current date is - {} \n {}'.format(email_address, email_username)

        #code to send email
spam.get_email_address()
spam.get_email_username()
print(send_email())
