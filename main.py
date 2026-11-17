import asyncio
from fastapi import FastAPI, Response, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import edge_tts

app = FastAPI(title="VEDA Studio Cloud Voice Bridge", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DEFAULT_VOICE = "en-US-JennyNeural"

class TTSRequest(BaseModel):
    text: str = ""
    input: str = ""
    voice: str = DEFAULT_VOICE

@app.get("/")
@app.get("/health")
async def health():
    return {"status": "online", "service": "VEDA Studio Cloud Voice Bridge"}

@app.get("/tts")
async def tts_get(text: str = Query(...), voice: str = Query(DEFAULT_VOICE)):
    if not text.strip():
        raise HTTPException(status_code=400, detail="Missing text parameter")
    try:
        communicate = edge_tts.Communicate(text, voice)
        audio = bytearray()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio.extend(chunk["data"])
        return Response(content=bytes(audio), media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tts")
@app.post("/v1/audio/speech")
async def tts_post(req: TTSRequest):
    text = req.text or req.input
    if not text.strip():
        raise HTTPException(status_code=400, detail="Missing text or input parameter")
    voice = req.voice or DEFAULT_VOICE
    try:
        communicate = edge_tts.Communicate(text, voice)
        audio = bytearray()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio.extend(chunk["data"])
        return Response(content=bytes(audio), media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
