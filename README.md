
# LFW dataset classification 🖼️

This is a project where I have used many Scikit-learn classification algorithms on the Faces labeled on the wild (FLW) dataset

## Goal 🎯
The goal of this project is to answer the question **Which machine learning classifcation algorithm(s) can fit the FLW data with the highest posssible accuracy score?**

## Technologies 🛠️
- **Python**
- **pandas**
- **scikit-learn**

## Tested algorithms 🧠
- **Gaussian Naive Bayes (GaussianNB)**
- **Decision tree classifier**
- **K-nearest neighbors (KNN)**
- **Support vector machine classifier (SVC)**

## Folder Structure 📁
```
/project-root
│
├── /.venv                 # Virtual environment with all required dependencies
├── /models                # Saved models, one for each algorithm
├── /notebooks             # Jupyter notebook for evaluation 
├── /src                   # Source code for loading and training data
├── requirements.txt       # Python dependencies
└── README.md              # This README file
```

## Installation 🔧
1. Clone this repository:
   ```bash
   git clone https://github.com/Amira-Bekhta/lfw_classifier.git 
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Findings 💉
- **Classifier**: Decision tree classifier
   - **Accuracy Score**: 0.89

- **Classifier**: Gausian Naive Bayes
   - **Accuracy Score**: 0.55

- **Classifier**: K-nearest neighbor classifier
   - **Accuracy Score**: 0.63

- **Classifier**: Support vector machine classifier
   - **Accuracy Score**: 0.93
   
## Explanation 🛰️
- SVC has scored best because of its flexibility with high-dimensional data such as image data, the decision tree classifier has scored good too because of its non-linear boundaries.
- KNN has scored relatively bed because of the high-dimensionality and also because of the lack of feauture engineering, since KNN relies heavily on meaningful ditances.
- Finally, Naive bayes algorithm is one that assumes that features are conditionally independent, which is rarely true in image data


## Dataset 📊
This project uses the [Spam Email Dataset](https://vis-www.cs.umass.edu/lfw/).