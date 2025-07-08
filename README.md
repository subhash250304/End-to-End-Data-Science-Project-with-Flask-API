# End-to-End-Data-Science-Project-with-Flask-API
campany:codtech it solutions
name:sunkenapllay subhash
Intern ID :CT06DF414 
domain:data science
mentor:neela santhosh
duration:45 days 
CODTECH AI Internship Tasks: A GitHub Repository
Overview description :  End-to-End Data Science Project with Flask API
TASK 3: End-to-End Data Science Project with Flask Deployment

Task 3 focused on integrating multiple components of a data science project into a cohesive pipeline, culminating in a deployed web application using Flask. The objective was to build a model, deploy it through a web API, and showcase its functionality with real-time predictions.

The process began with collecting and preprocessing a structured dataset. I used a synthetic dataset simulating customer purchase decisions based on features like age, salary, and city. Data preprocessing involved handling missing values, scaling numeric data, and encoding categorical variables using Scikit-learn's pipeline tools.

Next, I trained a logistic regression model using Scikit-learn. The model was trained to classify whether a customer would purchase a product based on the provided features. After evaluating the model's accuracy and verifying its predictions, I serialized it using Python’s pickle module, saving the trained pipeline to a .pkl file.

The core of this task was deploying the trained model as a RESTful API using Flask. I created an app.py file that defined two routes: a root route for status checking and a /predict route for making predictions. The Flask app loaded the pickled model, accepted JSON input via POST requests, and returned predictions in real-time. This allowed the model to serve predictions without requiring re-training or direct interaction with the training script.

To test the API, I used tools like Postman and curl commands to send sample inputs and receive predictions. The application successfully responded with correct outputs, demonstrating that the entire pipeline—from data preprocessing and model training to deployment—was functioning as intended.

This task was a significant learning experience in deploying machine learning models. It demonstrated how to bridge the gap between data science development and real-world application. By the end of the task, I had built a complete, functional web service capable of delivering ML predictions in real-time, simulating how ML models are deployed in industry.
output:<img width="198" height="93" alt="Image" src="https://github.com/user-attachments/assets/ebae6e8b-3146-41bb-9f66-72792e3b6537" />
