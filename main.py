import json
import pandas as pd
import matplotlib.pyplot as plt


def set_original_data():
    data = json.dumps({
        "data": [
            {
                "id": 3428793,
                "timestamp": "2019-01-12 14:34:34",
                "bytes": 12000,
                "value": 135,
            },
            {
                "id": 3428794,
                "timestamp": "2019-01-12 14:35:14",
                "bytes": 10000,
                "value": 85,
            },
            {
                "id": 3428795,
                "timestamp": "2019-01-12 14:37:40",
                "bytes": 18000,
                "value": 110,
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
    df = pd.DataFrame({list_x_name: list_x, list_y_name: list_y})

    # if it is 'time' value, use:
    df[list_x_name] = [pd.to_datetime(i) for i in df[list_x_name]]

    # additional print to check the correspondence
    print(df.sort_values(by=list_x_name))
    return df


def show(list_x, list_y):
    plt.bar(list_x, list_y)
    plt.grid()
    plt.show()


def demo_0():
    list_x_name = 'dates'  # dates
    list_y_name = 'bytes_values'  # bytes_values, values

    d = process_original_data(set_original_data())
    df = sort_by_(d[list_x_name], d[list_y_name])
    show(d[list_x_name], d[list_y_name])


def demo_1():
    list_x = [
        2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018
    ]
    list_y = [
        1657554647149.87,
        1578624060588.26,
        1282723881134.01,
        1363594369577.82,
        2059984158438.46,
        2297128039058.21,
        2210256976945.38,
        2051661732059.78,
        1524917468442.01,
    ]

    list_x_name = 'list_x'
    list_y_name = 'list_y'
    df = pd.DataFrame({list_x_name: list_x, list_y_name: list_y})
    print(df.sort_values(by=list_x_name))
    show(df[list_x_name], df[list_y_name])


if __name__ == "__main__":

    # demo_0()

    demo_1()

    print()
