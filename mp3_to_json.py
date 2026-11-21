import whisper
import json
import os

model = whisper.load_model("large-v2")
audis =os.listdir("audios")

for audio in audis:
    if("_" in audio):
        number = audio.split("_")[0][-1]
        title = audio.split("_")[1][:-4]
       
        result = model.transcribe(audio= f"audios/{audio}" ,task="translate" , language="hindi", word_timestamps=False)

        chunks=[]
        for segment in result["segments"]:
            chunks.append({ "number":number,"title":title, "start":segment['start'], "end":segment['end'],"text":segment["text"]})
                            
        chunk_with_data ={"chunks":chunks,"text":result["text"]}                     

        with open(f"json/{audio}.json", "w") as f:
            json.dump(chunk_with_data,f)                