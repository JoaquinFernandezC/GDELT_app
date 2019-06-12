from scripts import mongo_connection
from itertools import product
events = mongo_connection.get_events_collection()

all_years = [2015,2016,2017,2018,2019]
all_months= list(range(1,13))
years_months = list(product(all_years,all_months))


pipeline = [
    {"$group":{"_id": {"year": {"$year": "$date"}, "month": {"$month":"$date"}},"avgTone": { "$avg": "$avg_tone" }}},
    {"$sort": {"_id.year":1, "_id.month": 1}}]
agg = list(events.aggregate(pipeline))
all_years = list(map(lambda x: x['_id']['year'], agg))
years =set(all_years)
labels_indexes =list( map(lambda year: all_years.index(year),years))
dates = list(map(lambda x: "{0}-{1}".format(x['_id']['year'], x['_id']['month']) if x['_id']['month'] == 1 else None, agg))
labels = list(map(lambda x: "{0}-{1}".format(x['_id']['year'], x['_id']['month']), agg))

tones = list(map(lambda x: x['avgTone'], agg))
print (labels,tones)