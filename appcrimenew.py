import folium
import os

vis1 = os.path.join('vis1.json')
vis2 = os.path.join('vis2.json')
vis3 = os.path.join('vis3.json')
vis4 = os.path.join('vis4.json')
vis5 = os.path.join('vis5.json')
vis6 = os.path.join('vis6.json')
vis7 = os.path.join('vis7.json')
vis8 = os.path.join('vis8.json')
vis9 = os.path.join('vis9.json')
vis10 = os.path.join('vis10.json')
vis11 = os.path.join('vis11.json')
interpolate = os.path.join('interpolate.json')
stroke = os.path.join('stroke.json')

import json
from folium import plugins
from folium.plugins import FloatImage
from folium.features import CustomIcon
import pandas

url1 = ('logo2.JPG')
url2 = ('C.JPG')
url3 = ('caption2.JPG')

icon_image1 = ('1.jpg')
icon_image2 = ('2.jpg')
icon_image3 = ('3.jpg')
icon_image4 = ('4.jpg')
icon_image5 = ('5.jpg')
icon_image6 = ('6.jpg')
icon_image7 = ('7.jpg')


icon1 = CustomIcon(
    icon_image1,
    icon_size=(90, 70),  #size of image
    icon_anchor=(5, -18)#right / left image
)

icon2 = CustomIcon(
    icon_image2,
    icon_size=(90, 70),
    icon_anchor=(5, -16)
)

icon3 = CustomIcon(
    icon_image3,
    icon_size=(90, 70),
    icon_anchor=(5, -15)
)

icon4 = CustomIcon(
    icon_image4,
    icon_size=(90, 70),
    icon_anchor=(5, -13)
)

icon5 = CustomIcon(
    icon_image5,
    icon_size=(90, 70),
    icon_anchor=(5, -8)
)

icon6 = CustomIcon(
    icon_image6,
    icon_size=(90, 70),
    icon_anchor=(6, -13)
)

icon7 = CustomIcon(
    icon_image7,
    icon_size=(90, 70),
    icon_anchor=(7, 5)
)



data = pandas.read_csv("crime.csv")
lat = list(data["LATITUDE"])
lon = list(data["LONGITUDE"])
act = list(data["Acts"])
sec = list(data["Section"])
poc = list(data[" Place of Occurrence"])

data = pandas.read_csv("crimedetails.csv")
lats = list(data["LATITUDES"])
lons = list(data["LONGITUDES"])
acts = list(data["ActsS"])
secs = list(data["SectionS"])
pocs = list(data[" Place of OccurrenceS"])


def color_producer(the_section):
    if the_section < 60:
        return 'green'
    elif the_section == 61:
        return 'orange'
    elif the_section == 67:
        return 'red'
    elif the_section == 148:
        return 'purple'
    elif the_section == 279:
        return 'grey'
    elif the_section == 304:
        return 'beige'
    elif the_section == 338:
        return 'cadetblue'
    elif the_section == 354:
        return 'darkblue'
    elif the_section == 363:
        return 'pink'
    elif the_section == 379:
        return 'lightgreen'
    elif the_section == 420:
        return 'white'
    elif the_section == 454:
        return 'black'
    else:
        return 'blue'


