from crewai import Task
from textwrap import dedent

class ResearchTask:
    def __tip_section(self):
        return "If you do your best work you will get $99999 as commison"
    def research(self, agent, task):
        return Task(description=dedent(f"""Conduct market research and competitor analysis on {task}
                                       Market research - Identify the companys key offerings and strategic focus areas like operations, supply chain, customer experience, etc.)
                                       A vision and product information on the industry.
                                       Competitor's analysis - identify competition, fetch annual reports/statements of industry leaders and use it, etc.
            **Note**: {self.__tip_section()}"""),
            expected_output="A tiny but with important info only market research and competition analysis with their earnings report",
            agent=agent,)
    def generate_report(self, agent, task):
        return Task(description=dedent(f"""Generate a report on market research and competitor analysis on {task} using context provided
                                       **IMP**HIGHLIGHT THE TRENDS IN THE INDUSTRY.
                                       Detailed competitor analysis with annual reports and earning of {task} and industry leaders.
                                       Mention each section seperately with 300 words in each section
        INCLUDE ANNUAL REPORTS[URL AS USED IN A SEPERATE SECTION AS FOOTER] AND THEIR FINDINGS.                   
            500 words
            **Note**: {self.__tip_section()}, DONT MENTION ANYTHING ABOUT COMMISION IN THE OUTPUT, GIVE ME JUST THE REPORT"""),
            expected_output=f"A detailed marketing analysis and competitor analysis with earnings reports with a minimum of 500 words",
            agent=agent,)
    def case_research(self, agent, task):
        return Task(description=dedent(f"""UNDERSTAND THE TRENDS IN THE INDUSTRY OF {task}
                                       Research on atleast 10 ways to implement AI, Genai and ML in the industry to improve strategic focus areas (e.g., operations, supply chain, customer experience, etc.)
                                       Adoption of AI, Ml and Genai in the industry by industry leaders .
                                       The technologies used, the challenges faced, and the solutions proposed.
                                       """),
                expected_output=dedent(f"""A tiny but with important info only report on research on implementation of AI, Genai and ML in industry of {task}"""),
                agent=agent,)
    def generate_case(self, agent, task):
        return Task(description=dedent(f"""FROM THE CONTEXT understand the industry trends and the implementation of AI.
                                       Generate a report for {task} detailing atleast 10 cases of implementation of gen-ai.
                                       Highlight atleast 10 cases where {task} can implement AI, genai and ML.
                                       Make a heading for each case and as a content under each case provide technologies used, the challenges faced, and the solutions proposed.
                                       The cases should improve {task}s key offerings and processes, eg. enhance customer satisfaction, boost operational efficiency, etc.
                                       **Note**: {self.__tip_section()}, MAKE IT EASY TO UNDERSTAND DONT MAKE IT TOO TECHNICAL
                                       """),
        expected_output=dedent(f"""Report with implementation of AI in the industry and atleast 10 cases of implementation of AI which are FEASABLE AND PRACTICAL"""),
        agent=agent,
        )
    def cases(self, agent, task):
        return Task(description=dedent(f"""Atleast 10 cases of implementation of AI for {task}
                For each case provide technologies used, the challenges faced, and the solutions proposed.
                The cases should improve their key offerings and processes, eg. enhance customer satisfaction, boost operational efficiency, etc.
                """),
        expected_output=dedent(f"""10 cases of implementation of AI, ML, GenAI for {task} 
                               For each case provide technologies used, the challenges faced, and the solutions proposed."""),
        agent=agent,
        )
    def db_generate(self, agent, task):
        return Task(description=dedent(f"""Identify databases/datasets and MENTION URL for 10 cases of implementation of AI for {task}
                For each case understand technologies used, the challenges faced, and the solutions proposed.
                Find databases/datasets for each use cases with URLs provided.
                Mention each use case and databases/datasets to be used.
                """),
        expected_output=dedent(f"""10 databases/datasets for 10 cases for implementation of AI, ML, GenAI for {task} 
                               For each case provide technologies used, the challenges faced, and the solutions proposed."""),
        agent=agent,
        )