def menu():
    print("1. Send Email")
    print("2. Send SMS")
    print("3. Send Whatsapp")
    print("4.Exit")
    
menu() 
option=int(input("Enter your option:"))
while option !=0:
    
    if option==1:
        import smtplib
        from email.message import EmailMessage


        print("Email application started...Please wait...")
        msg=EmailMessage()

        msg['Subject']="Python tutorial"
        msg['From']="xyz@gmail.com"
        msg['To']="abcd@gmail.com"
        msg.set_content('Hello there/ this is demo email')
        Myserver = smtplib.SMTP('smtp.gmail.com',587)
        Myserver.starttls
        Myserver.login('keshavtrikha08@gmail.com',"********")
        Myserver.send_message(msg)
        Myserver.quit()
        print('Email sent successfully')
    
    elif option==2:
        from twilio.rest import Client
        SID = 'ACf5a19f9b908d13b186d4ac94df4fffd0'
        AUTH_TOKEN = 'f0abbd93482a7f80c270db072c033baf'

        cl = Client(SID, AUTH_TOKEN)

        cl.messages.create(body='Hey, I am GreyMatters Here', from_='+14704666619',to='+91**********')
        
    elif option==3:
        import pywhatkit
        pywhatkit.sendwhatmsg('+91**********','Hello there',12,19)
        
    elif option==4:
        print("Exiting the program")
        break
        
    else:
        print("Invalid option")
    
    print()
    menu()
    option=int(input("Enter your option:"))
    print("Thanks")
    
    

