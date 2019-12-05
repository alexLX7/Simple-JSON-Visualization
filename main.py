import json
import pandas as pd
import matplotlib.pyplot as plt


def set_original_data():
    data = json.dumps({
            "data":[
                {
                    "id":3428793,
                    "timestamp":"2019-01-12 14:34:34",
                    "bytes":12000,
                    "value":135,
                }
                ,
                {
                    "id":3428794,
                    "timestamp":"2019-01-12 14:35:14",
                    "bytes":10000,
                    "value":85,
                }
                ,
                {
                    "id":3428795,
                    "timestamp":"2019-01-12 14:37:40",
                    "bytes":18000,
                    "value":110,
                }
            ]
        })
    return data
    
    
def process_original_data(data_as_dict: dict):
    data = json.loads(data_as_dict)
    d = dict(
        dates=[i['timestamp'] for i in data['data']],
        bytes_values=[i['bytes'] for i in data['data']],
        values=[i['value'] for i in data['data']]
    )
    return d


def sort_by_(list_x, list_y):
    list_x_name = 'list_x'
    list_y_name = 'list_y'
    df = pd.DataFrame({list_x_name:list_x, list_y_name:list_y})
    
    # if its time value, use:
    df[list_x_name]  = [pd.to_datetime(i) for i in df[list_x_name]]
    
    # additional print to check correspondence
    print(df.sort_values(by=list_x_name))
    return df


def show(list_x, list_y):
    plt.bar(list_x, list_y)
    plt.show()


def demo():
    list_x_name = 'dates' # dates
    list_y_name = 'bytes_values' # bytes_values, values
    
    d = process_original_data(set_original_data())
    df = sort_by_(d[list_x_name], d[list_y_name])
    
    show(d[list_x_name], d[list_y_name])


if __name__ == "__main__":
    
    demo()
    
    print()
    