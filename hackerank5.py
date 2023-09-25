from functools import reduce
import numpy as np

def mostActive(customers):
    # Write your code here
    customers_list = []
    hun_percent_customers = len(customers)
    #print(hun_percent_customers)
    for each_customer in customers:
        customers_list.append(each_customer)
        
    customers_arr = np.array(customers_list)
    values, counts = np.unique(customers_arr,return_counts=True)
    print(values,counts)

    each_count_percentage = []
    for each_count in counts:
        each_count_percentage.append(100 * float(each_count)/float(hun_percent_customers))

    value_counts_dict = {}
    for each_value, each_count in zip(values,each_count_percentage):
        if each_count>=5:
            value_counts_dict[each_value]=each_count

    print(value_counts_dict)

    sorted_dict = dict(sorted(value_counts_dict.items(), key=lambda x: x[0]))
    sorted_final_list = list(sorted_dict.keys())
    return sorted_final_list    


customers=['new','Alpha','Beta','Gamma','Gamma','Alpha','Gamma','Beta']

print(mostActive(customers))