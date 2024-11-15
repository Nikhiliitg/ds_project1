End-to-End ML Pipeline for Predictive Modeling with DagsHub, MLflow, and Flask

This project is an end-to-end machine learning pipeline designed for predictive modeling, with full version control for data, code, and model artifacts. Using DagsHub and MLflow for tracking and managing versions, this solution includes model deployment through a scalable Flask API, enabling real-time predictions and integration with other applications.

Features

Data and Model Versioning: Comprehensive version tracking for data, code, and models using DagsHub and MLflow.

ElasticNet Model: Implements ElasticNet for model training, balancing between Ridge and Lasso regression to manage multicollinearity.

Experiment Tracking: Utilizes MLflow to log and compare model parameters, metrics, and artifacts.

Real-Time Prediction API: Deploys the trained model with Flask, providing a scalable API for live predictions.

Reproducible and Scalable Pipeline: Modular design allows easy extension, scalability, and reproducibility.


Project Workflow

1. Data Ingestion and Preprocessing

Raw data is ingested and preprocessed for model training.

Data is versioned using DagsHub, allowing reproducibility and tracking of changes.



2. Model Training

Trains an ElasticNet model to balance regularization and improve predictive accuracy.

MLflow is used for tracking experiments, capturing hyperparameters, metrics, and performance results.



3. Model Evaluation

Evaluates the model using metrics such as MSE, R2 Score, and MAE to ensure optimal performance.



4. Model Deployment

The best-performing model is saved and deployed as a Flask API, providing endpoints for real-time prediction.



5. API Integration

The Flask API is ready for integration with external applications, allowing clients to send data and receive predictions in real time.




Technical Stack

Programming Language: Python

Machine Learning Model: ElasticNet (for balance between Lasso and Ridge regression)

Experiment Tracking and Versioning: DagsHub, MLflow

Deployment Framework: Flask (providing a lightweight and scalable web API)


Installation

1. Clone the repository:

git clone https://github.com/yourusername/MLPipelineProject.git
cd MLPipelineProject


2. Install dependencies:

pip install -r requirements.txt


3. Set up environment variables for DagsHub, MLflow, and any database configurations by adding them to a .env file:

DAGSHUB_URI="your_dagshub_uri"
MLFLOW_TRACKING_URI="your_mlflow_tracking_uri"



Usage

1. Training the Model

Run the training script to preprocess data, train the ElasticNet model, and log experiments to MLflow:

// python main.py



2. Launching the API

Deploy the model with Flask:

//python app.py



3. Making Predictions

Send POST requests to the API endpoint with the required input format to receive predictions.

## Contributing

Contributions are welcome! Please fork the repository, make your updates, and submit a pull request.
