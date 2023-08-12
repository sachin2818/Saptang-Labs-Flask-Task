from mongoengine import connect, Document, StringField, ListField, DictField, \
                        EmbeddedDocument, EmbeddedDocumentField, IntField
import os

connect(host=os.environ["MONGO_URI"])


class LikedProfiles(EmbeddedDocument):
    profile_name = StringField(required=True)
    profile_link = StringField(required=True)


class CommentMessage(EmbeddedDocument):
    commented_profile  = StringField(required=True)
    commented_profile_link  = StringField(required=True)
    comment  = StringField(required=True)


class Profile(Document):
    meta = {'collection': 'ProfileCollection'}
    profile_name = StringField(required=True)
    description = StringField()
    location = StringField()
    followers_count = IntField()


class Post(Document):
    meta = {'collection': 'PostCollection'}
    posted_date_time = StringField()
    post_content = StringField()
    hashtag = ListField(StringField())
    likes_count = IntField()
    liked_profiles = ListField(EmbeddedDocumentField(LikedProfiles))
    comment_count = IntField()
    comment_message = ListField(EmbeddedDocumentField(CommentMessage))


