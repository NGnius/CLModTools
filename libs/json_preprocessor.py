import json, re

def preprocess_str(json_str):
    '''(str) -> str
    basically just removes all the trailing commas
    returns string that can be interpreted properly by the built-in Python json lib'''
    result = str(json_str)
    result.replace(" ", "")
    charnum = 0
    while charnum<len(result):
        if re.match(r"\s", result[charnum], re.I | re.M):
            #print(result[charnum])
            result = result[:charnum]+result[charnum+1:]
        else:
            charnum+=1
    result = result.replace(",}", "}")
    result = result.replace(",]", "]")
    return result


def preprocess_file(json_dir):
    '''(path-like str) -> None
    overwrites json at json_dir with a file that can be interpreted properly by Python json lib'''
    pass
