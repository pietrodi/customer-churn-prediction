# Customer Churn Prediction

## The problem - predicting customer churn

As stated on [Wikipedia](https://en.wikipedia.org/wiki/Customer_attrition):
> Customer attrition, also known as customer churn [...] is the loss of clients or customers.
>
> Banks, telephone service companies, Internet service providers, pay TV companies, insurance firms, and alarm monitoring services, often use customer attrition analysis and customer attrition rates as one of their key business metrics (along with cash flow, EBITDA, etc.) because the cost of retaining an existing customer is far less than acquiring a new one. Companies from these sectors often have customer service branches which attempt to win back defecting clients, because recovered long-term customers can be worth much more to a company than newly recruited clients.
>
> [...] 
>
> Current organizations face therefore a huge challenge: to be able to anticipate to customers’ abandon in order to retain them on time, reducing this way costs and risks and gaining efficiency and competitivity.

Therefore, the objective of this project is to develop and turn into a web service a machine learning model for a classification problem: predicting whether a customer of a company will churn or not. In particular, the modelling and training is done on the case of a bank and the model is served using Flask.

### Data

The data used for this project is from Kaggle and can be found [here](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling). The dataset contains details of a bank's customers and the target variable is a binary variable reflecting the fact whether the customer left the bank (closed his account) or he continues to be a customer.

## Navigating the project repository

- **Data**  
    [This folder](./data/) contains [customer-data.csv](./data/customer-data.csv), the dataset used for the project.

- **Notebooks**  
    [This folder](./notebooks/) contains [customer_churn_prediction.ipynb](./notebooks/customer_churn_prediction.ipynb), a copy of the Google Colab notebook used to do the analysis and model selection. In the notebook I first analyzed and processed the data available for better accuracy and to prevent overfitting. Then, I trained multiple models tuning several of their parameters to find the best performing among them. In the end, I did a last evalutation among the best models in order to find the final model.

- **Flaskapp**  
    [This folder](./flaskapp/) contains the code for the flask websever. The [scripts](./scripts/) folder contains [train.py](./scripts/train.py), which trains and saves the model used for prediction, [prepare_data.py](./scripts/prepare_data.py), which prepares training and prediction data for the model, and [request.py](./scripts/prepare_data.py), which is used to send a test request to the app. [predict.py](.flaskapp/predict.py) contains the function which returns a prediction upon receiving a post request with customer information. The [README](./flaskapp/README.md) contains information on how to run the app.