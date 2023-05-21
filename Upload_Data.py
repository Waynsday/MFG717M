import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
srcpath = '/Users/ERDT/Desktop/Wayne/MFG717M/Data'
srcfiles = os.listdir(srcpath)


cred = credentials.Certificate('key.json')
databaseURL = 'https://mfg717m-final-default-rtdb.asia-southeast1.firebasedatabase.app/'

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': databaseURL
    })


#Create satellites list
ref = db.reference('Satellites')
ref.set({
    1:{'satellite_name': 'Sentinel-2'},
    2:{'satellite_name': 'Diwata-2'},
    3:{'satellite_name': 'Maya-2'},
    4:{'satellite_name': 'Maya-3'},
    5:{'satellite_name': 'Maya-4'},
    6:{'satellite_name': 'LandSat'}
})

#create countries list
ref = db.reference('Countries')
ref.set({
    1:{'name': 'Philippines', 'continent':'Asia'},
    2:{'name': 'Japan', 'continent':'Asia'},
    3:{'name': 'China', 'continent':'Asia'},
    4:{'name': 'United States of America', 'continent':'North America'},
    5:{'name': 'Singapore', 'continent':'Asia'},
    6:{'name': 'Canada', 'continent':'North America'},
    7:{'name': 'Malaysia', 'continent':'Asia'},
    8:{'name': 'Vietnam', 'continent':'Asia'},
    9:{'name': 'Brunei', 'continent':'Asia'},
    10:{'name': 'Egypt', 'continent':'Africa'}
})

#create users
ref = db.reference('Users')
ref.set({
    1:{
        'username': 'Waynsday',
        'full_name': 'Wayne Akeboshi',
        'created': '17/12/2022',
        'country':2
    },
    2:{
        'username': 'Robert',
        'full_name': 'Robert Kerwin Billones',
        'created': '17/12/2022',
        'country':1
    },
    3:{
        'username': 'Shi',
        'full_name': 'Christalline Jhine Shi',
        'created': '17/12/2022',
        'country':3
    }
})


#Upload optical images data
ref = db.reference('Optical_Images')
for i in range(len(srcfiles)):
    ref.update({
        i+1:{
            'time_taken': '11:59:42',
            'day_taken': '17/12/2022',
            'time_received': '15:43:57',
            'day_received': '18/12/2022',
            'latitude': 121.562,
            'longitude': 11.684,
            'cloud_cover': 0.00,
            'satellite_id': 1,
            'spectral_frequency': 467.43,
            'image_data': srcpath+'/'+srcfiles[i]
        }
    })