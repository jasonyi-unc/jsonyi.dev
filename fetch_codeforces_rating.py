import requests
import json
import yaml
import os

def fetch_codeforces_rating(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            return data['result'][0]['rating']
        else:
            print("Failed to fetch data:", data['comment'])
    else:
        print("Failed to connect to Codeforces API")
    return None

def get_rating_info(rating):
    if rating < 1200:
        return {'title': 'Newbie', 'color': 'grey-color'}
    elif 1200 <= rating <= 1399:
        return {'title': 'Pupil', 'color': 'green-color'}
    elif 1400 <= rating <= 1599:
        return {'title': 'Specialist', 'color': 'cyan-color'}
    elif 1600 <= rating <= 1899:
        return {'title': 'Expert', 'color': 'blue-color'}
    elif 1900 <= rating <= 2099:
        return {'title': 'Candidate Master', 'color': 'purple-color'}
    elif 2100 <= rating <= 2299:
        return {'title': 'Master', 'color': 'orange-color'}
    elif 2300 <= rating <= 2399:
        return {'title': 'International Master', 'color': 'orange-color'}
    elif 2400 <= rating <= 2599:
        return {'title': 'Grandmaster', 'color': 'red-color'}
    elif 2600 <= rating <= 2899:
        return {'title': 'International Grandmaster', 'color': 'red-color'}
    else:
        return {'title': 'Legendary Grandmaster', 'color': 'red-color'}

def write_rating_to_file(rating, rating_info, filename="_data/codeforces_rating.yml"):
    rating_data = {
        'rating': rating,
        'title': rating_info['title'],
        'color': rating_info['color']
    }

    data_directory = os.path.dirname(filename)
    os.makedirs(data_directory, exist_ok=True)  # Ensure the _data directory exists
    
    with open(filename, 'w') as file:
        yaml.dump(rating_data, file)

def load_handle_from_config(filename="assets/json/config.json"):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config['handle']

if __name__ == "__main__":
    handle = load_handle_from_config()
    rating = fetch_codeforces_rating(handle)
    if rating is not None:
        rating_info = get_rating_info(rating)
        write_rating_to_file(rating, rating_info)
        print(f"Rating {rating} ({rating_info['title']}) written to file")
    else:
        print("Failed to fetch or write rating")