from models.frame_extracter import VideoFrameExtractor
from models.audio_to_text import AudioTranscriber
from models.audio_extracter import AudioExtractor
from models.image_to_text import ConstructionSiteInspector
from models.report_generator import ConstructionReportGenerator
from flask import Flask, render_template, request
from moviepy.editor import VideoFileClip
import os
import tempfile
import cv2
from pydub import AudioSegment

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = tempfile.mkdtemp()

api_key = "your-api-key-here"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_report', methods=['GET', 'POST'])
def create_report():
    report_name = ""
    report_prompt = ""
    report_summary = ""
    report_details = []
    saved_videos = []
    saved_images = []
    saved_audios = []

    if request.method == 'POST':
        transcriber = AudioTranscriber(api_key=api_key, chunk_length_minutes=5)
        report_name = request.form.get('report-name', "")
        report_prompt = request.form.get('report-prompt', "")

        # Processing uploaded videos
        if 'videos' in request.files:
            for video in request.files.getlist('videos'):
                if video.filename != '':
                    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
                    video.save(video_path)
                    saved_videos.append(video_path)

            # Processing uploaded images
        if 'images' in request.files:
            for image in request.files.getlist('images'):
                if image.filename != '':
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                    image.save(image_path)
                    saved_images.append(image.filename)

        # Processing uploaded audios
        if 'audios' in request.files:
            for audio in request.files.getlist('audios'):
                if audio.filename != '':
                    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio.filename)
                    audio.save(audio_path)
                    saved_audios.append(audio.filename)

        # Iterating through the saved video files
        video_descriptions = ""
        for video_file in saved_videos:
            print(f"Saved video file: {video_file}")
            video_capture = cv2.VideoCapture(video_file)
            extractor = VideoFrameExtractor(video_capture)
            frames = extractor.extract_frames()
            print(f"Extracted {len(frames)} frames.")
            

            video_clip = VideoFileClip(video_path)
            extractor = AudioExtractor(video_clip)
            audio_clip = extractor.extract_audio()
            if audio_clip:
                full_transcript = transcriber.split_audio_into_chunks(audio_clip)

            frames_prompt = "Act as a construction site inspector, you play a crucial role in ensuring the safety, quality, and compliance of construction projects. Inspect the frames of video and list down the necessary information."
            if frames:
                # slicing the frames list to take 1 out of every 50 frames.
                inspector = ConstructionSiteInspector(frames[::50], report_prompt + frames_prompt) 
                temp = inspector.analyze_images()
                video_descriptions += temp
        
        audio_transcripts = ""
        for audio_file in saved_audios:
            audio_segment = AudioSegment.from_mp3(audio_file)  # Replace this line with direct audio segment.
            full_transcript = transcriber.split_audio_into_chunks(audio_segment)
            audio_transcripts += full_transcript + "\n"


        img_prompt = "Act as a construction site inspector, you play a crucial role in ensuring the safety, quality, and compliance of construction projects.Inspect the images and list down the necessary information"
        if saved_images:
            inspector = ConstructionSiteInspector(saved_images, report_prompt + img_prompt)
            image_descriptions = inspector.analyze_images()

        prompt = report_prompt + "Video information : " + video_descriptions + "\n\n" + "image information : " + image_descriptions + "\n\n" + audio_transcripts + "\n\n" + "from all this information of site inspection make report details from this information"
        generator = ConstructionReportGenerator(api_key)
        report = generator.generate_report(prompt)

        # Actual rendering output : report
        # For a while sample report summary and details (this is should be repace report)
        report_summary = "The inspection report highlights key findings and observations from the construction site."
        report_details = [
                        {
                            "title": "Structural Integrity",
                            "content": "The main building's framework is constructed with reinforced steel and concrete, showing no visible defects. The foundations are deep and stable, indicating a strong base for the structure. Beams and columns are properly aligned and securely fastened. Additionally, there are no signs of cracks or settlements in the walls, and the load-bearing elements appear to be performing as expected."
                        },
                        {
                            "title": "Equipment and Machinery",
                            "content": "On-site equipment includes two tower cranes, three excavators, five cement mixers, and various smaller tools such as drills and welding machines. The machinery appears well-maintained with regular servicing records. Safety guards and operational protocols are in place for all heavy machinery. The fuel storage area is well-secured and away from high-traffic zones to prevent accidents."
                        },
                        {
                            "title": "Safety Compliance",
                            "content": "Safety measures are robust, with all personnel wearing PPE including helmets, gloves, and steel-toed boots. Safety harnesses are used correctly at heights. Clear signage marks hazardous areas, and fire extinguishers and first aid kits are readily accessible. Emergency evacuation routes are clearly indicated. Regular safety drills are conducted, and a safety officer is present on-site to enforce compliance."
                        },
                        {
                            "title": "Work Progress",
                            "content": "The project is on track with the construction schedule. The ground floor structure is complete, and the first floor slab has been poured. Bricklaying and internal partitioning are ongoing. Electrical wiring and plumbing rough-ins are in progress. Material stockpiles are well-organized and labeled. Quality control checks are conducted regularly to ensure adherence to specifications."
                        },
                        {
                            "title": "Environmental Considerations",
                            "content": "Efforts to reduce environmental impact include the use of eco-friendly materials such as low-VOC paints and recycled steel. Waste segregation practices are in place with separate bins for concrete, wood, and general waste. Noise and dust control measures, such as water spraying and sound barriers, are effectively implemented. Additionally, erosion control measures are in place to prevent soil displacement during heavy rains."
                        },
                        {
                            "title": "Notable Observations",
                            "content": "The construction site features a well-organized layout with designated zones for different activities, reducing the risk of accidents. A minor issue was identified with the temporary drainage system, which needs reinforcement to prevent waterlogging. Additionally, the site's logistics are efficient, with minimal delays in material delivery and worker deployment. An innovative feature includes the use of prefabricated components to speed up construction and ensure quality."
                        }
]

    return render_template('create_report.html', 
                           report_name=report_name, 
                           report_prompt=report_prompt, 
                           report_summary=report_summary, 
                           report_details=report_details)


if __name__ == "__main__":
    app.run(debug=True)
