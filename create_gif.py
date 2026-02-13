import imageio.v3 as iio
filenames = ['rest.png', 'Kame1.png','Kame2.png','Haaaa.png']
images = [ ]
for filename in filenames:
  images.append(iio.imread(filename))
  iio.imwrite('Kame_Kame_haaaaa.gif', images, duration = 500, loop = 0)
