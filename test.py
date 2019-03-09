from cartpolar import *
import matplotlib.pyplot as plt

img_dir = 'data/sample_img.png'
gt_dir = 'data/sample_gt.txt'
img = plt.imread(img_dir)
gt = np.loadtxt(gt_dir, delimiter=',')
phy_radius = 0.5*np.sqrt(np.average(np.array(img.shape)**2)) -1
cartpolar = CartPolar(np.array(img.shape)/2., phy_radius, 256, 128)
polar_img = cartpolar.img2polar(img)
polar_gt = cartpolar.gt2polar(gt)
print(polar_img.shape, polar_gt.shape)
plt.imshow(polar_img, cmap='gray')
plt.plot(polar_gt, 'r_')
plt.savefig('data/sample_polar_img_gt.png', dpi=100, bbox_inches='tight')
plt.show()
cart_gt = cartpolar.gt2cart(polar_gt)
print(cart_gt[0].shape)
plt.imshow(img, cmap='gray')
plt.plot(cart_gt[0], cart_gt[1], 'r-')
plt.show()