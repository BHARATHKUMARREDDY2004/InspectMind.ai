from moviepy.editor import VideoFileClip

class AudioExtractor:
    def __init__(self, video_clip):
        self.video_clip = video_clip

    def extract_audio(self):
        try:
            # Extract audio
            audio_clip = self.video_clip.audio
            print(f"Audio extracted from the video")
            return audio_clip
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

# # Usage example
# if __name__ == "__main__":
#     video_path = "videos/sample.mp4"
#     video_clip = VideoFileClip(video_path)
#     extractor = AudioExtractor(video_clip)
#     audio_clip = extractor.extract_audio()
