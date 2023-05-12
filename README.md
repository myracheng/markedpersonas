# Marked Personas: Using Natural Language Prompts to Measure Stereotypes in Language Models

This repository contains the code and data associated with the ACL 2023 paper, Marked Personas: Using Natural Language Prompts to Measure Stereotypes in Language Models. Please contact Myra Cheng (myra@cs.stanford.edu) if you have any questions or concerns!

## Code
Example scripts to generate personas using the OpenAI API are provided in the `generate_personas` folder. Then, to use Marked Words, the main script is `marked_words.py`. 
Example usage can be found in `reproduce_main_results_*.ipynb` which reproduces the figures, tables, and results of the paper for different models. `reproduce_appendix.ipynb` reproduces further results found in the appendix. 

## Data
In the `data` folder:
1. `gpt4_main_generations.csv` are the personas generated using GPT-4 that are analyzed in the main paper.
2. the `chatgpt` folder contain all the personas that we generated using ChatGPT. We focus on only the outputs from prompts 5 and 6, i.e. `chatgpt_prompts56_generations.csv`, for reasons explained in the paper. The outputs from other prompts are included in `chatgpt_other_generations.csv.`
3. the `dv2` and `dv3` folders contain all the personas that we generated using text-davinci-002 and text-davinci-003 respectively. `dv*_main_generations.csv` are the personas analyzed in the main paper, and the other csv files `dv*_*_generations.csv` are filtered based on the specific prompt. 
4. `stereo_dict.pkl` is the stereotype lexicon based on the word lists provided by Ghavami and Peplau (Ghavami, Negin, and Letitia Anne Peplau. "An intersectional analysis of gender and ethnic stereotypes: Testing three hypotheses." Psychology of Women Quarterly 37, no. 1 (2013): 113-127.)
