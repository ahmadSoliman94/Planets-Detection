import cv2
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def show_images(dataframe, num_images,num_rows, num_cols):
    # Randomly select 20 indices from the train_df DataFrame
    random_indices = random.sample(range(len(dataframe)), num_images)

    # Create a figure and subplots
    fig, ax = plt.subplots(num_rows, num_cols, figsize=(10, 5))

    # Iterate over the randomly selected indices
    for i, random_idx in enumerate(random_indices):
        row = dataframe.loc[random_idx]
        images = row['Image Path']
        labels = row['Class Name']

        # Read the image file specified by 'image_path' using OpenCV
        image = cv2.imread(images)

        # Convert the color space of the image from BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Determine the row and column indices for the subplot
        row_idx = i // 5
        col_idx = i % 5

        # Set the title for the subplot
        ax[row_idx, col_idx].set_title(labels)

        ax[row_idx, col_idx].axis('off')
        # Display the image in the subplot
        ax[row_idx, col_idx].imshow(image)

    plt.tight_layout()
    plt.show()