yamunanagar = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "id": "BIL",
            "properties": {
                "name": "Bilaspur", "density": 94.65
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[
              77.19165802001953,
              30.323841341092574
            ],
            [
              77.2503662109375,
              30.268556249047727
            ],
            [
              77.36984252929688,
              30.2910890570962
            ],
            [
              77.35198974609375,
              30.34088005484784
            ],
            [
              77.27148056030273,
              30.362877833108154
            ],
            [
              77.19165802001953,
              30.323841341092574
            ]]]
            }
        },
        {
            "type": "Feature",
            "id": "BUR",
            "properties": {
                "name": "Buria", "density": 1.264
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[
              77.32941627502441,
              30.139040741145017
            ],
            [
              77.37018585205078,
              30.148244483998933
            ],
            [
              77.36769676208496,
              30.167910894779403
            ],
            [
              77.35499382019043,
              30.182454093784802
            ],
            [
              77.33757019042969,
              30.18482828979236
            ],
            [
              77.31963157653809,
              30.182973454050956
            ],
            [
              77.32340812683105,
              30.170656458930967
            ],
            [
              77.32941627502441,
              30.139040741145017
            ]]]
            }
        },
        {
            "type": "Feature",
            "id": "CCH",
            "properties": {
                "name": "Chachrauli", "density": 57.05
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[
              77.36984252929688,
              30.289606794526495
            ],
            [
              77.25045204162598,
              30.268185600405772
            ],
            [
              77.266845703125,
              30.235340577517942
            ],
            [
              77.31937408447266,
              30.229111389015017
            ],
            [
              77.37979888916016,
              30.21665182811735
            ],
            [
              77.4319839477539,
              30.244831915307145
            ],
            [
              77.38391876220703,
              30.295832146790442
            ],
            [
              77.36984252929688,
              30.289606794526495
            ]]]
            }
        },
        {
            "type": "Feature",
            "id": "CPR",
            "properties": {
                "name": "Chappar", "density": 56.43
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[
              77.18650817871094,
              30.182528288276167
            ],
            [
              77.23388671874999,
              30.221101852485987
            ],
            [
              77.2119140625,
              30.259067203213018
            ],
            [
              77.16110229492188,
              30.274486436999464
            ],
            [
              77.11715698242186,
              30.243052359289663
            ],
            [
              77.10479736328125,
              30.19617912354204
            ],
            [
              77.13226318359375,
              30.167094631229592
            ],
            [
              77.15972900390625,
              30.167094631229592
            ],
            [
              77.18650817871094,
              30.182528288276167
            ]]]
            }
        },
        {
            "type": "Feature",
            "id": "FRK",
            "properties": {
                "name": "Farakpur", "density": 241.7
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[
              77.21895217895508,
              30.136220067448416
            ],
            [
              77.22959518432617,
              30.121224606751863
            ],
            [
              77.25088119506836,
              30.11350328343571
            ],
            [
              77.26341247558594,
              30.126569784666128
            ],
            [
              77.27079391479492,
              30.136220067448416
            ],
            [
              77.26615905761719,
              30.149728878245902
            ],
            [
              77.2445297241211,
              30.154478789727992
            ],
            [
              77.22633361816405,
              30.151213250155838
            ],
            [
              77.21895217895508,
              30.136220067448416
            ]]]
            }
        },
        {
            "type": "Feature",
            "id": "JUDC",
            "properties": {
                "name": "JagadhariCity", "density": 739.1
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[
              77.26607322692871,
              30.1499515354564
            ],
            [
              77.26581573486327,
              30.15061950407233
            ],
            [
              77.28418350219727,
              30.17228892027792
            ],
            [
              77.30976104736328,
              30.157002087161636
            ],
            [
              77.32503890991211,
              30.157002087161636
            ],
            [
              77.31903076171875,
              30.184605711347437
            ],
            [
              77.3374843597412,
              30.18534763754125
            ],
            [
              77.35456466674805,
              30.18267667709129
            ],
            [
              77.34512329101562,
              30.222585149205642
            ],
            [
              77.26615905761719,
              30.234154095850688
            ],
            [
              77.23594665527344,
              30.221398513619437
            ],
            [
              77.21019744873047,
              30.20122351857044
            ],
            [
              77.24899291992188,
              30.18697985549699
            ],
            [
              77.26607322692871,
              30.1499515354564
            ]]]
            }
        },
        {
            "type": "Feature",
            "id": "JTH",
            "properties": {
                "name": "Jathlana", "density": 464.3
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[
              77.19002723693848,
              30.037074214842445
            ],
            [
              77.19665765762329,
              30.02278828512759
            ],
            [
              77.19416856765747,
              30.018143521213833
            ],
            [
              77.19509124755858,
              30.01738175916562
            ],
            [
              77.24143981933594,
              29.979620759272258
            ],
            [
              77.28538513183594,
              30.001624978505664
            ],
            [
              77.30392456054688,
              30.034919382026448
            ],
            [
              77.26959228515625,
              30.06909396443887
            ],
            [
              77.22118377685547,
              30.068796844991812
            ],
            [
              77.19002723693848,
              30.037074214842445
            ]]]
            }
        },
        {
            "type": "Feature",
            "id": "KHB",
            "properties": {
                "name": "Khijrabad", "density": 353.4
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[
              77.43202686309814,
              30.245239725689075
            ],
            [
              77.52639770507812,
              30.306503259848835
            ],
            [
              77.5250244140625,
              30.364581158417973
            ],
            [
              77.48794555664062,
              30.393014902255455
            ],
            [
              77.44674682617188,
              30.40959743218008
            ],
            [
              77.39181518554688,
              30.351546261929034
            ],
            [
              77.38417625427245,
              30.295980364647217
            ],
            [
              77.43202686309814,
              30.245239725689075
            ]]]
            }
        },
        {
            "type": "Feature",
            "id": "RAD",
            "properties": {
                "name": "Radaur", "density": 169.5
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[
              77.1126937866211,
              30.013814405372617
            ],
            [
              77.13088989257812,
              29.99151553746812
            ],
            [
              77.17758178710938,
              29.988541976503846
            ],
            [
              77.19646453857422,
              30.022732549250424
            ],
            [
              77.18547821044922,
              30.046213157299167
            ],
            [
              77.15011596679688,
              30.068796844991812
            ],
            [
              77.11784362792969,
              30.058991402837037
            ],
            [
              77.10582733154297,
              30.042349642213367
            ],
            [
              77.1126937866211,
              30.013814405372617
            ]]]
            }
        },
        {
            "type": "Feature",
            "id": "SAD",
            "properties": {
                "name": "Sadhaura", "density": 19.15
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[
              77.22152709960938,
              30.53032794236421
            ],
            [
              77.16934204101562,
              30.484183951487754
            ],
            [
              77.17208862304686,
              30.454592956980054
            ],
            [
              77.10479736328125,
              30.45932812026586
            ],
            [
              77.12677001953125,
              30.37761431777479
            ],
            [
              77.19131469726562,
              30.324285866937423
            ],
            [
              77.27096557617188,
              30.363396239603716
            ],
            [
              77.31216430664061,
              30.433281874927655
            ],
            [
              77.22152709960938,
              30.53032794236421
            ]]]
            }
        },
        {
            "type": "Feature",
            "id": "YNRC",
            "properties": {
                "name": "YamunanagarCity", "density": 231.5
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[
              77.26622343063354,
              30.14976598781588
            ],
            [
              77.27113723754883,
              30.136368525968606
            ],
            [
              77.26422786712646,
              30.1269038486786
            ],
            [
              77.2547435760498,
              30.11707632658816
            ],
            [
              77.2507095336914,
              30.112909310487694
            ],
            [
              77.24289894104004,
              30.11587913951386
            ],
            [
              77.21603393554688,
              30.08899893504956
            ],
            [
              77.23620414733885,
              30.069391082993874
            ],
            [
              77.27002143859863,
              30.069836759153798
            ],
            [
              77.2829818725586,
              30.05691133569448
            ],
            [
              77.33104705810547,
              30.09404881287048
            ],
            [
              77.32938408851624,
              30.138957235515985
            ],
            [
              77.32598304748534,
              30.155925982916532
            ],
            [
              77.31019020080565,
              30.15581466111752
            ],
            [
              77.28418350219727,
              30.170879068888674
            ],
            [
              77.26622343063354,
              30.14976598781588
            ]]]
            }
        }
    ]
}

