import gradio as gr
from models import generate_image, MODEL_ID
from config import APPLE_TENCENT_THEME

def generate_image_with_auth(prompt: str, profile: gr.OAuthProfile | None):
    if profile is None:
        raise gr.Error("⚠️ Please Sign in with Hugging Face to use this generator.")
    return generate_image(prompt)

def create_ui():
    with gr.Blocks(
        title="Boss Img Generator v2",
        theme=APPLE_TENCENT_THEME,
        css="""
        body {
            background: linear-gradient(120deg, #1e1e2f, #2d2d44);
            color: #fff;
            font-family: 'Inter', sans-serif;
        }
        h1, h2, h3, p {
            color: white !important;
        }
        .gr-button {
            font-weight: 700;
            background: linear-gradient(90deg, #ff4d4d, #ff884d);
            border: none;
            transition: all 0.3s ease;
        }
        .gr-button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 15px rgba(255, 100, 50, 0.5);
        }
        .gr-textbox textarea {
            background-color: rgba(255,255,255,0.1) !important;
            color: white !important;
            border-radius: 10px !important;
        }
        .gr-image {
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(255,255,255,0.1);
            overflow: hidden;
        }
        .title-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 0 25px rgba(255,255,255,0.05);
            text-align: center;
        }
        footer {
            text-align: center;
            margin-top: 30px;
            color: #aaa;
        }
        """
    ) as demo:
        
        gr.HTML("""
        <div class='title-card'>
            <h1>🔥 Tencent Boss Image Generator</h1>
            <p>Generate stunning AI visuals using Tencent’s advanced FAL AI model.</p>
            <p style="color: gold;">⚠️ Sign in with Hugging Face to unlock free access.</p>
        </div>
        <br>
        """)

        gr.LoginButton()

        with gr.Row():
            with gr.Column(scale=1):
                prompt_input = gr.Textbox(
                    label="Your Imagination 💭",
                    placeholder="Describe what you want (e.g., 'A cyberpunk samurai under neon rain').",
                    lines=4
                )
                generate_btn = gr.Button("⚡ Generate Image", variant="primary", size="lg")

            with gr.Column(scale=1):
                output_image = gr.Image(
                    label="🎨 Result",
                    height=512,
                    width=512,
                    interactive=False,
                    show_download_button=True
                )

        generate_btn.click(
            fn=generate_image_with_auth,
            inputs=[prompt_input],
            outputs=[output_image],
            queue=False,
            api_name=False,
            show_api=False,
        )

        gr.HTML("""
        <div style='text-align:center; margin-top:30px;'>
            <h3>✨ Try these prompts:</h3>
        </div>
        """)

        gr.Examples(
            examples=[
                "A futuristic city skyline at sunset with flying cars and neon lights",
                "A majestic lion wearing a royal crown made of fire",
                "A cinematic portrait of a samurai standing in rain, lit by neon signs",
                "A realistic photo of a baby dragon sitting in a teacup"
            ],
            inputs=prompt_input,
            outputs=output_image,
            fn=generate_image,
            cache_examples=False,
            api_name=False,
            show_api=False,
        )

        gr.HTML("""
        <footer>
            <p>⚡ Built with ❤️ by Subash | Powered by Tencent & Hugging Face</p>
        </footer>
        """)

    return demo


if __name__ == "__main__":
    app = create_ui()
    app.launch(
        show_api=False,
        enable_monitoring=False,
        quiet=True,
    )
