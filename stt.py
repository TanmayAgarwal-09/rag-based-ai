import whisper
import json
model=whisper.load_model("base")
result=model.transcribe(audio="audio/1_Your First Day.mp3",language="en",task="translate",word_timestamps=False)
print(result["segments"])
chunks=[]
for segment in result["segments"]:
    chunks.append({"start":segment["start"],"end":segment["end"],"text":segment["text"]})
with open("output.json","w") as f:
    json.dump(chunks,f)

