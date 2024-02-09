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

    def create_system_message(self, json:bool):
        if json:
            return f"""
            When responding to this prompt, generate a single side project idea for a new full stack developer. 
            Ensure the idea utilizes these technologies ({self.tech_list}) and avoids these technologies ({self.unknown_tech_list}), aligning with the developer's interests in {self.topics}.
            Your response must be formatted as a JSON object following the provided schema, containing a project title, a concise description, three technical requirements (one sentence each), and five user stories based on Agile methodology (but don't mention acceptance criteria).
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
            
        return f"""
            When responding to this prompt, generate a single side project idea for a new full stack web developer. 
            Ensure the idea utilizes these technologies ({self.tech_list}) and avoids these technologies ({self.unknown_tech_list}), aligning with the developer's interests in {self.topics}.
            Your response must contain each of the following on a new line: a project title, a concise description, three sentences describing what the technical requirements should be and what technology features should be used, and five user stories based on Agile methodology (but don't mention acceptance criteria).
            If the user mentions a technology that you don't know anything about, do not try to use that technology in a response. Do not provide extra details, so for example do not write more than three sentences for the technical requirements, more than 5 user stories, etc.
            You must strictly adhere to this format: 
            
            Project Title: Give a creative and high quality title for the project
            Description: A concise description that describes the aim and goal of the project
            Technical Requirements: Three sentences describing what the tech stack should be and what technology features should be used, like below:
            • technical requirement 1, for example "Create a RESTful API using Java Sprint Boot with endpoints for each type of activity"
            • technical requirement 2, for example "Create a RESTful API using Java Sprint Boot with endpoints for each type of activity"
            etc 3 times
            User Stories: You should give 5 user stories in a list format like below:
            • As a [user type] I _____ (give an Agile user story)
            • As a [user type] I _____ (give an Agile user story)
            etc 5 times.
            
            Do not deviate from the category names on the left. They should always be Project Title, Description, Technical Requirements, User Stories
            Only one project idea is required. Responses not following this schema should be corrected and resubmitted. Do not say anything else or provide commentary.
            """
