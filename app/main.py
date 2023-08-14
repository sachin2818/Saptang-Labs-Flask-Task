from flask import Flask, jsonify, request
from bson.objectid import ObjectId

from app.models import Profile, Post
from app.load_dummy_data import load

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/profiles", methods=["GET"])
def get_profiles():
    page_nb = int(request.args.get('page', "1"))
    items_per_page = 25 

    offset = (page_nb - 1) * items_per_page

    profiles = [ {"id":str(profile.id), "profile_name":profile.profile_name} for profile in 
                Profile.objects.only("id","profile_name").skip( offset ).limit( items_per_page )]
    print(profiles)
    if profiles:
        return profiles
    
    return jsonify({"error": "Profiles not found"}), 404


@app.route("/profiles/<id>", methods=["GET"])
def get_profile_data(id):
    profile = Profile.objects(id=ObjectId(id)).exclude("id").first()
    if profile:
        return {"data":profile.to_mongo(), "id":id}
    return jsonify({"error": "Profile not found"}), 404


@app.route("/posts", methods=["GET"])
def get_posts():
    page_nb = int(request.args.get('page', "1"))
    items_per_page = 25 

    offset = (page_nb - 1) * items_per_page

    posts = [ {"id":str(Post.id)} for Post in 
                Post.objects.only("id").skip( offset ).limit( items_per_page )]
    print(posts)
    if posts:
        return posts
    
    return jsonify({"error": "Posts not found"}), 404


@app.route("/posts/<id>", methods=["GET"])
def get_post_data(id):
    post = Post.objects(id=ObjectId(id)).exclude("id").first()
    if post:
        return {"data":post.to_mongo(), "id":id}
    return jsonify({"error": "Post not found"}), 404


load() # load dummy data


def create_app():
    return app


if __name__ == "__main__":
    app.run(debug=True)

