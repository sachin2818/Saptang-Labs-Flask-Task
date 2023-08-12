import os

from app.models import Profile, Post, CommentMessage, LikedProfiles
from faker import Faker
import random


faker = Faker()


def create_dummy_profile():
    profile = Profile(
        profile_name=faker.name(),
        description=faker.text(),
        location=faker.city(),
        followers_count=random.randint(1, 10000)
    )
    profile.save()
    return profile

def create_dummy_post(profile, profiles):
    comments = []
    for _ in range(random.randint(1, 10)):
        _profile = random.choice(profiles)
        comments.append(CommentMessage(
                    commented_profile=_profile.profile_name,
                    commented_profile_link=f"/profile/{_profile.id}",
                    comment=faker.text()
                ) )
    
    liked_profiles = []
    for _ in range(random.randint(1, 50)):
        _profile = random.choice(profiles)
        liked_profiles.append(LikedProfiles(profile_name=_profile.profile_name,
                        profile_link=f"/profile/{_profile.id}"))

    post = Post(
        posted_date_time=faker.date_time_this_year().isoformat(),
        post_content=faker.text(),
        hashtag=[f"#{faker.word()}" for _ in range(random.randint(1, 5))],
        likes_count=len(liked_profiles),
        liked_profiles=liked_profiles,
        comment_count=len(comments),
        comment_message=comments
    )
    post.save()

# Create dummy data
NUM_PROFILES = 10
NUM_POSTS_PER_PROFILE = 5


def load():
    profiles = [create_dummy_profile() for _ in range(NUM_PROFILES) ]

    for profile in profiles:
        create_dummy_post(profile, profiles)

    print("Dummy data generation complete!")