stamen = folium.Map(location=[30.221896, 77.298825], zoom_start=10, tiles="Cartodb Positron")


plugins.Fullscreen(
    position='topleft',
    title='Expand me',
    title_cancel='Exit me',
    force_separate_button=True).add_to(stamen)

FloatImage(url1, bottom=0.08, left=87.4).add_to(stamen)

FloatImage(url2, bottom=19, left=82.5).add_to(stamen)

FloatImage(url3, bottom=93, left=7.7).add_to(stamen)



plugins.Search(yamunanagar, search_zoom=10, geom_type='Polygon').add_to(stamen)



folium.Marker(
    location=[30.50666, 76.52114],
    icon=icon1,
    popup=folium.Popup(max_width=500).add_child(
        folium.Vega(json.load(open(interpolate)), width=500, height=260))
).add_to(stamen)

folium.CircleMarker(
    location=[30.445122, 76.672211],
    radius=13,
    fill_color='purple',
    color='purple',
    popup=folium.Popup(max_width=500).add_child(
        folium.Vega(json.load(open(stroke)), width=500, height=260))
).add_to(stamen)

folium.Marker(
    location=[30.423809, 76.522522],
    icon=icon2,
    popup=folium.Popup(max_width=500).add_child(
        folium.Vega(json.load(open(interpolate)), width=500, height=260))
).add_to(stamen)

