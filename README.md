# Marked Personas: Using Natural Language Prompts to Measure Stereotypes in Language Models

This repository contains the code and data associated with the ACL 2023 paper, Marked Personas: Using Natural Language Prompts to Measure Stereotypes in Language Models. Please contact Myra Cheng (myra@cs.stanford.edu) if you have any questions or concerns!

## Code
Example scripts to generate personas using the OpenAI API are provided in the `persona_generation` folder. Then, to use Marked Words, the main script is `marked_words.py`. 
Example usage can be found in `make_tables.ipynb` which reproduces the results and tables of the paper for GPT-3.5 and GPT-4. 
`dv3_vs_dv2.ipynb` reproduces comparison of stereotype rates between text-davinci-003 and text-davinci-002. 
`reproduce_results_chatgpt.ipynb` reproduces results for ChatGPT. `reproduce_results_stories.ipynb` reproduces results for generated stories. 
`sentiment_analysis.ipynb` reproduces sentiment analysis results.

## Data
In the `data` folder:
1. `gpt4_main_generations.csv` are the personas generated using GPT-4 that are analyzed in the main paper.
2. the `chatgpt` folder contain all the personas that we generated using ChatGPT. We focus on only the outputs from prompts 5 and 6, i.e. `chatgpt_main_generations.csv`, for reasons explained in the paper. The outputs from other prompts are included in `chatgpt_all_generations.csv.`
3. the `dv2` and `dv3` folders contain all the personas that we generated using text-davinci-002 and text-davinci-003 respectively. `dv*_main_generations.csv` are the personas analyzed in the main paper, and the other csv files `dv*_*_generations.csv` are filtered based on the specific prompt. 
4. `stereo_dict.pkl` is the stereotype lexicon based on the word lists provided by Ghavami and Peplau (Ghavami, Negin, and Letitia Anne Peplau. "An intersectional analysis of gender and ethnic stereotypes: Testing three hypotheses." Psychology of Women Quarterly 37, no. 1 (2013): 113-127.)
