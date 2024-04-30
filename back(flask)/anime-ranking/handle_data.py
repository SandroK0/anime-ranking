import os
from app import db, app, Anime

image_folder = 'static/images'

def add_images(session, Anime):
    for filename in os.listdir(image_folder):

        if filename.endswith('.jpg') or filename.endswith('.png'):            
            image_path = os.path.join(image_folder, filename)
            anime = Anime(image=image_path, title=filename.split(".")[0])
            session.add(anime)
    session.commit()

with app.app_context():
    add_images(session=db.session, Anime=Anime)
