import json, os, collections, traceback, json_preprocessor

JSON_FILE_EXTENSIONS = (".json")

def find(directory, query):
    '''(path-like str, str) -> dict
    searches all .JSON files in dir for query
    returns dict of path-like string:[[path, in, json, to, query], [another, path, in, json, to, query]]'''
    result = dict()
    jsons = find_jsons(directory)
    for json_dir in jsons:
        pathes = find_in_json(json_dir, query)
        if pathes:
            result[json_dir]=pathes
    return result


def find_in_json(json_dir, query):
    '''(path-like str, str) -> list
    searches through the whole JSON for query
    returns list of list of path to string; one element in the top list per path'''
    try:
        with open(json_dir, 'r') as json_file:
            json_str = json_preprocessor.preprocess_str(json_file.read())
            return find_in_iterable(json.loads(json_str), query)
    except:
        print("Problem converting", json_dir, "to json")
        print("===== Contents =====")
        print(json_str)
        print("====================")
        traceback.print_exc()

def find_in_iterable(iterable, query):
    '''(iterable, str) -> list
    searches through the iterable (and any iterables contained within said iterable) for query
    returns list of list of path to string; one element in the top list per path; one element in the second highest list per sub-iterable'''
    result = list()
    count=0
    for item in iterable:
        if isinstance(item, collections.Iterable):
            if query in item:
                if isinstance(iterable, dict):
                    result.append([item, iterable[item]])
                else:
                    result.append([count, item])
            elif isinstance(item, collections.Iterable) and not isinstance(item, str):
                # if query not found and item is iterable, continue recursion
                returned = find_in_iterable(item, query)
                for i in returned:
                    if isinstance(i, list):
                        result.append([count]+i)
                    else:
                        result.append([count, i])
            elif isinstance(iterable, dict) and isinstance(iterable[item], collections.Iterable):
                # if query not found and item is iterable, continue recursion
                returned = find_in_iterable(iterable[item], query)
                for i in returned:
                    if isinstance(i, list):
                        result.append([item]+i)
                    else:
                        result.append([item, i])
        elif query == item:
            if isinstance(iterable, dict): # in case somebody is using integers (or floats or something else) as their dict keys, like an idiot
                result.append([item, iterable[item]])
            else:
                result.append([count, item])
        count+=1
    return result


def find_jsons(directory):
    '''(path-like str) -> list of path-like str
    searches from dir through any folders to find .JSON files
    returns list of pathes to .JSON files'''
    result = list()
    for (dirpath, dirnames, filenames) in os.walk(directory):
        for filename in filenames:
            if filename.split(".")[-1] in JSON_FILE_EXTENSIONS:
                result.append(dirpath+"/"+filename)
    return result

# TESTING
# print(find_jsons("/home/ngnius/Documents/CardLife"))
# print(find_in_iterable(["potato", ["potato", "watermelon"], ("potato", "potato", "watermelon", ["potatototototo", "banana", "potato"])], "pot"))
# print(find("/home/ngnius/Documents/CardLife", "RegrowthTime"))
