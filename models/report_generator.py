from openai import OpenAI

class ConstructionReportGenerator:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def generate_report(self, prompt):
        structured_prompt = f"""{prompt}\n\nPlease provide detailed descriptions for the following aspects:
        1. Structural elements: Describe the buildings, frameworks, foundations, and any structural components visible.
        2. Equipment and machinery: Identify and describe any machinery, vehicles, or equipment present on the site and their respective functions.
        3. Safety measures: Assess safety protocols, signage, protective gear, and any potential hazards.
        4. Work in progress: Detail ongoing construction activities, materials being used, and progress made.
        5. Environmental considerations: Note any environmental impacts, waste management practices, or eco-friendly initiatives.
        6. Notable observations: Highlight any unique features, challenges, or issues that require attention."""

        prompt_message = {
            "role": "user",
            "content": structured_prompt,
        }

        params = {
            "model": "gpt-4",
            "messages": [prompt_message],
            "max_tokens": 1500,
        }

        try:
            result = self.client.chat.completions.create(**params)
            response = result.choices[0].message['content']
            
            # Parse the response into the required format
            report_details = self.parse_response(response)
            return report_details
        except Exception as e:
            return f"An error occurred: {e}"

    def parse_response(self, response):
        # This should dynamic for a while sample structure of section.
        sections = {
            "Structural elements": "Structural Integrity",
            "Equipment and machinery": "Equipment and Machinery",
            "Safety measures": "Safety Compliance",
            "Work in progress": "Work Progress",
            "Environmental considerations": "Environmental Considerations",
            "Notable observations": "Notable Observations"
        }
        
        report_details = []
        for section, title in sections.items():
            start_idx = response.find(section) + len(section) + 1
            end_idx = response.find("\n", start_idx)
            if end_idx == -1:
                end_idx = len(response)
            content = response[start_idx:end_idx].strip()
            report_details.append({"title": title, "content": content})
        
        return report_details

# Example usage:
# if __name__ == "__main__":
#     api_key = "your-api-key-here"  # Replace with your OpenAI API key
#     prompt = "As a construction site inspector, I play a crucial role in ensuring the safety, quality, and compliance of construction projects."
#     generator = ConstructionReportGenerator(api_key)
#     report = generator.generate_report(prompt)
#     print(report)
