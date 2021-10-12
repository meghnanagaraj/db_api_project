import sys,os
import argparse
import requests
import pandas as pd



def query(args=sys.argv[1:]):

    parser=argparse.ArgumentParser(description="Utility to query users data from database using REST API")
    
    parser.add_argument(
    "--tablename", 
    dest="tablename", 
    action="store",
    required=True,
    help="Query by table name"
    )
    parser.add_argument(
    "--filterby", 
    dest="filterby", 
    action="store",
    help="Query by column name and its value ex:<columnname>=<value1>,<value2>"
    )
    parser.add_argument(
    "--dbname", 
    dest="dbname", 
    action="store",
    required=True,
    help="Query by table name"
    )
    
    args = parser.parse_args(args)
    #print(args)
    #print(args.filterby)
    filter_dict={}
    if args.filterby:
        filterby_list=args.filterby.split(';')
        #print(filterby_list)
        temp_list=[]
        for item in filterby_list:
            temp_list.append(item.split('='))
        #print(temp_list)
        for k,v in temp_list:
            filter_dict[k]=v
        #print(filter_dict)

    url=f"http://localhost:5000/{args.dbname}/{args.tablename}?"
    print (url)

    for k,v in filter_dict.items():
        url = url + f"{k}={v}&"
    response = requests.get(url)
    try:
        result = response.json()
        if result:
            #print(result)
            print(pd.DataFrame(result))
        else:
            print("   - No Data found for the query")
    except:
        print("Please check your query")
    #os.system(f'curl -X GET {url}')


if __name__ == "__main__":
    query(sys.argv)






