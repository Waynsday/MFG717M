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
ref = db.reference('user/')


# ##CREATE
# ref.set({
#     'Wayne Akeboshi':{
#         'nickname': 'Wayne',
#         'age': 22
#     },
#     'Juan Dela Cruz':{
#         'nickname': 'Juan',
#         'age': 25
#     }
# })
#
# ##UPDATE
# ref.child('Juan Dela Cruz').update({'nickname':'John'})
#
# ##READ
# snapshot = ref.get()
# print(snapshot['Wayne Akeboshi']['nickname'])
#
# for snap in snapshot:
#     print(snapshot[snap]['age'])
#     print(snapshot[snap]['nickname'])
#
# ##DELETE
# ref.child('Wayne Akeboshi').delete()
#
#
# ##LISTENER
# def listener(event):
#     print(event.data)
#
# db.reference('').listen(listener)

reader = csv.reader(open('gps.csv'))
gps_lat, gps_long = 0,0
i = 0

for row in reader:
    gps_lat = row[0]
    gps_long = row[1]
    ref.child(i).update({'gps_lat':gps_lat})
    ref.child(i).update({'gps_long':gps_long})
    i+=1