from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
# from langchain_openai.chat_models import ChatOpenAI
# from langchain.memory import ConversationSummaryBufferMemory
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import re
import json 

load_dotenv()




def extract_braces_content(text):
    # Search for the pattern with everything within and including the curly braces
    match = re.search(r'\{.*\}', text, re.DOTALL)
    
    # If a match is found, return it; otherwise, return an empty string
    return match.group(0) if match else ""





template = f"""
**Task:** You are a highly skilled recruiter. Your goal is to analyze the text extracted from a resume, which is enclosed within ####. 
Please identify and extract the following specific entities accurately:

**Entities to Extract:**
  - **First Name:** Identify the candidate's first name.
  - **Last Name:** Identify the candidate's last name.
  - **Email Address:** Detect an email address by locating the '@' symbol followed by a recognized domain (e.g., gmail, yahoo).
  - **Phone Number:** Extract a 10-digit phone number.
  - **Education History:** Identify the most recent university or school attended.
  - **Work Experience Summary:** Summarize the candidate's work experience concisely.
  - **Skills:** List all relevant skills mentioned in the resume.
  - **Current Position:** Specify the candidate's latest job title.
  - **Years of Experience:** Calculate the cumulative work experience in years, rounding months to decimal format (e.g., 1.5 years).

**Sample Input:**
  "Sample resume text here..."

**Expected Output Format:**
  Please provide a Python dictionary with the extracted entities, structured as shown below:

```json

  "First Name": "",
  "Last Name": "",
  "Email Address": "",
  "Phone Number": "",
  "Education History": "",
  "Experience Summary": "",
  "Skills": [],
  "Current Position": "",
  "Years of Experience": 0.0

  ```

  **Points to consider**
  1. Ensure that the output strictly adheres to the provided format as a valid Python dictionary.
  2. Avoid including any explanations or commentary in the output.
  3. Double-check that all instructions are followed closely.
  4. Please do not make anything up. If the entities are not identitfied in the text, then label that entitiy with NA.
  5. Please make sure that the output only contains a valid python dictionary. 


  ####
  {{cv_text}}
  ####
  """

# pip install langchain-groq

llm = ChatGroq(temperature=0.0, model_name="Llama3-8b-8192")
prompt = PromptTemplate(template=template, input_variables=["cv_text"])

chain = LLMChain(prompt=prompt, llm=llm)


def extract_entities(cv_text): 
  
  response = chain.invoke({"cv_text": cv_text})
#   print(response['text'])
  entities = json.loads(extract_braces_content(response['text']))
  print('\n\n\n', entities, '\n\n\n')
  return entities

# s = time.time()


# input = """
# AJAY KUCHHADIYA\n+91-7457878864 | Agra, Uttar Pradesh, India\nkuchhadiyaajay86kn@gmail.com | LinkedIn | GitHub\nPROFESSIONAL SUMMARY\nPassionate software engineer specializing in building advanced AI solutions. Skilled in Generative AI, NLP, and\nmachine learning using TensorFlow, Flask, and Python.\nAdept at creating cost-efficient systems and intelligent\nagents with a focus on developing impactful AI applications and deriving data-driven insights.\nEDUCATION\nB.Tech, Computer Science, 7.07 CGPA\n2020 - 2024\nHindustan College of Science and Technology\nFarah, Uttar Pradesh\n12th Grade, CBSE, 83%\n2019 - 2020\nRadhaballabh Public School\nAgra, Uttar Pradesh\nSKILLS\nProgramming Languages\nPython, C/C++\nMachine Learning/Deep Learning\nScikit-learn, TensorFlow\nData Analysis and Visualization\nPandas, SQL, NoSQL, Matplotlib, Seaborn\nGenerative AI\nLLM, RAG, Autogen, Vector Store, Hugging Face\nAPI Development\nFlask, FastAPI, RestfulAPI\nDatabases\nPostgreSQL, MongoDB\nEXPERIENCE\nTrainee Associate Software Engineer\nFeb 2024 – Aug 2024\nWalking Tree Technologies\nAgra, Uttar Pradesh\n• Developed AI-based solutions using LLM, Langchain, RAG, Vector Store databases, Autogen, and Flask.\n• Led the creation of a cost-efficient Retrieval-Augmented Generation (RAG) system, reducing API expenses.\n• Built a POC using Autogen for intelligent bug fixing and test case generation.\n• Contributed to AI-driven projects by utilizing Computer Vision techniques, PDF text extraction, Speech-to-\nText, Generative AI, and NLP.\nData Science Intern\nJun 2022 – Aug 2022\nFoxmula\nRemote\n• Analyzed datasets using Excel and Python, visualized with Matplotlib and Seaborn, leading to data-driven\ndecisions and revenue growth.\n• Produced reports on key performance indicators (KPIs), boosting efficiency by 15% and aiding strategic planning.\nPERSONAL PROJECTS\nCrewAI Health Advisor\n(GitHub)\n• Overview: Developed an AI system to assist in healthcare tasks, including summarizing medical reports, finding\nrelevant health articles, and providing health recommendations.\n• Technologies: LLM, CrewAI, Python, NLP, OCR, AI Agents.\nFashionAI: An AI-based Fashion Platform\n(GitHub)\n• Overview: Developed a fashion platform using Generative AI, Collaborative Filtering, and Visual Search.\n• Technologies: LLM (OpenAI, Groq), Computer Vision, Image Generation, Python, Flask, NLP.
# """
# x = extract_entities(input)

# print('\n\nThe new prompt : ', x)
