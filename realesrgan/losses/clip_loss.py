import torch
from torch import nn as nn
from torch.nn import functional as F
from torchvision.transforms.functional import to_pil_image

import clip
from basicsr.utils.registry import LOSS_REGISTRY

@LOSS_REGISTRY.register()
class ClipLoss(nn.Module):

    def __init__(self, loss_weight):
        super(ClipLoss, self).__init__()
        self.loss_weight = loss_weight
        
        self.device = torch.device('cuda' if torch.cuda.is_available() else "cpu")
        model, preprocess = clip.load("ViT-B/32", device=self.device)
        self.model = model
        self.preprocess = preprocess

        self.criterion = nn.CrossEntropyLoss()

    def forward(self, x, text):
        batch_size = x.shape[0]

        images = []
        for i in range(batch_size):
            image = to_pil_image(x[i])
            images.append(self.preprocess(image).unsqueeze(0).to(self.device))

        texts = clip.tokenize(text).to(self.device)

        probs = []
        for image in images:
            with torch.no_grad():
                # image_features = self.model.encode_image(image)
                # text_features = self.model.encode_text(text)
                
                logits_per_image, _ = self.model(image, texts) # (n_image, n_text)
                probs.append(logits_per_image.softmax(dim=-1))

        probs = torch.stack(probs, dim=0).squeeze(1)
        target = torch.eye(batch_size).to(self.device)

        return self.criterion(probs, target) * self.loss_weight