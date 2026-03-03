from instagrapi import Client

cl = Client()
cl.login("Your_insta_id", "Your_password")  # Replace with actual credentials

media = cl.album_upload(
    paths=[
        r"C:\Users\lakshya\Documents\images\1.jpg",
        r"C:\Users\lakshya\Documents\images\2.jpg"
    ],
    caption="My carousel post with two photos"
)
print("Post uploaded successfully:", media.dict())
