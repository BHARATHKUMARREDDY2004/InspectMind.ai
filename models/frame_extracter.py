import cv2
import base64
import os
import numpy as np

class VideoFrameExtractor:
    def __init__(self, video_source):
        self.video_source = video_source
        self.video = None

    def open_video(self):
        if isinstance(self.video_source, str):
            self.video = cv2.VideoCapture(self.video_source)
        else:
            self.video = self.video_source
        
        if not self.video.isOpened():
            raise ValueError("Error: Could not open video file.")
        return self.video

    def enhance_frame(self, frame):
        # Converting to YUV color space
        yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
        
        # Histogram equalization on the Y channel
        yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
        
        # Converting back to BGR color space
        frame = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
        
        # Sharpening the image using a kernel
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        frame = cv2.filter2D(frame, -1, kernel)
        
        return frame

    def extract_frames(self):
        if not self.video:
            self.open_video()

        frame_count = 0
        base64_frames = []

        while self.video.isOpened():
            success, frame = self.video.read()
            if not success:
                break

            # Ensuring the frames are of high quality
            height, width = frame.shape[:2]
            if height < 720 or width < 1280:
                print("Warning: Low-quality video detected. Enhancing frames.")
                frame = self.enhance_frame(frame)

            # Encoding frames to JPEG format
            _, buffer = cv2.imencode(".jpg", frame)
            # Converting to base64 and append to list
            base64_frames.append(base64.b64encode(buffer).decode("utf-8"))

            frame_count += 1

        self.video.release()
        print(f"{frame_count} frames read.")
        return base64_frames

# if __name__ == "__main__":
#     video_path = "InspectMind_AI/videos/3209828-uhd_3840_2160_25fps.mp4"
    
#     # You can either pass a file path or a VideoCapture object
#     video_capture = cv2.VideoCapture(video_path)
#     extractor = VideoFrameExtractor(video_capture)

#     try:
#         frames = extractor.extract_frames()
#         print(f"Extracted {len(frames)} frames.")
#     except ValueError as e:
#         print(e)
