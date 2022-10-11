import requests

"""
This script is used for sending a sample request to test the app.
"""

LOCAL_URL = 'http://localhost:9696/predict'
SAMPLE_CUSTOMER = {
    'CustomerId': 83131903810,
    'Surname': 'White',
    'CreditScore': 630,
    'Geography': 'Spain',
    'Gender': 'Female',
    'Age': 55,
    'Tenure': 2,
    'Balance': 223111.10,
    'NumOfProducts': 1,
    'HasCrCard': 1,
    'IsActiveMember': 0,
    'EstimatedSalary': 80100.77
}

def send_request(json, url):
    """
    Sends a json in a post request to the
    specified url and returns the json response.

    Args:
        json: The json request
        url: The url to send the request to

    Returns:
        The json response to the request
    """
    return requests.post(url, json = json).json()

if __name__ == "__main__":
    print(send_request(SAMPLE_CUSTOMER, LOCAL_URL))