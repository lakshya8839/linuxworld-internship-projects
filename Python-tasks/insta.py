from instagrapi import Client

cl = Client()
cl.login("chalana2004_", "Chalana_2004")

cl.photo_upload(
    path=r"C:\Users\lakshya\Documents\images\lakshya.jpg",
    caption="Hello,Its an post created by me by python automatically"
)
