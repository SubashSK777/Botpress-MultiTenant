import os
from huggingface_hub import InferenceClient
from PIL import Image
import gradio as gr
from typing import Union

# Load environment variables (useful for local testing)
from dotenv import load_dotenv
load_dotenv()

# --- Model Configuration ---
MODEL_ID = "tencent/HunyuanImage-3.0"
PROVIDER = "fal-ai"
BILL_TO = "huggingface"

# Initialize client
HF_TOKEN = os.environ.get("HF_TOKEN")
CLIENT: Union[InferenceClient, None] = None

if HF_TOKEN:
    try:
        # Note: FAL AI provider uses HF_TOKEN as its api_key
        CLIENT = InferenceClient(
            provider=PROVIDER,
            api_key=HF_TOKEN,
            bill_to=BILL_TO,
        )
        print(f"✅ InferenceClient initialized for {MODEL_ID} via {PROVIDER}")
    except Exception as e:
        print(f"❌ Error initializing InferenceClient: {e}")
        CLIENT = None
else:
    print("⚠️ HF_TOKEN environment variable not set. Client will be unavailable.")

def generate_image(prompt: str) -> Image.Image:
    """
    Generates an image from a text prompt using the Hugging Face Inference Client.
    """
    if not CLIENT:
        raise gr.Error("API client not available. Please ensure HF_TOKEN is set correctly.")
    
    if not prompt:
        raise gr.Error("Please provide a prompt.")

    print(f"Generating image for prompt: '{prompt[:50]}...'")

    try:
        # The output is a PIL.Image object directly
        image = CLIENT.text_to_image(
            prompt,
            model=MODEL_ID,
        )
        return image
    except Exception as e:
        print(f"Error during image generation: {e}")
        if "Authentication failed" in str(e):
             raise gr.Error("Authentication failed. Check your HF_TOKEN.")
        if "limit reached" in str(e) or "quota" in str(e):
             raise gr.Error("Rate limit or quota reached for this API endpoint.")
        raise gr.Error(f"Generation failed: {str(e)}")