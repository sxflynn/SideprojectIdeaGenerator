class PromptEngine:
    @staticmethod
    def prompt_project(known_tech=None, unknown_tech=None, topics=None):
        tech_list = ', '.join(known_tech) if known_tech else 'None specified'
        unknown_tech_list = ', '.join(unknown_tech) if unknown_tech else 'None specified'
        topics = ', '.join(topics) if topics else 'Pick a random topic'
        return f"""
          Your job is to help a new developer who is learning coding by suggesting one side project idea for them to work on. 
          You must provide the following for your response:
          Project Title: A short and descriptive title for the project.
          Description: A one sentence description of what the project aims to accomplish.
          Technical Requirements: 3 separate half-sentences that lay out what kind of technology stack should be used,
          and what features from the technology might the developer try implementing.
          User Stories: Write five user stories from the Agile methodology for this side project.
          
          It is an absolute requirement that your response must use this JSON format:
          {{
          "project_title": String,
          "description": String,
          "technical_requirements": [String, String, String] // array of strings
          "user_stories": [String, String, String] // array of strings
          }}
          Format your response as a JSON object using this schema. Only create one project. Do not create two or more projects.
          If your response doesn't follow this schema, then try again from the beginning to get it right.
          Do not say anything else or provide commentary, just respond with a JSON object.
          
          Use this prompt from the user to guide your response:
          The side project idea should involve some of these technologies: {tech_list}
          The side project should avoid these technologies: {unknown_tech_list}
          The developer is interested in these topics: 
          """

    
          
