# In this version I started adding a user interface 
from db_config import func_db_with_blob
import os
import io
import time
import subprocess
from PIL import Image, ImageTk
from tkinter import Tk, Entry, Label, Button, Canvas, PhotoImage, filedialog, simpledialog

# MySQL DB connection
db_with_blob = func_db_with_blob()

# Creating the cursor, and then a MySQL table with a BLOB column containing the images  
my_cursor = db_with_blob.cursor()
my_cursor.execute("CREATE TABLE IF NOT EXISTS Images (image_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, image LONGBLOB NOT NULL, title VARCHAR(20))")


# Defining the function to insert the images into the above created table
def insert_blob(open_file_path):
	with open(open_file_path, 'rb') as file:
		binary_data = file.read()
	SQL_statement = "INSERT INTO Images (image) VALUES (%s)" 
	my_cursor.execute(SQL_statement, (binary_data, ))
	db_with_blob.commit()
	global inserted_id
	inserted_id = my_cursor.lastrowid
	print(f"Image inserted with ID: {inserted_id}")
	

#Fetches the image from the database and puts it into the my_result variable
def fetch_blob(ID):
	SQL_statement2 = "SELECT * FROM Images WHERE image_id = %s"
	my_cursor.execute(SQL_statement2, (str(ID), ))
	my_result = my_cursor.fetchone()[1]
	if my_result:
		return my_result
	else:
		return None

# Save the image in a folder
def save_blob(ID, my_result):
	global save_file_path
	if my_result is None:
		print(f"No image found with this ID:{ID}")
		return	
	if not os.path.exists("image_output"):
		os.makedirs("image_output")
		return
	save_file_path = f"image_output/img{ID}.jpg"	
	with open(save_file_path, 'wb') as file:
		file.write(my_result)

# Function to handle the "Insert Image" button
def insert_image():
	try:
		file_path = filedialog.askopenfilename()
		if file_path:
			insert_blob(file_path)
			my_result = fetch_blob(inserted_id)
			if my_result is not None:
				save_blob(inserted_id, my_result)
				check_image = Image.open(os.path.join("resources", "checkmark-16.png"))
				check_image = check_image.resize((20, 20))
				check_image_tk = ImageTk.PhotoImage(check_image)
				check_label = Label(root, image=check_image_tk)
				check_label.image = check_image_tk
				check_label.grid(row=0, column=1, padx=(10, 0))
			
				script_directory = os.path.dirname(os.path.abspath(__file__))
				saved_here_path = os.path.join(script_directory, save_file_path)
				success_label.config(text=f"Image insertion successful and saved here:{saved_here_path}")
				print(f"Image insertion successful and saved here:{saved_here_path}")
				saved_here_path_dir = os.path.dirname(saved_here_path)
				time.sleep(1)
				subprocess.run(['explorer', saved_here_path_dir.replace('/', '\\')])
				
# if for some reason insertion fails, we get a red x near insert button 	        
	except Exception as e:
		x_image = Image.open(os.path.join("resources", "x-mark-16.png"))
		x_image = x_image.resize((20, 20))
		x_image_tk = ImageTk.PhotoImage(x_image)
		x_label = Label(root, image=x_image_tk)
		x_label.image = x_image_tk
		x_label.grid(row=0, column=1, padx=(10, 0))
		print(f"Image insertion failed. Error: {e}")

# Function to handle the "Display Image" button
# I choose to get the images from the db, not from the file system, so I have to do binary data conversion
def display_image():
	try:
		image_id = simpledialog.askinteger("Image ID", "Enter Image ID:")
		if image_id:
			blob_data = fetch_blob(image_id)
			if blob_data:
				image_stream = io.BytesIO(blob_data)
				image = Image.open(image_stream)
				image_tk = ImageTk.PhotoImage(image)
				image_label = Label(root, image=image_tk)
				image_label.image = image_tk
				image_label.grid(row=1, column=0, padx=10, pady=10)

	except Exception as e:
		print(f"Error displaying image with ID {image_id}: {e}")
		
root = Tk()
root.title("Image Viewer")
canvas = Canvas(root, width=200, height=150)
canvas.grid()

success_label = Label(root, text="")
success_label.grid(row=2, column=0, columnspan=2)

insert_button = Button(root, text="Insert Image", command=insert_image)
insert_button.grid(row=0, column=0, padx=(0, 10), pady=10)

display_button = Button(root, text="Display Image from DB", command=display_image)
display_button.grid(row=1, column=0, padx=(0,10), pady=10)

root.mainloop()
db_with_blob.close()
# -------------------------------------------------------------------------------------------		
