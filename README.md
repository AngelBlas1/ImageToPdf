# ImageToPdf
Construir una API en Python que permita a un usuario: Subir una imagen (JPG). Convertir la imagen en PDF. Almacenar el PDF en Firebase Storage. Guardar la información del usuario (nombre, correo, y referencia al archivo en Firebase) en Firestore. Aplicar los principios SOLID para garantizar modularidad, escalabilidad y mantenibilidad.

## Uso
In my case I created a virtual environment and used uvicorn to run the api.


## #1
Create the necessary folders and files.

## #2
create a virtual environment, so as not to change global settings of the visual environment

## #3
In image_controller.py we create a router that will have the API requests, in this case it is only of type Post for obtaining data and in main.py we include that router with the request routes.

## #4
A function is created in Image_service that is responsible for analyzing the data obtained in the request and tries to convert the images to pdf using another function from another file.

## #5
Now it is necessary to create the interfaces that save the user data and allow obtaining the file that will be uploaded to Firebase.

## #6
We added the code provided by firebase and modified it to make it more secure in the use of credentials

## #7 
Created the FirebaseRepository class in order to use the interface made previously, and use the functions to upload it to the firebase database and obtain the firestore link

## #8 
Modified the image_service file so that it can use the StorageInterface functions in the FirestoreRepository class. At this point you are able to convert an image to a pdf file.

## Extra commit
I realized that in the previous commit where I could already upload and convert the image to pdf in Firebase, in image_service the init function depended specifically on the FirestoreRepository, so why not the repository parameter would be managed from image_controler, in this way large changes would be avoided and allowing the use of other storages.