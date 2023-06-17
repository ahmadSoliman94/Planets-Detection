# Planets Detection

## Dataset: 
### The dataset is composed of 2 folders:
- train: 2497 images
- validation: 232 images
- test: 128

### The dataset contains 8 classes:
- Earth
- Jupiter
- Mercury
- Neptune
- Saturn
- Uranus
- Venus

### Model:
- YOLOv8

### Training:
- 30 epochs
- Batch size: 16
  

### Results:

#### Loss:
![1](images/results.png)

<br />

#### PR Curve:
![2](images/PR_curve.png)

<br />

#### Confusion Matrix:
![3](images/confusion_matrix_normalized.png)

<br />

#### Predictions:
![4](images/video.gif)


## Deployment:
### The model is deployed on Streamlit.