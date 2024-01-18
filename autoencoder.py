import torch.nn as nn
import torch.nn.functional as F
import torch


class SimpleEncoder(nn.Module):

    def __init__(self):
        super(SimpleEncoder, self).__init__()
        self.conv1 = nn.Conv2d(3, 8, 3, stride=2, padding=1)
        self.conv2 = nn.Conv2d(8, 16, 3, stride=2, padding=1)
        self.conv3 = nn.Conv2d(16, 32, 3, stride=2, padding=1)

    def forward(self, x):
        x = F.leaky_relu(self.conv1(x))
        x = F.leaky_relu(self.conv2(x))
        x = F.leaky_relu(self.conv3(x))

        return x


class SimpleDecoder(nn.Module):

    def __init__(self):
        super(SimpleDecoder, self).__init__()
        self.conv1 = nn.ConvTranspose2d(32, 16, 3, stride=2,
                                        padding=1, output_padding=1)
        self.conv2 = nn.ConvTranspose2d(16, 8, 3, stride=2,
                                        padding=1, output_padding=1)
        self.conv3 = nn.ConvTranspose2d(8, 3, 3, stride=2,
                                        padding=1, output_padding=1)

    def forward(self, x):
        x = F.leaky_relu(self.conv1(x))
        x = F.leaky_relu(self.conv2(x))
        x = F.sigmoid(self.conv3(x))

        return x


class SimpleConvAutoencoder(nn.Module):
    def __init__(self, encoder, decoder):
        super(SimpleConvAutoencoder, self).__init__()
        self.encoder = encoder
        self.decoder = decoder

    def forward(self, x):
        x = self.encoder(x)
        return self.decoder(x)


class ConvolutionalAutoencoder(nn.Module):
    def __init__(self):
        super().__init__()

        layer_count = 3
        in_channels = 3
        out_channels = 16

        encoder_layers = []
        decoder_layers = []

        for i in range(layer_count):
            encoder_layers.append(nn.Conv2d(in_channels, out_channels, 3, 2, 1))
            encoder_layers.append(nn.BatchNorm2d(out_channels))
            encoder_layers.append(nn.LeakyReLU())
            if i == 0:
                decoder_layers.append(nn.Tanh())
            else:
                decoder_layers.append(nn.LeakyReLU())
            decoder_layers.append(nn.ConvTranspose2d(out_channels, in_channels, 3, 2, 1, 1))
            in_channels = out_channels
            out_channels *= 2
        decoder_layers.reverse()

        self.encoder = nn.Sequential(*encoder_layers)
        self.decoder = nn.Sequential(*decoder_layers)

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x
