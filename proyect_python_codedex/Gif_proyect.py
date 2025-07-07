import imageio.v3 as iio

filenames = ['images\chicklet1.png', 'images\chicklet2.png', 'images\chicklet3.png', 'images\chicklet4.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))
  
  iio.imwrite('resukt_littleChicken.gif', images, duration = 200, loop = 0)
  
  

filenames2 = ['images\dino1.png', 'images\dino2.png', 'images\dino3.png', 'images\dino4.png']
images2 = [ ]

for filename2 in filenames2:
  images2.append(iio.imread(filename2))
  
  iio.imwrite('resukt_littleDino.gif', images2, duration = 200, loop = 0)
  
  
filenames3 = ['images\hippocorn1.png', 'images\hippocorn2.png', 'images\hippocorn3.png', 'images\hippocorn4.png']
images3 = [ ]

for filename3 in filenames3:
  images3.append(iio.imread(filename3))
  
  iio.imwrite('resukt_littleHipocorn.gif', images3, duration = 200, loop = 0)