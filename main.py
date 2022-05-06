import requests
import json
import pandas as pd
import openpyxl
from datetime import datetime
from ids import *

# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%b_%d_%Y_%Hh_%M")
print("date and time =", dt_string)

excel_name = "fox"


CHANNEL = "https://discord.com/api/v9/channels/"
AUTHORIZATION = authorization
CHANNEL_ID = channel_id
LIMIT = "100"


def retrieve_messages(chan_id):
    headers = {
        "authorization": AUTHORIZATION
    }
    r = requests.get(f"{CHANNEL}{chan_id}/messages?limit={LIMIT}", headers=headers)
    json_file = json.loads(r.text)
    the_json = r.json()
    # print(the_json)
    print(len(the_json))
    # print(type(the_json))
    # print(the_json)


    messages_list = []
    for value in the_json:
        message_dictionary = {}
        # print(type(el))
        # print(value["timestamp"], "|", value["author"]["username"], ": ", value["content"])
    # for value in json_file:
        # print(value["timestamp"], "|", value["author"]["username"], ": ", value["content"])
        # print(value, "\n")
        message_dictionary["time"] = value["timestamp"]
        message_dictionary["author"] = value["author"]["username"]
        message_dictionary["message"] = value["content"]

        messages_list.append(message_dictionary)
    df = pd.DataFrame(messages_list)
    return df
    # print(messages_list)


new_df = retrieve_messages(CHANNEL_ID)

print(new_df.columns)

# frequency count of column A
count = new_df['author'].value_counts()
print("ranking in terms of messages frequency")
print(count)

count.to_excel(f"msg_count_{excel_name}_{dt_string}.xlsx", sheet_name='num msg')
