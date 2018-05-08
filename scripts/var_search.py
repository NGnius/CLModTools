import sys
sys.path.append('../libs/')
sys.path.append('libs/')
import json_searcher

PATH_INDICATOR = ">>"
ASSOCIATION_INDICATOR = ":"

def get_input(prompt, options={"y", "n", ""}):
    '''covenience function for nagging users for an input'''
    response = input(prompt)
    while response not in options:
        response = input(prompt)
    return response

def process_results(results_in):
    results_out = ""
    for filepath in results:
        results_out += filepath+"\n"
        for result in results_in[filepath]:
            results_out += "\t"+str(result[-2])+ASSOCIATION_INDICATOR+str(result[-1])+" in "
            for i in range(len(result)-2):
                if i == len(result)-3:
                    results_out+=result[i]+"\n"
                else:
                    results_out+=result[i]+PATH_INDICATOR
    return results_out
another = True
while another:
    query = input("What term would you like to search for? ")
    directory = '/home/ngnius/Documents/CardLife' #input("Where would you like to look for it? ")
    results = json_searcher.find(directory, query)
    print(process_results(results))
    response = get_input("Refine query? [Y/n]")
    if response == "n":
        another = False
