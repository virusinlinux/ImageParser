import requests
from bs4 import BeautifulSoup
import os

# specify the URL of the website
url = ""

# send a GET request to the website
response = requests.get(url)

# parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# find all the image tags on the website
image_tags = soup.find_all("img")

# create a directory to store the downloaded images
if not os.path.exists("images"):
    os.makedirs("images")

# download each image and save it in the images directory
for img in image_tags:
    # get the URL of the image
    img_url = img.get("src")

    # check if the URL has a protocol scheme (http:// or https://)
    if not img_url.startswith("http"):
        # if not, add the scheme to the beginning of the URL
        img_url = "https:" + img_url

    # download the image
    img_data = requests.get(img_url).content

    # save the image in the images directory
    with open("images/" + img_url.split("/")[-1], "wb") as f:
        f.write(img_data)
