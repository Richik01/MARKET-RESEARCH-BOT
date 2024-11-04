from crewai import Task
from textwrap import dedent

class ResearchTask:
    def __tip_section(self):
        return "Your effort could earn a commission of up to $99,999 for top-quality work."

    def research(self, agent, task):
        return Task(
            description=dedent(f"""
                Conduct in-depth market research and competitor analysis for **{task}**:
                
                - **Market Research**: Identify key offerings, strategic focus areas (e.g., operations, supply chain, customer experience), and provide an overview of the industry.
                - **Competitor Analysis**: Identify major competitors and analyze their market position and strategies.
                
                **Note**: {self.__tip_section()}
            """),
            expected_output="A report detailing market research and competitor insights.",
            agent=agent,
        )

    def generate_report(self, agent, task):
        return Task(
            description=dedent(f"""
                Generate a comprehensive report on **{task}** with the following:
                
                - **Market Research**: Highlight emerging trends in the industry .
                - **Competitor Analysis**: Detailed analysis with annual reports and earnings for {task} and industry leaders. Include URLs in a footer for reference.
                - **INCLUDE FINANCIAL FROM ANNUAL REPORTS FOR {task} and its competition**
                **Report Requirements**:
                - Each section should have at least 100 words.
                - Minimum of 500 words overall.
                
                **Note**: {self.__tip_section()} Do not include any references to the commission in the output.
            """),
            expected_output="A well-organized report with industry trends and competitor earnings analysis, minimum 500 words.",
            agent=agent,
        )

    def case_research(self, agent, task):
        return Task(
            description=dedent(f"""
                Research AI/GenAI/ML use cases for **{task}**:
                
                - **Objective**: Identify at least 10 practical ways to implement AI to improve areas such as operations, supply chain, and customer experience.
                - Include industry examples, challenges, and solutions about how to implement it
            """),
            expected_output="A focused report with 10 potential AI, GenAI, and ML implementations for the {task} industry.",
            agent=agent,
        )

    def generate_case(self, agent, task):
        return Task(
            description=dedent(f"""
                Develop a report for **{task}** on AI implementation:
                
                - **Implementation Cases**: Detail 10 feasible AI use cases that can enhance customer satisfaction, operational efficiency, etc.
                - **For Each Case**: Include a heading, technologies used, challenges, and solutions.
                
                **Note**: {self.__tip_section()} Keep explanations accessible and avoid overly technical terms.
            """),
            expected_output="A practical report with 10 AI cases, each with technologies, challenges, and solutions.",
            agent=agent,
        )

    def cases(self, agent, task):
        return Task(
            description=dedent(f"""
                Outline 10 potential AI implementation cases for **{task}**:
                
                - For each case, provide the technologies used, challenges faced, and solutions proposed.
                - Focus on enhancing key offerings and improving core processes, such as customer satisfaction and efficiency.
            """),
            expected_output="10 AI implementation cases with technologies, challenges, and solutions for {task}.",
            agent=agent,
        )

    def db_generate(self, agent, task):
        return Task(
            description=dedent(f"""
                Identify datasets and resources for AI implementations in **{task}**:
                
                - Provide datasets and their URLs for each of the 10 AI use cases.
                - For each case, explain the technologies used, challenges faced, and solutions proposed.
            """),
            expected_output="10 datasets with URLs for AI use cases in {task}, including technologies, challenges, and solutions.",
            agent=agent,
        )
