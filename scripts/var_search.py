import sys
sys.path.append('../libs/')
sys.path.append('libs/')
import json_searcher

PATH_INDICATOR = ">>"
ASSOCIATION_INDICATOR = ":"
DEFAULT_DIRECTORY = "C:\\Games\\CardLife"

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
                    results_out+=str(result[i])
                else:
                    results_out+=str(result[i])+PATH_INDICATOR
            results_out+="\n"
    if results_out == "":
        results_out="No results"
    return results_out
another = True
while another:
    query = input("What term would you like to search for? ")
    directory = input("Where would you like to look for it? ")
    if directory == "":
        directory = DEFAULT_DIRECTORY
    print("Searching...")
    results = json_searcher.find(directory, query)
    print("Results")
    print(process_results(results))
    response = get_input("Another query? [Y/n]")
    if response == "n":
        another = False
