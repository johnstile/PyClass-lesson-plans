#!/usr/bin/env python
'''Graph json data into plot'''

# for the json 
import json as j
# For the bar chart
import numpy as np
import matplotlib.pyplot as plt

def main():
    '''Parse json object into dictionary'''
    # container for the parsed date
    request_types_dict = {}
    
    # Data file
    data_file = 'testdata.json'
    
    # parse the date
    parse_data(data_file=data_file,data_dict=request_types_dict)

    # call plotting package
    plot(request_types_dict)

def parse_data(data_file=None,data_dict=None ):
    '''Parse the json file and populate a dictionary'''

    # data file
    f = data_file
    
    # Open file pointer to file
    with open(f) as fp:
        
        # read lines one at a time
        for file_line in fp:
            
            # convert line to a json object
            json_line = j.loads(file_line)

            # collect item of interest from json object
            request_type = json_line['request_type']
            
            #print "request_types: {}".format(request_type)

            # Return value of dict for this key, or zero if it does not exist
            times = data_dict.get(request_type, 0)
            
            # Increment counter
            times += 1
            
            # Set the value for this key
            data_dict[request_type] = times
            
            # times falls out of scope

    # Printout the the content of the dictionary
    print "{:<10}{}".format("Freq","Request Type")
    for key in sorted(data_dict.keys()):
        print "{:<10d}{}".format(data_dict[key], key)

    
def plot(data_dict=None):
    """
    Bar chart demo with pairs of bars grouped for easy comparison.
    """
    
    # create plot object
    fig, ax = plt.subplots()
    
    # create the orderd list
    key_list = []
    val_list = []
    
    # split 
    for k,v in sorted(data_dict.iteritems()):
        #print "k:{},v:{}".format(k,v)
        key_list.append(k)
        val_list.append(v)
        
        
    # set index to the number of keys in the dict
    index = np.arange(  len(data_dict.keys())  )
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(
        index,
        val_list,
        bar_width,
        alpha=opacity,
        color='b',
        #yerr=std_men,
        error_kw=error_config,
        label='request_type'
    )
    
    plt.xlabel('Type')
    plt.ylabel('Frequency')
    plt.title('Foodles')
    plt.xticks(index + bar_width, tuple(key_list),rotation='vertical')
    plt.legend()
    plt.tight_layout()
    plt.show()

   
if __name__ == "__main__":
    main()
    
