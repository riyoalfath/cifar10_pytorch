import torch

# Load the checkpoint
checkpoint = torch.load('./checkpoint/ckpt.pth')

# Print the values of accuracy, loss, and epoch from the checkpoint
print("Checkpoint Accuracy:", checkpoint['acc'])
print("Checkpoint Epoch:", checkpoint['epoch'])