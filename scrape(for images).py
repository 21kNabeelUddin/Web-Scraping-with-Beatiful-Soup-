from bs4 import BeautifulSoup
import requests
import os

# Base URL for dog breeds
base_url = 'https://bowwowinsurance.com.au/dogs/dogs-breeds/page/'

# Directory to save the images
output_dir = 'dog_breeds_images'
os.makedirs(output_dir, exist_ok=True)

# Loop through all pages (assuming 11 pages)
for page in range(1, 12):  # Adjust range based on the total number of pages
    print(f"Scraping page {page}...")
    response = requests.get(f'{base_url}{page}/')
    soup = BeautifulSoup(response.text, 'lxml')

    # Find all breed boxes on the page
    for breed_box in soup.find_all('div', class_='col-md-4 col-sm-6 col-xs-12'):
        # Extract the breed name
        try:
            breed_name = breed_box.find('h3', class_='tit').text.strip()
        except (AttributeError, TypeError):
            breed_name = "Unknown_Breed"

        # Extract the image URL
        try:
            img_tag = breed_box.find('img', class_='img-responsive')
            img_url = img_tag['src'] if img_tag else None
        except (AttributeError, TypeError):
            img_url = None

        # Download the image if URL is available
        if img_url:
            try:
                # Create a valid filename for the breed
                breed_filename = breed_name.replace(' ', '_').replace('/', '_') + '.jpg'
                img_path = os.path.join(output_dir, breed_filename)

                # Download the image
                img_data = requests.get(img_url).content
                with open(img_path, 'wb') as img_file:
                    img_file.write(img_data)
                print(f"Downloaded: {breed_name} -> {img_path}")
            except Exception as e:
                print(f"Failed to download image for {breed_name}: {e}")

print("Scraping complete. Images saved in the 'dog_breeds_images' folder.")
