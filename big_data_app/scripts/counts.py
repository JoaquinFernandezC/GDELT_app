from scripts import mongo_connection

events = mongo_connection.get_events_collection()

goldsteins = list(range(-10,11))
counts = []
for goldstein in goldsteins:
    counts.append(events.find({'goldstein_scale':goldstein}).count())

print (goldsteins)
print (counts)


tones = list(range(-10,11))
counts = []
for tone in tones:
    counts.append(events.find({'goldstein_scale':tone}).count())

print (tones)
print (counts)

