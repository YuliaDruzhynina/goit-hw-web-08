import pika
from faker import Faker
from model import Contact
from mongoengine import connect
import json

uri = "mongodb+srv://goitlearn:Goit2023@cluster0.p3tvwqy.mongodb.net/hw-08?retryWrites=true&w=majority&appName=Cluster0"
connect(host=uri)

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='task_mock', exchange_type='direct')
channel.queue_declare(queue='email_queue', durable=True)
channel.queue_bind(exchange='task_mock', queue='email_queue')


def add_contact(n):
    faker = Faker()
    contacts_list = []
    for _ in range(n):
        contact = Contact(
            fullname=faker.name(),
            email=faker.email()
        )
        contact.save() 
        contacts_list.append(contact)
    return contacts_list  


if __name__ == '__main__':
    contacts = add_contact(10)  
    for contact in contacts:
        # Отправили  сообщения с ObjectID контакта в очередь RabbitMQ
        channel.basic_publish(
            exchange='task_mock',
            routing_key='email_queue',
            body=json.dumps(str(contact.id)),  # Преобразование ObjectID в строку для синхр с json и сериализация в JSON
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            )
        )
    print("Sent contacts to queue")
    connection.close()