import os
from PIL import Image
from torch.utils.data import Dataset


class ImageDataset(Dataset):
    def __init__(self, root_dir, listdir=None, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        if listdir is None:
            self.file_list = os.listdir(root_dir)
        else:
            self.file_list = listdir

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, self.file_list[idx])
        image = Image.open(img_name).convert('RGB')

        if self.transform:
            image = self.transform(image)

        return image


class TestDataset(Dataset):
    def __init__(self, root_dir, images_folder_name, annotations_name, transform=None):
        self.images_dir = os.path.join(root_dir, images_folder_name)
        self.annotations_path = os.path.join(root_dir, annotations_name)
        self.transform = transform
        self.file_list = os.listdir(self.images_dir)

        with open(self.annotations_path) as f:
            labels = {}
            for line in f.readlines():
                filename, label = line.split()
                labels[filename] = int(label)

        self.labels = labels

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        img_name = os.path.join(self.images_dir, self.file_list[idx])
        image = Image.open(img_name).convert('RGB')

        if self.transform:
            image = self.transform(image)

        label = self.labels[self.file_list[idx]]

        return image, label
