import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import csv


cred = credentials.Certificate('key.json')
databaseURL = 'https://mfg717m-final-default-rtdb.asia-southeast1.firebasedatabase.app/'

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': databaseURL
    })


#Log access data
def access_log(datetime, file_accessed, country_accessed, user_access):
    ref = db.reference('access_log')
    ref.update({
        datetime: {
            'file_accessed': file_accessed,
            'country_accessed': country_accessed,
            'user_accessed': user_access
        }
    })
    return None

while True:
    a = input('Search: ')
    if a == 'stop':
        break
    ref = db.reference('Optical_Images')
    results = ref.order_by_child('cloud_cover').equal_to(int(a)).get()
    for i in results:
        print(ref.get()[int(i)]['image_data'])