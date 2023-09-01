import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from moviepy.editor import VideoFileClip
import urllib
import pyrebase
import datetime
from firebase_admin import storage
import os
import firebase_admin
from firebase_admin import credentials, storage

firebaseConfig = {
    'apiKey': "AIzaSyB-ygNPo0YW2FR0K8d56ZKPmaCX3peJjp0",
    'authDomain': "experiment-f3951.firebaseapp.com",
    'projectId': "experiment-f3951",
    'storageBucket': "experiment-f3951.appspot.com",
    'messagingSenderId': "866298631498",
    'appId': "1:866298631498:web:3dfdbbc6c74b6bf684ddb3",
    'databaseURL': ""
}


# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'experiment-f3951.appspot.com'
})
db = firestore.client()


# Initialize Firebase Storage
firebase = pyrebase.initialize_app(firebaseConfig)
storag = firebase.storage()

# Function to delete a local file


def delete_local_file(file_path):
    try:
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    except OSError as e:
        print(f"Error deleting {file_path}: {e}")


x = 1
docs = db.collection('videos').get()

for doc in docs:
    print(f"doc :  {doc}")
    # cU2jfvusnno6PU18fU1D
    data = doc.to_dict().get('url')
    print(f"data :  {data}")
    print(f"id : {doc.id}")
    print("duration")
    print(VideoFileClip(data).duration)
    if (VideoFileClip(data).duration!=240.12):
      break
    
    if data:
        try:
            clip1 = VideoFileClip(data).subclip(0, 7)
            clip1.write_videofile(f"clip{x}.mp4")
            cloudfilename = 'neutral/' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
            storag.child(cloudfilename).put(f"clip{x}.mp4")

            # Delete the local file
            delete_local_file(f"clip{x}.mp4")

            x += 1
            # Process the video and upload clips
            clip1 = VideoFileClip(data).subclip(8, 31)
            clip1.write_videofile(f"clip{x}.mp4")
            cloudfilename = 'happy/' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
            storag.child(cloudfilename).put(f"clip{x}.mp4")

            # Delete the local file
            delete_local_file(f"clip{x}.mp4")

            x += 1
#-------------------------------------------------
            clip2 = VideoFileClip(data).subclip(31, 41)
            clip2.write_videofile(f"clip{x}.mp4")
            cloudfilename = 'fhappy/' + \
                datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
            storag.child(cloudfilename).put(f"clip{x}.mp4")

            # Delete the local file
            delete_local_file(f"clip{x}.mp4")

            x += 1
#-----------------------------------------------------
            clip2 = VideoFileClip(data).subclip(49, 71)
            clip2.write_videofile(f"clip{x}.mp4")
            cloudfilename = 'sad/' + \
                datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
            storag.child(cloudfilename).put(f"clip{x}.mp4")

            # Delete the local file
            delete_local_file(f"clip{x}.mp4")

            x += 1
#--------------------------------------------------------            
            clip2 = VideoFileClip(data).subclip(72, 80)
            clip2.write_videofile(f"clip{x}.mp4")
            cloudfilename = 'fsad/' + \
                datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
            storag.child(cloudfilename).put(f"clip{x}.mp4")

            # Delete the local file
            delete_local_file(f"clip{x}.mp4")

            x += 1

#--------------------------------------------------------                  
            clip2 = VideoFileClip(data).subclip(88, 111)
            clip2.write_videofile(f"clip{x}.mp4")
            cloudfilename = 'surprised/' + \
                datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
            storag.child(cloudfilename).put(f"clip{x}.mp4")

            # Delete the local file
            delete_local_file(f"clip{x}.mp4")

            x += 1

#--------------------------------------------------------                  
            clip2 = VideoFileClip(data).subclip(112, 121)
            clip2.write_videofile(f"clip{x}.mp4")
            cloudfilename = 'fsurprised/' + \
                datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
            storag.child(cloudfilename).put(f"clip{x}.mp4")

            # Delete the local file
            delete_local_file(f"clip{x}.mp4")

            x += 1

#--------------------------------------------------------                  
            clip2 = VideoFileClip(data).subclip(129, 151)
            clip2.write_videofile(f"clip{x}.mp4")
            cloudfilename = 'angry/' + \
                datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
            storag.child(cloudfilename).put(f"clip{x}.mp4")

            # Delete the local file
            delete_local_file(f"clip{x}.mp4")

            x += 1

#--------------------------------------------------------                  
            clip2 = VideoFileClip(data).subclip(152, 159)
            clip2.write_videofile(f"clip{x}.mp4")
            cloudfilename = 'fangry/' + \
                datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
            storag.child(cloudfilename).put(f"clip{x}.mp4")

            # Delete the local file
            delete_local_file(f"clip{x}.mp4")

            x += 1

#--------------------------------------------------------      
            clip2 = VideoFileClip(data).subclip(168, 190)
            clip2.write_videofile(f"clip{x}.mp4")
            cloudfilename = 'disgusted/' + \
                datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
            storag.child(cloudfilename).put(f"clip{x}.mp4")

            # Delete the local file
            delete_local_file(f"clip{x}.mp4")

            x += 1
            

#--------------------------------------------------------         
            clip2 = VideoFileClip(data).subclip(191, 199)
            clip2.write_videofile(f"clip{x}.mp4")
            cloudfilename = 'fdisgusted/' + \
                datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
            storag.child(cloudfilename).put(f"clip{x}.mp4")

            # Delete the local file
            delete_local_file(f"clip{x}.mp4")

            x += 1
                     
            clip2 = VideoFileClip(data).subclip(208, 230)
            clip2.write_videofile(f"clip{x}.mp4")
            cloudfilename = 'scared/' + \
                datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
            storag.child(cloudfilename).put(f"clip{x}.mp4")

            # Delete the local file
            delete_local_file(f"clip{x}.mp4")

            x += 1
            
#-----------------------------------------------------------           
            clip2 = VideoFileClip(data).subclip(231, 239)
            clip2.write_videofile(f"clip{x}.mp4")
            cloudfilename = 'fscared/' + \
                datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
            storag.child(cloudfilename).put(f"clip{x}.mp4")

            # Delete the local file
            delete_local_file(f"clip{x}.mp4")

            x += 1
            
            # Delete the file reference from Firebase Storage
            try:
                # Create a reference to the file you want to delete
                s = doc.to_dict().get('Fname')
                file_ref = storage.bucket().blob(f'videos/{s}')
                # Delete the file
                file_ref.delete()
                doc_ref = db.collection('videos').document(doc.id)
                doc_ref.delete()
                print(f"{data} has been deleted from Firebase Storage.")
            except Exception as e:
                print(f"Error deleting {data} from Firebase Storage: {e}")
        except Exception as e:
            print(f"Error processing video: {e}")

          # Exit the loop after processing the first document
