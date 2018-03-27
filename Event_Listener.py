import requests
from pymongo import MongoClient
from time import sleep


# Connect to mongo
# uri = "mongodb://way:findr@54.194.175.227:27017/wayfindr?authMechanism=SCRAM-SHA-1"
# client = MongoClient(uri)
client = MongoClient('mongodb://54.229.58.205:27017')
db = client.wayfindr
collection = db.Noise_Data


def get_noise_data(position_num):
    print(position_num)
    url_noise = 'http://dublincitynoise.sonitussystems.com/applications/api/dublinnoisedata.php?location='+ str(position_num)
    url_position = 'http://dublincitynoise.sonitussystems.com/applications/api/dublinnoisedata.php?returnLocationStrings=true&location=' + str(position_num)

    r_noise = requests.get(url_noise)
    r_position = requests.get(url_position)
    # print('Status code:', r.status_code)

    r_noise_dict = r_noise.json()
    # print(r_noise_dict.keys())
    noise_list = r_noise_dict['aleq']
    current_noise = noise_list[-1]
    date_list = r_noise_dict["dates"]
    current_date = date_list[-1]
    time_list = r_noise_dict['times']
    current_time = time_list[-1]
    # print(current_noise)
    # print(current_date)
    # print(current_time)
    # print(r_position.text)

    if position_num != 15:
        noise_data = [position_num, current_noise, r_position.text, current_date, current_time]
    else:
        noise_data = [position_num, current_noise, 'Mellows Park', current_date, current_time]

    print(noise_data)
    return noise_data


def main():
    while True:
        for position in range(1,16):
            noise_list = get_noise_data(position)
            collection.update_one({'Position_Number': noise_list[0]}, {"$set": {"Noise_Index": noise_list[1],'Position_Name': noise_list[2],
                                                                                'Date':noise_list[3], 'Time': noise_list[4]}}, upsert = True)
        sleep(5*60)


if __name__ == '__main__':
    main()
