# House Price Prediction API
This project implements a machine learning model to predict house prices based on various input features. The model is trained using Linear Regression on house price data and is deployed as a web application using Flask. This setup provides a practical example of how to transition a model from Python code to a live web API.

# Requirements
This project is developed using Python and Flask. All dependencies are listed in the requirements.txt file.<br><br> Run the following command in the terminal to install the required packages.<br><br>

```
pip install -r requirement.txt
```
<br>
<br>

## Getting Started

To run the application on your local machine, follow these steps:<br><br>
```
python app.py
```
<br>
<br>

## Preview
<img src='https://github.com/MaikarfiJesse/HouseP_MLModel/blob/main/static/images/form.png'></img>
<br>
<br>
<img src='https://github.com/MaikarfiJesse/HouseP_MLModel/blob/main/static/images/prediction.png'></img>
<br>
<br>

## Usage
Once the application is running, you can use it to predict house prices:

    Homepage: Navigate to the homepage (http://localhost:5004). The homepage provides a form to input the house features.
    Predict: After filling out the form with the necessary house attributes (e.g., number of bedrooms, bathrooms, etc.), submit it to see the predicted house price.
<br>
<br>

### Troubleshooting
    Port Already in Use: If you encounter an error stating that the port is already in use, you can specify a different port by modifying the app.run(host='0.0.0.0', port=5004) line in the app.py file.
    Dependencies Not Found: Ensure all dependencies are installed correctly as per the requirements.txt file. If problems persist, try reinstalling the dependencies.
<br>
<br>

## Customization and Feedback
Feel free to fork this repository or send me suggestions to improve the project. Your feedback is valuable as I continue to learn and improve the way I present and manage projects. 
<br>
<br>
