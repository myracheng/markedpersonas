"""
Running this file obtains the words that distinguish a target group from the corresponding
unmarked ones.
Example usage: (To obtain the words that differentiate the 'Asian F' category)
python3 marked_words.py ../generated_personas.csv --target_val 'an Asian' F --target_col race gender --unmarked_val 'a White' M
"""

import pandas as pd
import numpy as np
from collections import Counter
import argparse
from collections import defaultdict
import math
import sys

def get_log_odds(df1, df2, df0,verbose=False,lower=True):
    """Monroe et al. Fightin' Words method to identify top words in df1 and df2
    against df0 as the background corpus"""
    if lower:
        counts1 = defaultdict(int,[[i,j] for i,j in df1.str.lower().str.split(expand=True).stack().replace('[^a-zA-Z\s]','',regex=True).value_counts().items()])
        counts2 = defaultdict(int,[[i,j] for i,j in df2.str.lower().str.split(expand=True).stack().replace('[^a-zA-Z\s]','',regex=True).value_counts().items()])
        prior = defaultdict(int,[[i,j] for i,j in df0.str.lower().str.split(expand=True).stack().replace('[^a-zA-Z\s]','',regex=True).value_counts().items()])
    else:
        counts1 = defaultdict(int,[[i,j] for i,j in df1.str.split(expand=True).stack().replace('[^a-zA-Z\s]','',regex=True).value_counts().items()])
        counts2 = defaultdict(int,[[i,j] for i,j in df2.str.split(expand=True).stack().replace('[^a-zA-Z\s]','',regex=True).value_counts().items()])
        prior = defaultdict(int,[[i,j] for i,j in df0.str.split(expand=True).stack().replace('[^a-zA-Z\s]','',regex=True).value_counts().items()])
    
    sigmasquared = defaultdict(float)
    sigma = defaultdict(float)
    delta = defaultdict(float)

    for word in prior.keys():
        prior[word] = int(prior[word] + 0.5)

    for word in counts2.keys():
        counts1[word] = int(counts1[word] + 0.5)
        if prior[word] == 0:
            prior[word] = 1

    for word in counts1.keys():
        counts2[word] = int(counts2[word] + 0.5)
        if prior[word] == 0:
            prior[word] = 1

    n1 = sum(counts1.values())
    n2 = sum(counts2.values())
    nprior = sum(prior.values())
    
    for word in prior.keys():
        if prior[word] > 0:
            l1 = float(counts1[word] + prior[word]) / (( n1 + nprior ) - (counts1[word] + prior[word]))
            l2 = float(counts2[word] + prior[word]) / (( n2 + nprior ) - (counts2[word] + prior[word]))
            sigmasquared[word] =  1/(float(counts1[word]) + float(prior[word])) + 1/(float(counts2[word]) + float(prior[word]))
            sigma[word] =  math.sqrt(sigmasquared[word])
            delta[word] = ( math.log(l1) - math.log(l2) ) / sigma[word]

    if verbose:
        for word in sorted(delta, key=delta.get)[:10]:
            print("%s, %.3f" % (word, delta[word]))

        for word in sorted(delta, key=delta.get,reverse=True)[:10]:
            print("%s, %.3f" % (word, delta[word]))
    return delta




def marked_words(df, target_val, target_col, unmarked_val,verbose=False):

    """Get words that distinguish the target group (which is defined as having 
    target_group_vals in the target_group_cols column of the dataframe) 
    from all unmarked_attrs (list of values that correspond to the categories 
    in unmarked_attrs)"""

    grams = dict()
    thr = 2 #z-score threshold

    subdf = df.copy()
    for i in range(len(target_val)):
        subdf = subdf.loc[subdf[target_col[i]]==target_val[i]]

    for i in range(len(unmarked_val)):
        delt = get_log_odds(subdf['text'], df.loc[df[target_col[i]]==unmarked_val[i]]['text'],df['text'],verbose) #first one is the positive-valued one
                
        c1 = []
        c2 = []
        for k,v in delt.items():
            if v > thr:
                c1.append([k,v])
            elif v < -thr:
                c2.append([k,v])

        if 'target' in grams:
            grams['target'].extend(c1)
        else:
            grams['target'] = c1
        if unmarked_val[i] in grams:
            grams[unmarked_val[i]].extend(c2)
        else:
            grams[unmarked_val[i]] = c2
    grams_refine = dict()

    for r in grams.keys():
        temp = []
        thr = len(unmarked_val) # must satisfy all intersections
        for k,v in Counter([word for word, z in grams[r]]).most_common():
            if v >= thr:
                z_score_sum = np.sum([z for word, z in grams[r] if word == k])
                temp.append([k, z_score_sum])

        grams_refine[r] = temp
    return grams_refine['target']


def main():
    parser = argparse.ArgumentParser(description="Just an example",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("filename", help="Generated personas file")
    parser.add_argument("--target_val",nargs="*", 
    type=str,
    default=[''], help="List of demographic attribute(s) for target group of interest")
    parser.add_argument("--target_col", nargs="*",
    type=str,
    default=[''],help="List of demographic categories that distinguish target group")
    parser.add_argument("--unmarked_val", nargs="*",
    type=str,
    default=[''],help="List of unmarked default values for relevant demographic categories")
    parser.add_argument("--verbose", action='store_true',help="If set to true, prints out top words calculated by Fightin' Words")

    args = parser.parse_args()

    filename = args.filename
    target_val = args.target_val
    target_col = args.target_col
    unmarked_val = args.unmarked_val

    assert len(target_val) == len(target_col) == len(unmarked_val)
    assert len(target_val) > 0
    df = pd.read_csv(filename)

    # Optional: filter out unwanted prompts
    # df = df.loc[~df['prompt'].str.contains('you like')]
    top_words = marked_words(df, target_val, target_col, unmarked_val,verbose=args.verbose)
    print("Top words:")
    print(top_words)

if __name__ == '__main__':
    
    main()
