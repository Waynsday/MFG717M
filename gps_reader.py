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
gps_lat, gps_long = 0,0
i = 0

print(ref.get()[i]['gps_lat'])
while(True):
    print('{0},{1}'.format(ref.get()[i]['gps_lat'],ref.get()[i]['gps_long']))
    i+=1
