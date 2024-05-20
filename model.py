
from mongoengine import Document, BooleanField, StringField
from mongoengine import connect

connect(host="mongodb+srv://goitlearn:Goit2023@cluster0.p3tvwqy.mongodb.net/hw-08?retryWrites=true&w=majority&appName=Cluster0")

class Contact(Document):
   
    fullname = StringField()
    email = StringField()
    email_sent = BooleanField(default=False)

