# Breast-Cancer-Prediction-Model-using-Machine-Learning

This project implements a machine learning model to predict whether a breast tumor is malignant or benign based on a set of features extracted from the digital images of breast mass

## Introduction 

This report is based on a dataset consisting of information about breast cancer diagnosis. The dataset contains 33 columns and 569 rows, with each row representing a patient and each column representing a different feature of the patient's diagnosis. The first column contains a unique identifier for each patient, while the second column contains information about whether the patient's diagnosis was malignant (M) or benign (B).

The following columns contain numerical data about various physical characteristics of the tumor, such as radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave points_mean, and so on. These features are calculated from images of the tumor that were taken using digital mammography.

The last column, Unnamed: 32, is empty and does not contain any data. So it was dropped from dataset. 

# Project Report 

The objective of this project is to analyze the dataset and build a machine learning model to predict whether a breast cancer diagnosis is malignant or benign based on the physical characteristics of the tumor.

# Data Description 

The Dataset contains the following columns. 

- **id** : An unique identifier for each patient 
- **diagnosis** : Whether the diagnosis is malignant(M) or benign (B) 
- **radius_mean** : Mean of distances from center to points on the perimeter 
- **texture_mean** : Standard deviation of gray-scale values 
- **perimeter_mean** : Perimeter of the tumour 
- **area_mean** : Area of the tumour 
- **smoothness_mean** : Local variations in radius lengths
- **compactness_mean** : Perimeter^2 / area - 1.0
- **concavity_mean** : Severity of the concave portions of the contour
- **concave points_mean** : Number of concave portions of the contour
- **symmetry_mean** : Symmetry of the tumour
- **fractal_dimension_mean** : "Coastline approximation" - 1 
- **radius_se** : Standard error of mean distances from center to points on the perimeter
- **texture_se** : Standard error of gray-scale values 
- **perimeter_se** : Standard error of perimeter
- **area_se** : Standard error of area
- **smoothness_se** : Standard error of local variation in radius lengths 
- **compactness_se** : Standard error of Perimeter^2 / area - 1.0
- **concavity_se** :  Standard error of severity of concave portions of the contour
- **symmetry_se** : Standard error for symmetry of tumour
- **fractional_dimension_se** : Standard error for "coastline approximation" - 1
- **radius_worst** : "Worst" or largest mean value for mean of distances from center to points on the perimeter
- **texture_worst** : "Worst" or largest mean value for standard deviation of gray-scale values
- **perimeter_worst** : "Worst" or largest mean value for perimeter
- **area_worst** : "Worst" or largest mean value for area
- **smoothness_worst** : "Worst" or largest mean value for local variation in radius lengths
- **compactness_worst** : "Worst" or largest mean value for perimeter^2 / area - 1.0
- **concavity_worst** : "Worst" or largest mean value for severity of concave portions of the contour
- **concave_points_worst** : "Worst" or largest mean value for number of concave portions of the contour
- **symmetry_worst** : "Worst" or largest mean value for symmetry of tumor
- **fractional_dimension_worst** : "Worst" or largest mean value for "coastline approximation" - 1
- **Unnamed: 32** : An empty column that can be dropped from the dataset.

