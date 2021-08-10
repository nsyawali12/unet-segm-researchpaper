# def open_image(path, width, height):
#     try :
#         image = cv2.imread(path)
#         image = cv2.resize(image, (width, height))
#         return image
#     except:
#         return []


# Index File ada berapa?
# 92
import numpy as np

def open_image(path, width, height):
    if (np.random.rand() > 0.5):
        return []
    else:
        return ["aya boy"]

image_healthy_left = "/content/drive/MyDrive/glaucoma_research/RIM-ONE-r3/dataset_v2/healthy/healthy_stereo/N-%s-L.jpg"
image_healthy_right = "/content/drive/MyDrive/glaucoma_research/RIM-ONE-r3/dataset_v2/healthy/healthy_stereo/N-%s-R.jpg"
dataset_path = "/content/drive/MyDrive/glaucoma_research/RIM-ONE-r3/dataset_v2/"
glaucoma_path = dataset_path + "glaucoma_suspect/glaucoma_stereo/"

image_glaucoma_left = glaucoma_path + "G-%d-L" + "*.jpg"
image_glaucoma_right = glaucoma_path + "G-%d-R" + "*.jpg"

dataset_path = "/content/drive/MyDrive/glaucoma_research/RIM-ONE-r3/dataset_v2/"
healthy_path = dataset_path + "healthy/healthy_stereo/"
healthy_masked_path = dataset_path + "healthy/avg_healthy_mask/"
glaucoma_path = dataset_path + "glaucoma_suspect/glaucoma_stereo/"
glaucoma_masked_path = dataset_path + "glaucoma_suspect/glaucoma_suspect_avg_mask/"

masked_healthy_disc = glaucoma_masked_path + "N-%d-%s-Disc-Avg.png"
masked_healthy_cup = glaucoma_masked_path + "N-%d-%s-Cup-Avg.png"

width = 256
height = 256

# sample_data = {
#     "index" : 1
#     "normal" : {
#         "left" : "hasil",
#         "right" : "hasil"
#     },
#     "glaucoma" : {
#         "left" : "hasil",
#         "right" : "hasil"
#     }
# }

healthy_list = []
masked_healthy_cup_list = []
masked_healthy_disc_list = []


for i in range(1, 92):
    healthy_left = open_image(image_healthy_left % i, width, height)
    healthy_right = open_image(image_healthy_right % i, width, height)
    if (len(healthy_left) > 0):
        healthy_list.append(healthy_left)
        masked_healthy_disc_left = open_image(masked_healthy_disc % (i, "L"), width, height)
        masked_healthy_disc_list.append(masked_healthy_disc_left)
        masked_healthy_cup_left = open_image(masked_healthy_cup % (i, "L"), width, height)
        masked_healthy_cup_list.append(masked_healthy_cup_left)
    elif(len(healthy_right) > 0):
        healthy_list.append(healthy_right)
        masked_healthy_disc_right = open_image(masked_healthy_disc % (i, "R"), width, height)
        masked_healthy_disc_list.append(masked_healthy_disc_right)
        masked_healthy_cup_right = open_image(masked_healthy_cup % (i, "R"), width, height)
        masked_healthy_cup_list.append(masked_healthy_cup_right)

print(healthy_list)
print(masked_healthy_cup_list)
print(masked_healthy_disc_list)


print(len(healthy_list), len(masked_healthy_cup_list), len(masked_healthy_disc_list))
    



# for path in healthy432:
#   print(path)
#   if (path == image_healthy_left):
#     image = cv2.imread(path)
#     image = cv2.resize(image, (width, height))
#     list_img_stereo_left.append(image)
#   elif (path == image_healthy_right):
#     image = cv2.imread(path)
#     image = cv2.resize(image, (width, height))
#     list_img_stereo_right.append(image)
#   # list_img_stereo.append(image)
