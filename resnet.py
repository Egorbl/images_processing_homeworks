import torch.nn as nn
import torch.nn.functional as F


class BasicBlock(nn.Module):

    def __init__(self, in_planes, planes, stride=1):
        super(BasicBlock, self).__init__()
        self.conv1 = nn.Conv2d(
            in_planes, planes, kernel_size=3, stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(planes)
        self.conv2 = nn.Conv2d(planes, planes, kernel_size=3,
                               stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(planes)

        self.shortcut = nn.Sequential()
        if stride != 1 or in_planes != planes:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_planes, planes,
                          kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(planes)
            )

    def forward(self, x):
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += self.shortcut(x)
        out = F.relu(out)
        return out


class Encoder(nn.Module):
    def __init__(self, block):
        super(Encoder, self).__init__()
        self.in_planes = 8

        self.conv1 = nn.Conv2d(3, 8, kernel_size=3,
                               stride=1, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(8)
        self.layer1 = self._make_layer(block, 8, 2, stride=1)
        self.layer2 = self._make_layer(block, 16, 2, stride=2)
        self.layer3 = self._make_layer(block, 32, 2, stride=2)
        self.layer4 = self._make_layer(block, 64, 2, stride=2)

    def _make_layer(self, block, planes, num_blocks, stride):
        strides = [stride] + [1]*(num_blocks-1)
        layers = []
        for stride in strides:
            layers.append(block(self.in_planes, planes, stride))
            self.in_planes = planes
        return nn.Sequential(*layers)

    def forward(self, x):
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.layer1(out)
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.layer4(out)

        return out


class Decoder(nn.Module):
    def __init__(self):
        super(Decoder, self).__init__()
        self.dconv1 = nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2,
                                         padding=1, output_padding=1)
        self.dconv2 = nn.ConvTranspose2d(32, 16, kernel_size=3, stride=2,
                                         padding=1, output_padding=1)
        self.dconv3 = nn.ConvTranspose2d(16, 3, kernel_size=3, stride=2,
                                         padding=1, output_padding=1)

    def forward(self, x):
        x = F.relu(x)
        x = F.relu(self.dconv1(x))
        x = F.relu(self.dconv2(x))
        x = self.dconv3(x)
        return x


class Autoencoder(nn.Module):
    def __init__(self, encoder, decoder):
        super(Autoencoder, self).__init__()
        self.encoder = encoder
        self.decoder = decoder

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)

        return x


class ResNet18(nn.Module):
    def __init__(self, encoder, num_classes=10):
        super(ResNet18, self).__init__()
        self.encoder = encoder
        self.linear = nn.Linear(64, num_classes)

    def forward(self, x):
        out = self.encoder(x)
        out = F.avg_pool2d(out, 4)
        out = out.view(out.size(0), -1)
        out = self.linear(out)
        return out
