from pydub import AudioSegment
import io
import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "your api key"

class AudioTranscriber:
    def __init__(self, api_key, chunk_length_minutes=5):
        aai.settings.api_key = api_key
        self.chunk_length_minutes = chunk_length_minutes
        self.transcriber = aai.Transcriber()

    def split_audio_into_chunks(self, audio_segment):
        chunk_length_ms = self.chunk_length_minutes * 60 * 1000
        total_length_ms = len(audio_segment)
        num_chunks = total_length_ms // chunk_length_ms + (1 if total_length_ms % chunk_length_ms else 0)

        full_transcript = ""

        for i in range(num_chunks):
            start_time = i * chunk_length_ms
            end_time = min((i + 1) * chunk_length_ms, total_length_ms)
            chunk = audio_segment[start_time:end_time]

            try:
                chunk_io = io.BytesIO()
                chunk.export(chunk_io, format="mp3")
                chunk_io.seek(0)
                transcript = self.transcriber.transcribe(chunk_io)

                if transcript.status == aai.TranscriptStatus.error:
                    print(f"Error in chunk {i + 1}: {transcript.error}")
                else:
                    full_transcript += transcript.text + " "
                    print(f"Transcript for chunk {i + 1} added.")
            except Exception as e:
                print(f"Error processing chunk {i + 1}: {e}")

        return full_transcript

# if __name__ == "__main__":
#     audio_path = "audio/sample.mp3"
#     audio_segment = AudioSegment.from_mp3(audio_path)  # Replace this line with your direct audio segment if you have it
#     transcriber = AudioTranscriber(api_key="013554abcd444e1", chunk_length_minutes=5)
#     full_transcript = transcriber.split_audio_into_chunks(audio_segment)

#     if full_transcript:
#         print("Full Transcript:\n", full_transcript)
