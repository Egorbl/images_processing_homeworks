import torchvision.transforms as transforms
import torch
import torchvision
import random

transform = transforms.Compose([
     transforms.ToTensor(),
     transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2112, 0.2086, 0.2121))
     ])


def get_cifar_train_loader(batch_size: int, size: float = 1):
    train_data = torchvision.datasets.CIFAR10(root="train/", train=True,
                                              download=True, transform=transform)
    if size == 1:
        used_data = range(0, len(train_data), 1)
    elif size == 0.5:
        used_data = range(0, len(train_data), 2)
    elif size == 0.1:
        used_data = range(0, len(train_data), 10)
    else:
        raise ValueError
    train_data_1 = torch.utils.data.Subset(train_data, used_data)
    train_loader = torch.utils.data.DataLoader(train_data_1, batch_size=batch_size,
                                               shuffle=True)
    return train_loader


def get_cifar_valid_loader(batch_size: int, size: float = 1):
    valid_data = torchvision.datasets.CIFAR10(root="test/", train=False,
                                              download=True, transform=transform)
    # used_data_num = int(size * len(valid_data))
    # used_data = [1] * used_data_num + [0] * (len(valid_data) - used_data_num)
    # random.shuffle(used_data)
    # valid_data = torch.utils.data.Subset(valid_data, used_data)
    valid_loader = torch.utils.data.DataLoader(valid_data, batch_size=batch_size,
                                               shuffle=True)
    return valid_loader
