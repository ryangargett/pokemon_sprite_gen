from diffusers import AutoPipelineForText2Image
import regex as re
import torch
import os
import sys

def sanitize_deduplicate_filename(
    prompt: str,
    output_path: str = "."
) -> str:
    file_name = re.sub(r"[<>:'/\\|?*]", "_", prompt)
        
    os.makedirs(output_path, exist_ok=True)

    counter = 1
    base_path = os.path.join(output_path, file_name)
    file_path = f"{base_path}.png"
    
    while os.path.exists(file_path): # deduplicate to avoid accidental overwrite
        file_path = f"{base_path}_{counter}"
        counter += 1
    
    return file_path

def generate(prompt: str):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    ###
    # Replace the below with different models / pipelines from huggingface (legit just copy the code lol 😊)
    ###

    pipeline = AutoPipelineForText2Image.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0",
        torch_dtype=torch.float16,
        use_safetensors=True
    ).to(device)

    pipeline.load_lora_weights(
        "sWizad/pokemon-trainer-sprite-pixelart",
        weight_name="pk_trainer_xl_v1.safetensors"
    )
    
    modified_prompt = ",".join([prompt, "simple background", "pokemon trainer"])

    image = pipeline(modified_prompt).images[0]
    image.save(f"{sanitize_deduplicate_filename(prompt)}")
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: python main.py <prompt>")
        sys.ext(1)
        
    prompt = " ".join(sys.argv[1:])
    generate(prompt)