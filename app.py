from flask import Flask, render_template
import requests

app = Flask(__name__)

# Define the route for displaying the user data
@app.route('/')
def display_users():
    # Make an API call to ReqRes to get user data
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    data = response.json().get('data', [])  # Extract the 'data' field

    # Prepare the data for rendering in the template
    user_list = []
    for user in data:
        user_info = {
            'id': user['id'],
            'email': user['email'],
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'avatar': user['avatar'],
        }
        user_list.append(user_info)

    return render_template('users.html', users=user_list)

if __name__ == '__main__':
    app.run(debug=True)
