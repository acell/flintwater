import csv
import json

with open('residential_test_data_reduced.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[:-1] for rows in reader}

data = []
entry = {}
geojson = {}
results = []
geojson["type"] = "FeatureCollection"

for entry in mydict.keys():
    try:
        # print(mydict[entry])
        d = float((mydict[entry][28]))
        c = (float(mydict[entry][29]))
        e = float(mydict[entry][1])


        row = {}
        for y in range(0, 39):
            try:
                row[y] = mydict[entry][y]
            except:
                row[y]= "N/A"
        # print(row)

        resultInfo = {}
        resultInfo["type"] = "Feature"
        entry = {}
        latlon = []
        # lon = float(mydict[entry][29])
        # lat = float(mydict[entry][28])
        latlon.append(c)
        latlon.append(d)
        addressInfo = {}
        addressInfo["type"] = "Point"
        addressInfo["coordinates"] = latlon
        resultInfo["geometry"] = addressInfo
        entry["PID"] = row[0]
        entry["copper"] = row[2]
        entry["lead"] = row[3]
        entry["zip"] = row[4]
        entry["owner_type"] = row[5]
        entry["owner_state"] = row[6]
        entry["homestead"] = row[7]
        entry["homestead_pct"] = row[8]
        entry["home_SEV"] = row[9]
        entry["land_value"] = row[10]
        entry["land_improvements"] = row[11]
        entry["res_bldg_value"] = row[12]
        entry["res_style"] = row[13]
        entry["commercial"] = row[14]
        entry["bldg_storeys"] = row[15]
        entry["parcel_acres"] = row[16]
        entry["rental"] = row[17]
        entry["use_type"] = row[18]
        entry["prop_class"] = row[19]
        entry["old_prop_class"] = row[20]
        entry["year_built"] = row[21]
        entry["usps_vacancy"] = row[22]
        entry["zoning"] = row[23]
        entry["future_landuse"] = row[24]
        entry["draft_zone"] = row[25]
        entry["housing_condition_2012"] = row[26]
        entry["housing_condition_2014"] = row[27]
        entry["commercial_condiiton_2013"] = row[28]
        entry["latitude"] = row[29]
        entry["longitude"] = row[30]
        entry["hydrant_type"] = row[31]
        entry["ward"] = row[32]
        entry["precinct"] = row[33]
        entry["centract"] = row[34]
        entry["cenblock"] = row[35]
        entry["sl_type"] = row[36]
        entry["sl_type2"] = row[37]
        entry["sl_lead"] = row[38]
        entry["lead"] = e

        data.append(entry)

        resultInfo["properties"] = entry
        resultInfo["type"] = "Feature"
        results.append(resultInfo)
    except:
        pass

geojson["features"] = results

# print(geojson)

with open('flintdata.geojson', 'w') as outfile:
    json.dump(geojson, outfile)
