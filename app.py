import gradio as gr
import edge_tts
import asyncio
import tempfile
import os

DEFAULT_VOICE = "en-US-JennyNeural"

async def generate_speech(text, voice):
    if not text.strip():
        return None
    communicate = edge_tts.Communicate(text, voice)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp_path = tmp.name
    await communicate.save(tmp_path)
    return tmp_path

def tts_fn(text, voice=DEFAULT_VOICE):
    return asyncio.run(generate_speech(text, voice))

# Gradio Interface (Automatically exposes an API endpoint)
demo = gr.Interface(
    fn=tts_fn,
    inputs=[
        gr.Textbox(label="Text to Speak", value="Hello Joy, VEDA Studio Voice is online."),
        gr.Dropdown(
            choices=[
                "en-US-JennyNeural",
                "en-US-AvaMultilingualNeural",
                "en-US-AriaNeural",
                "en-US-EmmaMultilingualNeural",
                "en-IN-NeerjaNeural",
                "en-GB-SoniaNeural"
            ],
            value=DEFAULT_VOICE,
            label="Voice"
        )
    ],
    outputs=gr.Audio(label="Synthesized Audio", type="filepath"),
    title="VEDA Studio Cloud Voice Bridge"
)

if __name__ == "__main__":
    demo.launch()
