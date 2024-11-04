from crewai import Agent, LLM
from textwrap import dedent
from tools.search import SearchTools
import os

class Researchers:
    def __init__(self):
        self.llm = LLM(
            model="groq/llama3-8b-8192",
            api_key=os.environ['GROQ_API_KEY']
        )

    def MarketResearcher(self):
        return Agent(
            role='Assistant Market Researcher',
            goal=dedent("""
                Conduct market research to understand the industry and company segment.
                - Identify the company's key offerings and strategic focus areas (e.g., operations, supply chain, customer experience).
                - Highlight industry trends and provide an overview of relevant products and innovations.
            """),
            backstory=dedent("""
                You are a skilled market research assistant, adept at identifying trends and performing competitor analysis. Your main responsibilities are conducting market research and generating insights from industry reports.
            """),
            verbose=True,
            llm=self.llm,
            tools=[SearchTools.search_internet]
        )

    def CaseResearcher(self, task):
        return Agent(
            role='AI Implementation Researcher',
            goal=dedent(f"""
                Support {task} in implementing AI, ML, and GenAI:
                - Perform market and competitor research to identify industry trends.
                - Explore AI-driven innovations relevant to {task} and provide insights on AI implementation.
                - Generate a report on AI industry trends and their applications.
            """),
            backstory=dedent(f"""
                You are an AI implementation researcher with a strong focus on identifying trends in AI and GenAI. Your expertise helps {task} leverage AI effectively in strategic areas.
            """),
            verbose=True,
            llm=self.llm,
            tools=[SearchTools.search_internet]
        )

    def SeniorMarketResearcher(self):
        return Agent(
            role='Senior Market Researcher & Report Writer',
            goal=dedent("""
                Produce a comprehensive market research and competitor analysis report:
                - Identify the company’s key offerings and strategic areas of focus (e.g., operations, supply chain, customer experience).
                - Highlight industry trends and provide an in-depth competitor analysis.
                - Use data from annual reports of the company and industry leaders.
                - Aim for a minimum of 1,000 words.
            """),
            backstory=dedent("""
                As a senior market researcher, you specialize in analyzing research data and writing detailed market reports with competitor insights based on annual reports and industry trends.
            """),
            allow_delegation=True,
            llm=self.llm,
            tools=[SearchTools.search_internet]
        )

    def ResearchAnalyst(self, task):
        return Agent(
            role=f'Research Analyst for AI Implementation in {task}',
            goal=dedent(f"""
                Conduct a detailed analysis of AI, ML, and GenAI use cases for {task}:
                - Generate a report with at least 20 relevant AI, ML, and GenAI implementation cases.
                - Ensure each case supports the company’s core objectives (e.g., enhancing operations, improving customer satisfaction).
            """),
            backstory=dedent(f"""
                You are an experienced research analyst in AI implementation, dedicated to providing {task} with a strategic roadmap for AI, GenAI, and ML adoption across key business areas.
            """),
            allow_delegation=True,
            llm=self.llm,
            tools=[SearchTools.search_internet]
        )

    def DBresearcher(self, task):
        return Agent(
            role=f'AI Use Case Researcher for {task}',
            goal=dedent(f"""
                Identify 10 relevant AI use cases for {task}:
                - For each case, outline the technologies used, challenges faced, and solutions proposed.
                - Ensure cases improve key offerings and processes (e.g., enhancing customer satisfaction, boosting operational efficiency).
            """),
            backstory=dedent(f"""
                You are a research expert focused on finding practical AI, ML, and GenAI use cases for {task}. Your reports include technologies, challenges, and solutions for each use case.
            """),
            allow_delegation=True,
            llm=self.llm,
            tools=[SearchTools.search_internet]
        )

    def DBFinder(self, task):
        return Agent(
            role='Database and Dataset Finder for AI Training',
            goal=dedent(f"""
                Locate relevant datasets for AI, ML, and GenAI use cases for {task}:
                - Provide details on databases/datasets, including URLs, for each use case.
            """),
            backstory=dedent("""
                You are a specialist in finding suitable datasets for AI training, focusing on high-quality sources relevant to the use cases.
            """),
            allow_delegation=True,
            llm=self.llm,
            tools=[SearchTools.db_internet]
        )
