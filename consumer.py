import pika
from model import Contact
import sys
from mongoengine import connect
from bson import ObjectId

uri = "mongodb+srv://goitlearn:Goit2023@cluster0.p3tvwqy.mongodb.net/hw-08?retryWrites=true&w=majority&appName=Cluster0"
connect(host=uri)

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue', durable=True)

    
     def callback(ch, method, properties, body):
        contact_id = body.decode()
        contact = Contact.objects(id=contact_id, email_sent=False).first()
        if contact:
            contact.update(set__email_sent=True)
        print(f"send email to contact id: {contact_id}, {contact.fullname}")

    #channel.basic_qos(prefetch_count=1)макс.кількість повідомлень, які споживач може взяти 
    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
