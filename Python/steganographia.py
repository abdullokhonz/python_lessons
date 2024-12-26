from stegano import lsb

secret = lsb.hide('imgs/image.jpg', 'It\'s Cat!')
secret.save('imgs/image_secret.jpg')

result = lsb.reveal("imgs/image_secret.jpg", )
print(result)
