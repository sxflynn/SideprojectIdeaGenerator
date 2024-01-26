class PromptEngine:
    def __init__(self, user_input):
        self.inputs = {
            'tech_list': {
                'data': user_input.known_tech,
                'fallback': 'Frequently used full stack frameworks'
            },
            'unknown_tech_list': {
                'data': user_input.unknown_tech,
                'fallback': 'Rarely used or difficult to understand technologies'
            },
            'topics': {
                'data': user_input.topics,
                'fallback': 'Pick a random topic'
            }
        }
        self.tech_list = self.unpack_list('tech_list')
        self.unknown_tech_list = self.unpack_list('unknown_tech_list')
        self.topics = self.unpack_list('topics')
        
    def unpack_list(self, key):
        data = self.inputs[key]['data']
        fallback = self.inputs[key]['fallback']
        return ', '.join(data) if data else fallback
    
    def create_prompt(self):
        return f"""
          Suggest one side project idea for a new developer to work on. 
          The side project idea should involve some of these technologies: {self.tech_list}
          The side project should avoid these technologies: {self.unknown_tech_list}
          The developer is interested in these topics: {self.topics}
          """

    def create_system_message(self):
        return f"""
            When responding to this prompt, generate a single side project idea for a new full stack developer. 
            Ensure the idea utilizes these technologies ({self.tech_list}) and avoids these technologies ({self.unknown_tech_list}), aligning with the developer's interests in {self.topics}.
            Your response must be formatted as a JSON object following the provided schema, containing a project title, a concise description, three technical requirements (one sentence each), and five user stories based on Agile methodology.
            Adhere strictly to this format: 
            {{
                "project_title": "String",
                "description": "String",
                "technical_requirements": ["String", "String", "String"], 
                "user_stories": ["String", "String", "String", "String", "String"]
            }}
            Only one project idea is required. Responses not following this schema should be corrected and resubmitted. Do not include additional commentary.
            Do not say anything else or provide commentary beyond the JSON, just respond with a JSON object.
            """
