import threading
import requests
from pymongo import MongoClient
from time import sleep


uri1 = 'mongodb://54.229.58.205:27017'
uri2 = 'mongodb://52.31.97.5:27017'


def get_noise_data(position_num):
    print(position_num)
    url_noise = 'http://dublincitynoise.sonitussystems.com/applications/api/dublinnoisedata.php?location='+ str(position_num)
    url_position = 'http://dublincitynoise.sonitussystems.com/applications/api/dublinnoisedata.php?returnLocationStrings=true&location=' + str(position_num)
    r_noise = requests.get(url_noise)
    r_position = requests.get(url_position)
    r_noise_dict = r_noise.json()
    noise_list = r_noise_dict['aleq']
    current_noise = noise_list[-1]
    date_list = r_noise_dict["dates"]
    current_date = date_list[-1]
    time_list = r_noise_dict['times']
    current_time = time_list[-1]

    if position_num != 15:
        noise_data = [position_num, current_noise, r_position.text, current_date, current_time]
    else:
        noise_data = [position_num, current_noise, 'Mellows Park', current_date, current_time]

    print(noise_data)
    return noise_data


def write_noise_data(uri_1, uri_2):
    client1 = MongoClient(uri_1)
    db1 = client1.wayfindr
    client2 = MongoClient(uri_2)
    db2 = client2.wayfindr
    while(1):
        if is_master(uri_1) == 1:
            for position in range(1, 16):
                noise_list = get_noise_data(position)
                db1.Noise_Data.update_one({'Position_Number': noise_list[0]},
                                      {"$set": {"Noise_Index": noise_list[1], 'Position_Name': noise_list[2],
                                                'Date': noise_list[3], 'Time': noise_list[4]}}, upsert=True)
            print("\nMachine 1 is the primary, has written noise data to machine 1.\n")
            print("Will request data after 5 minutes ...\n")
            sleep(5 * 60)
        else:
            for position in range(1, 16):
                noise_list = get_noise_data(position)
                db2.Noise_Data.update_one({'Position_Number': noise_list[0]},
                                      {"$set": {"Noise_Index": noise_list[1], 'Position_Name': noise_list[2],
                                                'Date': noise_list[3], 'Time': noise_list[4]}}, upsert=True)
            print("\nMachine 2 is the primary, has written noise data to machine 2.\n")
            print("Will request data after 5 minutes ...\n")
            sleep(5 * 60)


# https://docs.mongodb.com/manual/reference/method/db.collection.watch/
def updating_listener(uri_1, uri_2):
    client1 = MongoClient(uri_1)
    db1 = client1.wayfindr
    client2 = MongoClient(uri_2)
    db2 = client2.wayfindr
    while(1):
        if is_master(uri_1) == 1:
            print("Machine 1 is the primary, listening to the updating.\n")
            cursor = db2.Noise_Data.watch(full_document='updateLookup')
            document = next(cursor)
            print(document)
            print("\nData has been updated, flag has been reset as 1.\n")
            db1.Trigger.update_one({'flag of noise data': '1: changed; 0: not changed.'}, {'$set': {'value': 1}},
                                  upsert=True)
        else:
            print("Machine 2 is the primary, listening to the updating.\n")
            cursor = db1.Noise_Data.watch(full_document='updateLookup')
            document = next(cursor)
            print(document)
            print("\nData has been updated, flag has been reset as 1.\n")
            db2.Trigger.update_one({'flag of noise data': '1: changed; 0: not changed.'}, {'$set': {'value': 1}},
                                  upsert=True)


def is_master(uri):
    client = MongoClient(uri)
    doc = client.admin.command('ismaster')
    r = doc['ismaster']
    return r


def updating_listener_iteration():
    try:
        updating_listener(uri1, uri2)
    except:
        print('###############################')
        print('#Primary data set has changed.#')
        print('###############################\n')
    else:
        updating_listener_iteration()


def main():
    t1 = threading.Thread(target=write_noise_data, args=(uri1, uri2))
    t1.start()
    # t1.join()
    while(1):
        updating_listener_iteration()


if __name__ == '__main__':
    main()
