from app import db, Anime, app  # Import the app, db, and Anime model from Flask app
import csv

# Function to import data from CSV to the SQLite database


def import_csv_to_sqlite(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            # Prepare the image path by replacing URL with '/static/images/<anime_id>.jpeg'
            image_path = f'/static/images/{row["id"]}.jpeg'

            # Create an instance of Anime and populate the fields
            anime = Anime(
                id=row["id"],
                title=row["title"],  # Assuming CSV has 'title'
                years=row["years"],
                eps=row["eps"],
                desc=row["desc"],
                image=image_path
            )

            # Add the anime to the session
            db.session.add(anime)

        # Commit the changes to the database
        db.session.commit()
        print(f"Data from {
              csv_file} has been imported successfully into SQLite.")


# Main function to run the script
if __name__ == '__main__':
    # Push the app context to allow database operations
    with app.app_context():
        # Path to your CSV file
        csv_file = 'anime_data.csv'  # Replace with your CSV file path

        # Import the data from the CSV into the SQLite database
        import_csv_to_sqlite(csv_file)
