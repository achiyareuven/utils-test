# from pydub import AudioSegment
# from pathlib import Path
#
# def convert_to_wav(input_path: str | Path, output_path: str | Path | None = None, sample_rate: int = 16000, mono: bool = True) -> str:
#     """
#     ממיר כל פורמט נתמך (mp3/m4a/flac/ogg/amr/wav...) ל-WAV סטנדרטי (ברירת מחדל 16kHz מונו)
#     מחזיר את הנתיב של קובץ ה-WAV שנוצר.
#     """
#     input_path = Path(input_path)
#     if output_path is None:
#         output_path = input_path.with_suffix(".wav")
#     else:
#         output_path = Path(output_path)
#
#     # טעינה אוטומטית לפי סיומת/מג'יק
#     audio = AudioSegment.from_file(input_path)
#
#     # נורמליזציה: קצב דגימה/מונו (מומלץ ל-STT)
#     if sample_rate:
#         audio = audio.set_frame_rate(sample_rate)
#     if mono:
#         audio = audio.set_channels(1)
#
#     audio.export(output_path, format="wav")
#     return str(output_path)
#
#
# from pydub import AudioSegment
# import speech_recognition as sr
# from pathlib import Path
# import io, tempfile
#
# def _to_wav_bytes(input_path: str | Path) -> bytes:
#     """ממיר כל פורמט נתמך ל־WAV ומחזיר bytes."""
#     input_path = Path(input_path)
#     audio = AudioSegment.from_file(input_path)  # ffmpeg חובה
#     audio = audio.set_frame_rate(16000).set_channels(1)  # מומלץ ל-STT
#     buf = io.BytesIO()
#     audio.export(buf, format="wav")
#     return buf.getvalue()
#
# def transcribe_file(input_path: str | Path, language: str = "he-IL") -> str:
#     """
#     ממיר את הקובץ ל-WAV (אם צריך) ומתמלל עם Google Web Speech.
#     הערה: השירות אונליין ויכול להיות מוגבל בקצב/אורך.
#     """
#     r = sr.Recognizer()
#     wav_bytes = _to_wav_bytes(input_path)
#     with sr.AudioFile(io.BytesIO(wav_bytes)) as source:
#         audio = r.record(source)  # כל הקובץ; לקבצים ארוכים עדיף לעבוד במקטעים
#     try:
#         return r.recognize_google(audio, language=language)
#     except sr.UnknownValueError:
#         return ""  # לא זוהה דיבור
#     except sr.RequestError as e:
#         raise RuntimeError(f"תקלה בשירות STT: {e}")


from pydub import AudioSegment
import speech_recognition as sr
import io

def audio_to_text(file_path: str, language: str = "en-US") -> str:
    # המרה ל-WAV (16kHz, מונו)
    audio = AudioSegment.from_file(file_path)
    audio = audio.set_frame_rate(16000).set_channels(1)
    buf = io.BytesIO()
    audio.export(buf, format="wav")
    buf.seek(0)

    # תמלול עם SpeechRecognition
    r = sr.Recognizer()
    with sr.AudioFile(buf) as source:
        audio_data = r.record(source)
    try:
        return r.recognize_google(audio_data, language=language)
    except sr.UnknownValueError:
        return "[Speech not recognized]"
    except sr.RequestError as e:
        return f"[STT service error: {e}]"

# שימוש:
print(audio_to_text(r"C:\Users\achiy\Downloads\audio-data\cv-corpus-19.0-delta-2024-09-13\en\clips\common_voice_en_41227191.mp3"))  # תחליף בשם הקובץ שלך
from pydub.utils import which

print(which("ffmpeg"))