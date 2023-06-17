
import os
import pandas as pd

def create(root_dir):

    image_paths = []
    label_paths = []
    class_names = []

    # Iterate through the images folder
    for root, dirs, files in os.walk(os.path.join(root_dir, "images")):
        for file in files:
            if file.endswith(".jpg"):  # Assuming the images are in JPEG format
                image_path = os.path.join(root, file)
                label_path = os.path.join(root_dir, "labels", file.replace(".jpg", ".txt"))  # Assuming the labels have the same name as the corresponding image but with a .txt extension
                image_paths.append(image_path)
                label_paths.append(label_path)
                
                # Extract the class name from the image path
                class_name = os.path.basename(image_path).split("-")[0]
                class_names.append(class_name)
                

    # Create a dataframe
    data = pd.DataFrame({'Image Path': image_paths, 'Label Path': label_paths, 'Class Name': class_names})

    # Save the dataframe to a CSV file
    data.to_csv('df.csv', index=False)

