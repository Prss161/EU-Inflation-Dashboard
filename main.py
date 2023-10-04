import subprocess

subprocess.run(["python", ".\Doc\inflation_eurostat.py"])

subprocess.run(["python", "-m", "streamlit", 'run', ".\Doc\dashboard.py"])