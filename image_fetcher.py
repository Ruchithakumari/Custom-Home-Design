import requests

def fetch_image_from_lexica(style):
    lexica_url = f"https://lexica.art/api/search?q={style} home"
    response = requests.get(lexica_url)

    if response.status_code == 200:
        data = response.json()
        if "images" in data and len(data["images"]) > 0:
            return data["images"][0]["src"]  # Get first image URL
        else:
            return None  # No images found
    else:
        return None  # API request failed
