from flask import Flask, render_template, redirect
import pymongo
import scrape_mars
import pprint

# setting up pretty print
pp = pprint.PrettyPrinter(indent=2)

# Create an instance of Flask
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db

# Drops collection if available to remove duplicates
db.mars.drop()

# # Creates a collection in the database and inserts two documents
# db.mars.insert_many(
#     [
#         {
#             'player': 'Jessica',
#             'position': 'Point Guard'
#         },
#         {
#             'player': 'Mark',
#             'position': 'Center'
#         }
#     ]
# )

@app.route("/")
def home():
    # Find one record of data from the mongo database
    mars_dict = db.mars.find_one()
    print("mars_dict:")
    pp.pprint(mars_dict)

    # Return template and data
    return render_template("index.html", mars=mars_dict)

# Set route
@app.route('/scrape')
def scrape():
    # Run the scrape function
    mars_dict = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    db.mars.update({}, mars_dict, upsert=True)

    # Redirect back to home page
    return redirect("/")





if __name__ == "__main__":
    app.run(debug=True)