import json


def load_data(filepath):
    with open(filepath, 'r') as js:  # открываем файл на чтение
        python_data = json.load(js) # загружаем из файла данные в словарь
        js.close()  # Закрываем файл
        return python_data

def get_biggest_bar(data):
    max_siats = 0
    max_bar = ''
    for bar in data:
        if int(bar['SeatsCount']) > max_siats:
            max_siats = bar['SeatsCount']
            max_bar = bar['Name']
    return max_bar

def get_smallest_bar(data):
    min_siats = 9999999999999
    min_bar = ''
    for bar in data:
        if int(bar['SeatsCount']) < min_siats:
            min_siats = bar['SeatsCount']
            min_bar = bar['Name']
    return min_bar

def get_closest_bar(data, longitude, latitude):
    closest_bar = ''
    minimal_differences = 9999.0
    for bar in data:
        differences = (float(bar['Longitude_WGS84'])-longitude) ** 2 +\
                        (float(bar['Latitude_WGS84'])-latitude) ** 2
        if differences < minimal_differences:
            minimal_differences = differences
            closest_bar = bar['Name']
    return closest_bar


if __name__ == '__main__':
    latitude = float(input('Введите широту: '))
    longitude = float(input('Введите долготу: '))
    json_file = 'data-2897-2016-11-23.json'
    data_from_json = load_data(json_file)
    biggest_bar = get_biggest_bar(data_from_json)
    smallest_bar = get_smallest_bar(data_from_json)
    closest_bar = get_closest_bar(data_from_json, longitude, latitude)
    print ('Самый большой бар: ', biggest_bar)
    print ('Самый маленьикй бар: ', smallest_bar)
    print('самый близкий бар: ', closest_bar)