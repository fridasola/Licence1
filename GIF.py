import imageio.v3 as iio
from PIL import Image

filenames = ['HK1.png', 'HK2.png']
images = []

# Définir une taille
target_size = (500, 500) 

for filename in filenames:
    # On ouvre l'image avec Pillow pour la redimensionner et la convertir en RGB
    img = Image.open(filename).convert('RGB').resize(target_size)
    images.append(img)

# Sauvegarder le GIF
iio.imwrite('team.gif', images, loop=0)