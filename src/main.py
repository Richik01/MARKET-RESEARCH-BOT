import streamlit as st
from crewai import Crew
from agents import Researchers
from tasks import ResearchTask
from dotenv import load_dotenv

load_dotenv()

class ResearchCrew:
    def __init__(self, tasks):
        self.tasks = tasks

    def run(self):
        agents = Researchers()
        tasks = ResearchTask()

        # AGENTS for the first research
        market_researcher = agents.MarketResearcher()
        senior_researcher = agents.SeniorMarketResearcher()
        # TASKS for the first research
        research1 = tasks.research(market_researcher, self.tasks)
        generate_report1 = tasks.generate_report(senior_researcher, self.tasks)

        crew1 = Crew(
            agents=[market_researcher, senior_researcher],
            tasks=[research1, generate_report1],
            verbose=True,
        )
        
        # AGENTS for the second research
        market_researcher2 = agents.CaseResearcher(self.tasks)
        research_analyst = agents.ResearchAnalyst(self.tasks)
        # TASKS for the second research
        research2 = tasks.case_research(market_researcher2, self.tasks)
        generate_report2 = tasks.generate_report(research_analyst, self.tasks)

        crew2 = Crew(
            agents=[market_researcher2, research_analyst],
            tasks=[research2, generate_report2],
            verbose=True,
        )
        
        # AGENTS for the third research
        case_agent = agents.DBresearcher(self.tasks)
        db_finder = agents.DBFinder(self.tasks)
        # TASKS for the third research
        cases = tasks.cases(case_agent, self.tasks)
        generate_db = tasks.db_generate(db_finder, self.tasks)

        crew3 = Crew(
            agents=[case_agent, db_finder],
            tasks=[cases, generate_db],
            verbose=True,
        )

        # Execute all crews
        result0 = crew1.kickoff()
        result1 = crew2.kickoff()
        result2 = crew3.kickoff()
        return [result0, result1, result2]

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
            
            result0 = results[0].raw
            result1 = results[1].raw
            result2 = results[2].raw
            st.write("### Market Research Results")
            st.write(result0)
            print(results[1])
            print(type(results[1]))
            st.write("### Alternative Research Results")
            st.write(result1)
            st.write("### Database Research Results")
            st.write(result2)
            with open ('links.txt', 'w') as f:
                f.write(result2)
    else:
        st.warning("Please enter a company name to proceed.")
