from openai import OpenAI
import os

class ConstructionSiteInspector:
    def __init__(self, images, prompt):
        self.images = images
        self.prompt = prompt
        self.client = OpenAI(apikey = "your api key")

    def analyze_images(self):
        prompt_messages = [
            {
                "role": "user",
                "content": [
                    f"""{self.prompt}\n\nPlease analyze each image meticulously and provide in-depth information regarding the following: As a construction site inspector, I play a crucial role in ensuring the safety, quality, and compliance of construction projects. To conduct a thorough inspection, I need detailed descriptions for each image capturing various aspects of the construction site. Please analyze each image meticulously and provide in-depth information regarding the following:
                    1. Structural elements: Describe the buildings, frameworks, foundations, and any structural components visible.
                    2. Equipment and machinery: Identify and describe any machinery, vehicles, or equipment present on the site and their respective functions.
                    3. Safety measures: Assess safety protocols, signage, protective gear, and any potential hazards.
                    4. Work in progress: Detail ongoing construction activities, materials being used, and progress made.
                    5. Environmental considerations: Note any environmental impacts, waste management practices, or eco-friendly initiatives.
                    6. Notable observations: Highlight any unique features, challenges, or issues that require attention.
                    Please provide comprehensive information for each image to facilitate a thorough inspection and ensure the success of the construction project.""",
                    *map(lambda x: {"image": x}, self.images),
                ],
            },
        ]

        params = {
            "model": "gpt-4o",
            "messages": prompt_messages,
            "max_tokens": 1000,
        }

        try:
            result = self.client.chat.completions.create(**params)
            descriptions = result.choices[0].message.content
            return descriptions
        except Exception as e:
            return f"An error occurred: {e}"

# # Example usage:
# if __name__ == "__main__":
#     images = ["image1.jpg", "image2.jpg"]  # Replace with user-provided image URLs or file paths
#     prompt = "As a construction site inspector, I play a crucial role in ensuring the safety, quality, and compliance of construction projects."
#     inspector = ConstructionSiteInspector(images, prompt)
#     descriptions = inspector.analyze_images()
#     print(descriptions)
