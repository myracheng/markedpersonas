# Marked Personas: Using Natural Language Prompts to Measure Stereotypes in Language Models

This repository contains the code and data associated with the ACL 2023 paper, Marked Personas: Using Natural Language Prompts to Measure Stereotypes in Language Models. 

## Code
To use Marked Personas, the main script is `marked_personas.py`. Example usage can be found in `reproduce_main_results.ipynb` which reproduces the figures, tables, and results of the paper. `reproduce_appendix.ipynb` reproduces the appendix in the paper. An example script to generate personas using the OpenAI API is provided in `generate_personas.py`. 

## Data
In the `data` folder, `dv2_generations.csv` and `dv3_generations.csv` contain all the personas that we generated. The other csv files `dv*_*_generations.csv` are filtered from this based on prompt;  `dv*_main_generations.csv` are the personas analyzed in the main paper. `stereo_dict.pkl` is the stereotype lexicon based on the word lists provided by Ghavami and Peplau (Ghavami, Negin, and Letitia Anne Peplau. "An intersectional analysis of gender and ethnic stereotypes: Testing three hypotheses." Psychology of Women Quarterly 37, no. 1 (2013): 113-127.)