folium.CircleMarker(
    location=[30.362211, 76.674957],
    radius=13,
    fill_color='grey',
    color='grey',
    popup=folium.Popup(max_width=500).add_child(
        folium.Vega(json.load(open(stroke)), width=500, height=260))
).add_to(stamen)

folium.Marker(
    location=[30.345621, 76.523895],
    icon=icon3,
    popup=folium.Popup(max_width=500).add_child(
        folium.Vega(json.load(open(interpolate)), width=500, height=260))
).add_to(stamen)

folium.CircleMarker(
    location=[30.28516, 76.68045],
    radius=13,
    fill_color='cadetblue',
    color='cadetblue',
    popup=folium.Popup(max_width=500).add_child(
        folium.Vega(json.load(open(stroke)), width=500, height=260))
).add_to(stamen)

folium.Marker(
    location=[30.266184, 76.523895],
    icon=icon4,
    popup=folium.Popup(max_width=500).add_child(
        folium.Vega(json.load(open(interpolate)), width=500, height=260))
).add_to(stamen)

folium.CircleMarker(
    location=[30.216355, 76.683197],
    radius=13,
    fill_color='lightgreen',
    color='lightgreen',
    popup=folium.Popup(max_width=500).add_child(
        folium.Vega(json.load(open(stroke)), width=500, height=260))
).add_to(stamen)

folium.Marker(
    location=[30.184057, 76.523895],
    icon=icon5,
    popup=folium.Popup(max_width=500).add_child(
        folium.Vega(json.load(open(interpolate)), width=500, height=260))
).add_to(stamen)

folium.CircleMarker(
    location=[30.142752, 76.683197],
    radius=13,
    fill_color='beige',
    color='grey',
    popup=folium.Popup(max_width=500).add_child(
        folium.Vega(json.load(open(stroke)), width=500, height=260))
).add_to(stamen)

folium.Marker(
    location=[30.108306, 76.526642],
    icon=icon6,
    popup=folium.Popup(max_width=500).add_child(
        folium.Vega(json.load(open(interpolate)), width=500, height=260))
).add_to(stamen)

folium.CircleMarker(
    location=[30.063151, 76.685944],
    radius=13,
    fill_color='black',
    color='black',
    popup=folium.Popup(max_width=500).add_child(
        folium.Vega(json.load(open(stroke)), width=500, height=260))
).add_to(stamen)

folium.Marker(
    location=[30.017976, 76.529388],
    icon=icon7,
    popup=folium.Popup(max_width=500).add_child(
        folium.Vega(json.load(open(interpolate)), width=500, height=260))
).add_to(stamen)

folium.CircleMarker(
    location=[29.988245, 76.68869],
    radius=13,
    fill_color='orange',
    color='orange',
    popup=folium.Popup(max_width=500).add_child(
        folium.Vega(json.load(open(stroke)), width=500, height=260))
).add_to(stamen)





folium.Marker(
    location=[30.29, 77.29],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis1)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.159, 77.360],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis2)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.244, 77.363],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis3)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.220, 77.171],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis4)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.133, 77.240],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis5)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.168, 77.301],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis6)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.023, 77.249],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis7)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.29, 77.48],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis8)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.040, 77.170],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis9)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.38, 77.22],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis10)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.10, 77.30],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis11)), width=450, height=250))
).add_to(stamen)

fgc = folium.FeatureGroup(name="CrimesinYNR")

for lt, ln, se, ac, pc in zip(lat, lon, sec, act, poc):
    fgc.add_child(folium.CircleMarker(location=[lt, ln], radius=7, popup=str(ac) + " , Occured At :-  " + str(pc),
                                      fill_color=color_producer(se), fill=True, color='grey', fill_opacity=2))

stamen.add_child(fgc)
stamen.add_child(folium.LayerControl())

stamen.save("MapCrimeNew.html")

