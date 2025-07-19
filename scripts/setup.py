import shutil
import subprocess
import sys

def get_cuda_version():
    try:
        if shutil.which("nvidia-smi"):
            nvidia_smi = subprocess.check_output(["nvidia-smi"]).decode("utf-8")
            if "CUDA Version" in nvidia_smi:
                cuda_version = nvidia_smi.split("CUDA Version: ")[1].split(" ")[0]
                cuda_version = float(cuda_version)
                return cuda_version
        else:
            print("ERROR: nvidia-smi package not found")
        
    except Exception as e:
        print(e)
        
def install_packages(cuda_version: str = None):
    
    cuda_version = get_cuda_version()
       
    if cuda_version:
        print(f"Installing packages for CUDA {cuda_version}")
        
        if cuda_version > 12.6:
            install_str = "cu128"
        elif cuda_version > 11.8:
            install_str = "cu126"
        else:
            install_str = "cu118"
        
        if install_str != "":
            subprocess.check_call([
                sys.executable, "-m", "pip", "install",
                "torch", "torchvision", "torchaudio",
                "--index-url", f"https://download.pytorch.org/whl/{install_str}"
            ])
        else:
            print(f"CUDA version {cuda_version} is not mapped to a torch release.")
            
install_packages()