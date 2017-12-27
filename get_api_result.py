import requests
from requests.auth import HTTPDigestAuth
from requests.auth import HTTPBasicAuth
import json

'''
    This program is useful to get the result set from an API
    API should render the result in json format
    You have to install requests, json  packages

    Args:
        None

    Returns:
        Result set from teh requested API end point in the specified result file
'''

def getdatafromapi(api_endpoint, user_id, user_password):
    '''
    This module is useful to get the result set from an API
    API should render the result in json format
    You have to install requests, json  packages

    Args:
        api_endpoint: URL for API
        user_id: USER ID required to access the API
        user_password: PASSWORD required to access the API

    Returns:
        returnvalue: -1 if there was an error, 1 otherwise
        jsonobject: result set or exception error details

    '''

    auth = HTTPDigestAuth(user_id, user_password)
    requests.packages.urllib3.disable_warnings()



    try:
        r = requests.get(api_endpoint, auth=auth, verify=False)
        filejsonobject = json.loads(r.text)
        return 1, filejsonobject
    except Exception as inst:

        return -1, inst



def main():
    import pprint



    user_id = str(input("Enter the user id : "))
    print(user_id)
    user_password = str(input("Enter the user password : "))
    print(user_password)
    api_endpoint = str(input("Enter the API endpoint : "))
    print(api_endpoint)
    filename = str(input("Enter name of the file where results will be stored  : "))
    print(filename)

    returnvalue, jsonobject = getdatafromapi(api_endpoint, user_id, user_password)


    if returnvalue == -1:
        print("Sorry could not fetch results: \n" + str(jsonobject))
    else:
        print("Result  Fetched Successfully. Check FileName: " + filename )
        with open(filename, "w") as resultfile_fp:
            pp = pprint.PrettyPrinter(indent=4, stream=resultfile_fp)
            pp.pprint(jsonobject)



    return


if __name__== '__main__':
        main()
