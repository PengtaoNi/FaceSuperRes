import torch
from torch import nn as nn
from torch.nn import functional as F

import clip
from basicsr.utils.registry import LOSS_REGISTRY

@LOSS_REGISTRY.register()
class ClipLoss(nn.Module):

    def __init__(self, loss_weight):
        super(ClipLoss, self).__init__()
        self.device = torch.device('cuda' if torch.cuda.is_available() else "cpu")
        model, preprocess = clip.load("ViT-B/32", device=self.device)
        self.model = model
        self.preprocess = preprocess

        self.criterion = nn.CrossEntropyLoss()

    def forward(self, x, text):
        images = self.preprocess(x).to(self.device)
        texts = clip.tokenize(text).to(self.device)

        with torch.no_grad():
            # image_features = self.model.encode_image(image)
            # text_features = self.model.encode_text(text)
            
            logits_per_image, _ = self.model(images, texts) # (n_image, n_text)
            probs = logits_per_image.softmax(dim=-1)
            
            target = torch.eye(probs.shape[0]).to(self.device)

        return self.criterion(probs, target) * self.loss_weight