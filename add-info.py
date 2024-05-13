
import json
from mongoengine import connect
from models import Quote, Author  
uri = "mongodb+srv://goitlearn:Goit2023@cluster0.p3tvwqy.mongodb.net/hw-08?retryWrites=true&w=majority&appName=Cluster0"
connect(host=uri)


with open('authors.json', 'r') as file:
    data1 = json.load(file)

with open('quotes.json', 'r') as file:
    data2 = json.load(file)


for item in data1:
    author = Author(
        fullname=item['fullname'],
        born_date=item['born_date'],
        born_location=item['born_location'],
        description=item['description']
    )
    author.save()


for item in data2:
    author_name = item.get('author')  # Получаем имя автора из данных цитаты
    author = Author.objects(fullname=author_name).first()  # Поиск автора по имени

    if author:
        quote = Quote(
            tags=item['tags'],
            author=author,
            quote=item['quote']
        )
        quote.save()
    else:
        print(f"Author '{author_name}' not found.")






    
# import json
# from mongoengine import connect
# from models import Quote, Author  

# # Подключение к базе данных
# connect("hw-08")

# # Чтение данных из первого JSON-файла
# with open('authors.json', 'r') as file:
#     data1 = json.load(file)

# # Чтение данных из второго JSON-файла
# with open('quotes.json', 'r') as file:
#     data2 = json.load(file)

# # Создание и сохранение объектов Author из первого JSON-файла
# for item in data1:
#     author = Author(
#         fullname=item['fullname'],
#         born_date=item['born_date'],
#         born_location=item['born_location'],
#         description=item['description']
#     )
#     author.save()

# # Создание и сохранение объектов Quote из второго JSON-файла
# for item in data2:
#     # Получение объекта Author по имени из первого JSON-файла
#     author = Author.objects.get(fullname=item['author_fullname'])

#     quote = Quote(
#         places_id=author,
#         tags=item['tags'],
#         author=author,
#         content=item['content']
#     )
#     quote.save()
# import json
# from mongoengine import connect
# from models import Quote, Author  

# # Подключение к базе данных
# connect("hw-08")

# # Чтение данных из первого JSON-файла
# with open('authors.json', 'r') as file:
#     data1 = json.load(file)

# # Чтение данных из второго JSON-файла
# with open('quotes.json', 'r') as file:
#     data2 = json.load(file)

# # Создание и сохранение объектов Author из первого JSON-файла
# for item in data1:
#     author = Author(
#         fullname=item['fullname'],
#         born_date=item['born_date'],
#         born_location=item['born_location'],
#         description=item['description']
#     )
#     author.save()

# # Создание и сохранение объектов Quote из второго JSON-файла
# for item in data2:
#     # Получение объекта Author по имени из первого JSON-файла
#     author = Author.objects.get(fullname=item['author_fullname'])

#     quote = Quote(
#         places_id=author,
#         tags=item['tags'],
#         author=author,
#         content=item['content']
#     )
#     quote.save()




# from models import Quote, Author
# import connect

# import json
# from pymongo import MongoClient

# # Подключение к MongoDB Atlas
# client = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/<dbname>?retryWrites=true&w=majority")
# db = client.get_database()

# # Путь к JSON-файлам
# json_files = ["file1.json", "file2.json"]

# # Загрузка данных из JSON-файлов в базу данных
# for file_name in json_files:
#     with open(file_name, 'r') as file:
#         data = json.load(file)
#         # Выберите коллекцию, в которую хотите загрузить данные
#         collection = db['collection_name']
#         # Вставляем данные в коллекцию
#         collection.insert_many(data)

#print("Data loaded successfully.")




# qoute = Quote(author=author,
#               description='In 1879, Albert Einstein was born in Ulm, Germany. He completed his Ph.D. at the University')


# author = Author(fullname='Albert Einstein', 
#               born_date='March 14, 1879',
#               born_location='in Ulm, Germany',
#               description='In 1879, Albert Einstein was born in Ulm, Germany. He completed his Ph.D. at the University \
#                 of Zurich by 1909. His 1905 paper explaining the photoelectric effect, the basis of electronics, earned  \
#                 him the Nobel Prize in 1921. His first paper on Special Relativity')


# author.quotes.append(quote)
# author.save()