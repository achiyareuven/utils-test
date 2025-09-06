from faster_whisper import WhisperModel

# טוענים מודל קטן (tiny/base/small/...)
model = WhisperModel("small", device="cpu", compute_type="int8")

# מבצעים תמלול לקובץ שמע
segments, info = model.transcribe(r"C:\Users\achiy\Downloads\audio-data\cv-corpus-19.0-delta-2024-09-13\en\clips\common_voice_en_41227192.mp3", language="he")

print("שפה מזוהה:", info.language, " | הסתברות:", info.language_probability)
for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
print(type(segments))
from pydub.utils import which

print(which("ffmpeg"))
