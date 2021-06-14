# Draw faces 
# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(newPic)
# Create a PIL imagedraw object so we can draw on the picture
pil_image = Image.fromarray(newPic)
d = ImageDraw.Draw(pil_image)
for face_landmarks in face_landmarks_list:
    # Let's trace out each facial feature in the image with a line!
    for facial_feature in face_landmarks.keys():
        d.line(face_landmarks[facial_feature], width=5)
# Show the picture
file_name_dest=file_name.replace('images/', 'saved/')
saved = pil_image.save(f"{output_folder}/{img}") 
