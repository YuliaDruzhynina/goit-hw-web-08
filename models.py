
from mongoengine import EmbeddedDocument, Document,ObjectIdField, ReferenceField
from mongoengine.fields import EmbeddedDocumentField, ListField, StringField


class Quote(Document):
    #places_id = ReferenceField('Author')#думаю лишний
    author = ReferenceField('Author')
    quote = StringField()
    tags = ListField(StringField())


class Author(Document):
    original_id = ObjectIdField()
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    quote = ListField(ReferenceField(Quote))

