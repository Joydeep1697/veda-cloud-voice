# 🎙️ VEDA Studio Cloud Voice Bridge

This cloud microservice proxies Microsoft's Edge Neural TTS service (`Jenny`, `Ava`, `Aria`, `Emma`) into a clean REST API.
It allows Vaani to speak with broadcast-quality studio human voices on your mobile phone from anywhere in the world, even when your laptop is switched off.

---

### Option 1: Free 24/7 Hosting on Hugging Face Spaces (Recommended - Takes 1 Minute)
1. Go to [Hugging Face Spaces](https://huggingface.co/new-space).
2. Space Name: `veda-voice`
3. License: `MIT`
4. Space SDK: **Docker** (Blank)
5. Visibility: **Public**
6. Click **Create Space**.
7. Upload the 3 files from this folder:
   - `Dockerfile`
   - `requirements.txt`
   - `main.py`
8. Click **Commit new changes**. Hugging Face builds and runs the container automatically.
9. Your public endpoint will be:
   `https://<your-username>-veda-voice.hf.space/tts`

---

### Option 2: Free Hosting on Render.com
1. Go to [Render Dashboard](https://dashboard.render.com/) -> **New Web Service**.
2. Connect your Git repository containing this folder, or select Docker.
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Free Tier plan -> Deploy.
6. Your public endpoint will be:
   `https://<your-service-name>.onrender.com/tts`

---

### Connecting to Your Phone
In VEDA Android App:
Open settings and set `cloud_tts_url` to your hosted `/tts` URL!
Vaani will immediately use your cloud voice bridge from anywhere over 4G/5G/Wi-Fi with zero laptop dependency!
