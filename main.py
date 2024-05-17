
from mongoengine import connect
from models import Quote, Author


uri = "mongodb+srv://goitlearn:Goit2023@cluster0.p3tvwqy.mongodb.net/hw-08?retryWrites=true&w=majority&appName=Cluster0"
connect(host=uri)

def search_quotes_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return quotes

def search_quotes_by_author(author_name):
    author = Author.objects(fullname=author_name).first()
    if author:
        quotes = Quote.objects(author=author)
        return quotes
    else:
        return []

def search_quotes_by_tags(tags):
    quotes = Quote.objects(tags__in=tags)
    return quotes

if __name__ == '__main__':
    print("Welcome to the Quote Search Script!")
    while True:
        command = input("Enter command (tag, author name, tags, exit): ")
        if command == 'exit':
            print("Goodbye!")
            break
        elif command == 'tag':
            tag = input("Enter tag: ")
            quotes = search_quotes_by_tag(tag)
            print("Quotes with tag '{tag}':")#.format(tag))
            for quote in quotes:
                print("- {}".format(quote.quote))
        
         elif command == 'author name':
            author_name = input("Enter author's name: ")
            quotes = search_quotes_by_author(author_name)
            print(f"Quotes by author '{author_name}':")
            for quote in quotes:
                print("- {}".format(quote.quote))

        elif command == 'tags':
            tags = input("Enter tags separated by commas: ").split(',')
            quotes = search_quotes_by_tags(tags)
            print("Quotes with tags '{}':".format(', '.join(tags)))
            for quote in quotes:
                print("- {}".format(quote.quote))
        else:
            print("Invalid command. Please try again.")

   
        
