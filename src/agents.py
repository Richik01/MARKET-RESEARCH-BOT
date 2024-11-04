from crewai import Agent, LLM
from textwrap import dedent
from tools.search import SearchTools

class Researchers:
    def __init__(self):
        self.llm = LLM(
            model="groq/llama3-8b-8192",
            api_key="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"
        )
    def MarketResearcher(self):
        return Agent(role='Assistant Market Researcher',
        goal=dedent(f"""Market Research - understanding the industry and the segemnt the company is working in.
                    Identify the companys key offerings and strategic focus areas(eg. operations, supply chain, customer experience, etc.)
                    A vision and product information on the industry. 
                    HIGHLIGHT TRENDS IN INDUSTRY.
                    For Competitor analysis use annual reports/statements of industry leaders.
                    A comprehensive competitor analysis and market research report is required
                    """),
        backstory=dedent(f"""You are an assistant market researcher
                        You are in need for a commision. You are an professional, good at spotting and highlighting trends 
                        You have to do market research, competitor analysis and finding insights from annual reports"""),
        verbose=True,
        llm=self.llm,
        tools=[SearchTools.search_internet])
    def CaseResearcher(self,task):
        return Agent(role='AI implementation Researcher',
        goal=dedent(f"""Help {task} with the implementation of AI, ML and genai.
                    Conduct market research and competitor analysis to understand trends in industry
                    Understand AI and its implementation in innovation in the industry
                    Write a detailed report highlighting trends in the industry in terms of AI and its implementation"""),
        backstory=dedent(f"""You are an AI implementation Researcher
                        You are in need for a commision. You are an professional, good at spotting and highlighting trends 
                        You are in charge of implementation of AI for{task}"""),
        verbose=True,
        llm=self.llm,
        tools=[SearchTools.search_internet])
    def SeniorMarketResearcher(self):
        return Agent(role='Senior Market Researcher & Market Research Report Writer',
        goal=dedent(f"""Writing an detailed report for market research and competitor analysis
                    The report should identify the companys key offerings and strategic focus areas (e.g., operations, supply chain, customer experience, etc.). 
                    A vision and product information on the industry should be included. 
                    HIGHLIGHTING INDUSTRY TRENDS
                    Include a detailed competitor analyse  
                    use annual reports of company and industry leaders and competiton.
                    A comprehensive competitor analysis and market research report is required
                    1000 words """),
        backstory=dedent(f"""Senior market research with experience in analysing and understanding research work then making reports
                        You specialize in market research report writing and competitor analysis with insights from annual statements/reports"""),
        allow_delegation=True,
        llm=self.llm,
        tools=[SearchTools.search_internet])
    def ResearchAnalyst(self, task):
        return Agent(role='Researcher Analyst working for implementation of AI for {task}',
        goal=dedent(f"""Given the context understand industry trends, generate a detailed report 
                    Detailing atleast 20 cases of implementation of genai, ML, AI for {task} 
                    Should benifiting company's key offerings and strategic focus areas (e.g., operations, supply chain, customer experience, etc.)"""),
        backstory=dedent(f"""Expert research analyst at a IT company helping companies with implementation AI and genAI in their industry.
                        You are tasked with wrtiting a detailed report detailing at least 20 cases of the implementation of genai, ai and ml for {task}"""),
        allow_delegation=True,
        llm=self.llm,
        tools=[SearchTools.search_internet])
    def DBresearcher(self, task):
        return Agent(role=f'Researcher working for implementation of AI for {task}',
        goal=dedent(f"""Find 10 relevent use cases for {task}
                    Should benifiting company's key offerings and strategic focus areas (e.g., operations, supply chain, customer experience, etc.)
                    For each case provide technologies used, the challenges faced, and the solutions proposed.
                    The cases should improve their key offerings & processes, eg. enhance customer satisfaction, boost operationalial efficiency, etc"""),
        backstory=dedent(f"""Expert in finding atleast 10 relevent cases for implementation of AI, grnai, ml for {task}
                        Mention the technologies used, the challenges faced, and the solutions proposed"""),
        allow_delegation=True,
        llm=self.llm,
        tools=[SearchTools.search_internet])
    def DBFinder(self, task):
        return Agent(role='Database, Dataset, etc for AI training',
        goal=dedent(f"""Find databases for implementation of AI,ML & GenAI for {task}
                    Mention the cases and the databases/datasets for training the algorithm"""),
        backstory=dedent(f"""Expert in finding relevent datasets for training the AI"""),
        allow_delegation=True,
        llm=self.llm,
        tools=[SearchTools.db_internet])    