from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os

name = input("Enter Name:")
batch = input("Batch:")
contact = input("Contact No:")
email = input("Enter senders mail:")
num = input("Enter the number of tickets:")

for i in range(1,int(num)+1):
    img = Image.open("ticket.jpg")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("adventpro-bold.ttf", 20)
    file = open('serial.txt', 'r')
    serial = file.read(4)
    file.close()

    #draw.text((x, y),"Sample Text",(r,g,b))
    #Name
    draw.text((120, 330),name,(0,0,0),font=font)

    #Batch
    draw.text((120, 370),batch,(0,0,0),font=font)

    #Contact No
    draw.text((190, 410),contact,(0,0,0),font=font)

    #Slno-1
    draw.text((330, 10),serial,(0,0,0),font=font)

    #Slno-2
    draw.text((1430, 9),serial,(0,0,0),font=font)

    img.save('C:/Users/Asus/Desktop/Tickets/tickets/'+name+batch+str(i)+'.jpg')
    img.save('output.jpg')

    import csv
    with open('details.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([serial,name,batch,contact,email])

    file = open('serial.txt','w')
    serial = int(serial) + 1
    file.write(str(serial))
    file.close()

    from mailsender import MailSender

    username = 'youremail@gmail.com'
    password = 'password'
    sender = username

    images = list()
    images.append({
        'id': 'logo',
        'path': 'output.jpg'
    })

    with open('template.html') as template_html, open('template.txt') as template_plain:
        message_html = template_html.read()
        message_plain = template_plain.read()
        mail_sender = MailSender(username, password)
        mail_sender.send(sender, [email], 'Lucky draw ticket.', message_html=message_html, message_plain=message_plain, images=images)
    print('..')
    os.remove("output.jpg")
print('Email Send')
    