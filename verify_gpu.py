import torch

def verify_gpu_setup():
    print(f"CUDA available: {torch.cuda.is_available()}")
    print(f"GPU count: {torch.cuda.device_count()}")
    print(f"GPU name: {torch.cuda.get_device_name(0)}")

if __name__ == "__main__":
    verify_gpu_setup()
