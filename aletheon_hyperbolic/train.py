import argparse
import torch
from torch import nn
from .model import AletheonClassifier
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=30)
    parser.add_argument("--checkpoint", default="aletheon_checkpoint.pt")
    args = parser.parse_args()
    torch.manual_seed(42)
    x = torch.randn(240, 8)
    y = torch.bucketize(x[:, 0] + 0.5*x[:, 1], torch.tensor([-0.5, 0.5]))
    model = AletheonClassifier()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    for epoch in range(args.epochs):
        optimizer.zero_grad()
        loss = nn.functional.cross_entropy(model(x), y)
        loss.backward()
        optimizer.step()
        print(f"epoch={epoch+1} loss={loss.item():.4f}")
    torch.save({"state_dict":model.state_dict(),"config":{"input_dim":8,"hidden_dim":16,"num_classes":3,"c":1.0},"seed":42}, args.checkpoint)
if __name__ == "__main__":
    main()
