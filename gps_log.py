import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import csv

# Fetch the service account key JSON file contents
cred = credentials.Certificate('key.json')

# Initialize the app with a service account, granting admin privileges
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://mfg717m-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('')

reader = csv.reader(open('gps.csv'))
gps_lat = 0
gps_long = 0
i = 0

for row in reader:
    gps_lat = row[0]
    gps_long = row[1]
    ref.child(str(i)).update({'gps_lat':gps_lat})
    ref.child(str(i)).update({'gps_long':gps_long})
    i+=1