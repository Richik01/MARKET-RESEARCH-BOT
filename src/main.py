import streamlit as st
from crewai import Crew
from agents import Researchers
from tasks import ResearchTask
from dotenv import load_dotenv

load_dotenv()

class ResearchCrew:
    def __init__(self, tasks):
        self.tasks = tasks
        self.agents = Researchers()
        self.tasks_module = ResearchTask()

    def create_crews(self):
        
        crews = []

        # Crew 1: Market Research
        market_researcher = self.agents.MarketResearcher()
        senior_researcher = self.agents.SeniorMarketResearcher()
        research_task1 = self.tasks_module.research(market_researcher, self.tasks)
        report_task1 = self.tasks_module.generate_report(senior_researcher, self.tasks)
        crews.append(Crew(
            agents=[market_researcher, senior_researcher],
            tasks=[research_task1, report_task1],
            verbose=True
        ))

        # Crew 2: Case Research
        case_researcher = self.agents.CaseResearcher(self.tasks)
        research_analyst = self.agents.ResearchAnalyst(self.tasks)
        research_task2 = self.tasks_module.case_research(case_researcher, self.tasks)
        report_task2 = self.tasks_module.generate_report(research_analyst, self.tasks)
        crews.append(Crew(
            agents=[case_researcher, research_analyst],
            tasks=[research_task2, report_task2],
            verbose=True
        ))

        # Crew 3: Database Research
        db_researcher = self.agents.DBresearcher(self.tasks)
        db_finder = self.agents.DBFinder(self.tasks)
        cases_task = self.tasks_module.cases(db_researcher, self.tasks)
        db_generate_task = self.tasks_module.db_generate(db_finder, self.tasks)
        crews.append(Crew(
            agents=[db_researcher, db_finder],
            tasks=[cases_task, db_generate_task],
            verbose=True
        ))

        return crews

    def run(self):
        crews = self.create_crews()
        
        results = []
        for crew in crews:
            result = crew.kickoff()
            results.append(result)
        return results

# Streamlit UI
st.set_page_config(page_title="Market Research Bot", page_icon="🔍")
st.title("🔍 Market Research Bot")
st.sidebar.header("Input")
st.sidebar.write("Enter the name of the company you want to research:")
company_name = st.sidebar.text_input("Company Name:")

if st.sidebar.button("Run All Research"):
    if company_name:
        crew = ResearchCrew(tasks=company_name)
        
        with st.spinner("Running all research tasks..."):
            results = crew.run()  
            st.success("Research completed!")

            
            sections = ["### Market Research", "### Use Cases", "### Database Research Results"]
            for i, result in enumerate(results):
                st.write(sections[i])
                st.write(result.raw)

                
                if i == 2:  
                    with open('links.txt', 'w') as f:
                        f.write(result.raw)

    else:
        st.warning("Please enter a company name to proceed.")
