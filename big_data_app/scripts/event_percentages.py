from scripts import mongo_connection

events = mongo_connection.get_events_collection()
event_base_codes = map(lambda x: str(x), range(1,21))
labels = []
counts = []
for event_base_code in event_base_codes:

    count = events.find({'event_code':event_base_code}).count()
    if count>0:
        labels.append(event_base_code)
        counts.append(count)

total = sum(counts)


print (labels)
percentajes =[]
for i in counts:
    percentajes.append(i/total*100)

print (percentajes)
