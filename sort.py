# Import needed libs
import shutil
import face_recognition
import os
from PIL import Image, ImageDraw
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askopenfilenames
import pathlib

#Take user input 
def input_array():
    #Ask user for reference photos and return array
    Tk().withdraw()
    filenames = askopenfilenames()
    return filenames
# Compare selected pic to images directory and return true for each matches
def compare_to_images(input_image, compare_image):
    print(f"input  : {input_image}, compare : {compare_image}")
    #Encode the expected face to known format 
    input_face = face_recognition.load_image_file(input_image)
    encoded_input_face = face_recognition.face_encodings(input_face)[0]
    # load comparaison img
    compare_faces = face_recognition.load_image_file(compare_image)
    # compare all faces to expected face and return true if match
    for face_detected in face_recognition.face_encodings(compare_faces):
        result=face_recognition.compare_faces([encoded_input_face], face_detected, 0.6)
        if result[0] == True:
            
            return True, compare_image
    return False

    

# Variables setup
dir=os.getcwd()
input_dir=f"{dir}\source\\"
working_dir=f"{dir}\images\\"

for filename in input_array():
    fname=filename.replace("C:/Users/Krisy/Documents/face_reco/source/", "")
    fname=fname.strip(".jpg")
    output_dir=f"{dir}\saved\\{fname}\\"
    pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
    for image in os.listdir(working_dir):
        split_up = os.path.splitext(image)
        if split_up[1] in ('.jpg', '.JPG', '.jpeg'):
            img = f"{working_dir}{image}"
            result = compare_to_images(filename, img)
            if not result==False:
                output_file=f"{output_dir}{image}"
                shutil.copy(img, output_file)
