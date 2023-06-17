import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




def show_class_distributaion(df):
   
    """ 
    This function shows the class distribution of a dataframe
    Parameters:
    df (dataframe) : A data frame with two columns, one for target and other is features
    """
    
    # Create a figure with a specified size
    fig, ax = plt.subplots()
    ax.pie(df['Class Name'].value_counts(), labels=df['Class Name'].unique(), autopct='%1.1f%%')
 

    # Set custom labels for the x-axis and y-axis
    plt.title('Palanet Names')


    # Display the plot
    plt.show()