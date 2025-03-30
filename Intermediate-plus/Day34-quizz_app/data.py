import requests

endpoint = "https://opentdb.com/api.php"

parameters = {
    "amount": 10,
    "category": 11,
    "difficulty": "easy",
    "type": "boolean",
}

try:
    response = requests.get(url=endpoint, params=parameters)
    response.raise_for_status()

    data = response.json()
    question_data = data["results"]

    # unscaping the characters in each question
    # for item in question_data:
    #     item['question'] = html.unescape(item['question'])

except requests.exceptions.HTTPError as e:
    print(f"Error: {e}")


