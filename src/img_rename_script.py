import os


def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


i = 0
for file in files("../img_second_dataset/"):
    if "IMAGE" in file:
        num = str(i)
        num = num.zfill(3)
        os.rename("../img_second_dataset/" + file, f"../img_second_dataset/scene_{num}.jpg")
        i = i + 1
