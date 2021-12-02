import smtplib,ssl
def sendemail(message):
    smtpserver="smtp.gmail.com"
    port=587
    senderemail="virajmehtayt@gmail.com"
    password="Mehta2202"
    recieveremail="pooja.chhikara8@gmail.com"
    context=ssl.create_default_context()
    try:
        server=smtplib.SMTP(smtpserver,port)
        server.starttls(context=context)
        server.login(senderemail,password)
        server.sendmail(senderemail,recieveremail,message)

    except Exception as e:
        print(e)

    finally:
        server.quit()
        
    
