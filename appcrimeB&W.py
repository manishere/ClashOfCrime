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
ipc1 = os.path.join('ipc1.json')
ipc2 = os.path.join('ipc2.json')
ipc3 = os.path.join('ipc3.json')
ipc4 = os.path.join('ipc4.json')
ipc5 = os.path.join('ipc5.json')
ipc6 = os.path.join('ipc6.json')
ipc7 = os.path.join('ipc7.json')
ipc8 = os.path.join('ipc8.json')
ipc9 = os.path.join('ipc9.json')
ipc10 = os.path.join('ipc10.json')
ipc11 = os.path.join('ipc11.json')
ipc12 = os.path.join('ipc12.json')
ipc13 = os.path.join('ipc13.json')

import json
from folium import plugins
from folium.plugins import FloatImage
import pandas

url = ('logo.JPG')

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
    "type":"FeatureCollection",
    "features":[
    {
        "type":"Feature",
        "id":"BIL",
        "properties":{
            "name":"Bilaspur","density":94.65
        },
        "geometry":{
            "type":"Polygon",
            "coordinates":[[[77.2719955444336,30.317321396948888],[77.26461410522461,30.311541992821706],[77.26203918457031,30.288717426233095],[77.28212356567383,30.275968928008236],[77.30890274047852,30.282639860425128],[77.3353385925293,30.294349955901886],[77.32486724853516,30.323248636828104],[77.29568481445312,30.336583615284862],[77.2719955444336,30.317321396948888]]]
        }
    },
    {
        "type":"Feature",
        "id":"BUR",
        "properties":{
            "name":"Buria","density":1.264
        },
        "geometry":{
            "type":"Polygon",
            "coordinates":[[[77.35241889953613,30.162345327420233],[77.34898567199706,30.15844924332155],[77.35053062438965,30.152697599728047],[77.36010074615479,30.150953486684084],[77.36327648162842,30.156334161771117],[77.36091613769531,30.162864793668167],[77.35241889953613,30.162345327420233]]]
        }
    },
    {
        "type":"Feature",
        "id":"CCH",
        "properties":{
            "name":"Chachrauli","density":57.05
        },
        "geometry":{
            "type":"Polygon",
            "coordinates":[[[77.34967231750487,30.247130460800545],[77.35061645507812,30.238158414085085],[77.36331939697266,30.23763934499742],[77.36795425415039,30.24920652019233],[77.35636711120605,30.25335850737292],[77.34967231750487,30.247130460800545]]]
        }
    },
    {
        "type":"Feature",
        "id":"CPR",
        "properties":{
            "name":"Chappar","density":56.43
        },
        "geometry":{
            "type":"Polygon",
            "coordinates":[[[77.15389251708984,30.22740570905255],[77.16204643249512,30.214055887606026],[77.17912673950195,30.21331417773627],[77.18084335327148,30.22362344359965],[77.16805458068848,30.234302406842193],[77.15389251708984,30.22740570905255]]]
        }
    },
    {
        "type":"Feature",
        "id":"FRK",
        "properties":{
            "name":"Farakpur","density":241.7
        },
        "geometry":{
            "type":"Polygon",
            "coordinates":[[[77.23955154418945,30.129427851351167],[77.24101066589355,30.12864838682423],[77.24401473999023,30.128407122747245],[77.24566698074341,30.131098111757005],[77.24384307861328,30.133399313136767],[77.24090337753296,30.13462412425315],[77.2374701499939,30.132137370635977],[77.23955154418945,30.129427851351167]]]
        }
    },
    {
        "type":"Feature",
        "id":"JUDS",
        "properties":{
            "name":"JagadhariSadar","density":49.33
        },
        "geometry":{
            "type":"Polygon",
            "coordinates":[[[77.25577354431152,30.184754097033277],[77.26624488830566,30.190318398887626],[77.26564407348633,30.18972488833379],[77.26581573486327,30.190837717688126],[77.26212501525879,30.19269240533443],[77.25431442260742,30.19276659211374],[77.24899291992188,30.185792790575192],[77.2492504119873,30.17525696254129],[77.25989341735838,30.176221557029574],[77.2679615020752,30.178744297972123],[77.27371215820312,30.18304764815116],[77.2671890258789,30.189873266307576],[77.25577354431152,30.184754097033277]]]
        }
    },
    {
        "type":"Feature",
        "id":"JUDC",
        "properties":{
            "name":"JagadhariCity","density":739.1
        },
        "geometry":{
            "type":"Polygon",
            "coordinates":[[[77.29353904724121,30.168207716212535],[77.29379653930664,30.163384257179096],[77.29551315307617,30.164497384057398],[77.29928970336914,30.15900583618957],[77.30684280395508,30.15900583618957],[77.31139183044434,30.165833119721185],[77.31122016906738,30.171546895744946],[77.30358123779297,30.17458916082585],[77.29602813720703,30.173179342342927],[77.29353904724121,30.168207716212535]]]
        }
    },
    {
        "type":"Feature",
        "id":"JTH",
        "properties":{
            "name":"Jathlana","density":464.3
        },
        "geometry":{
            "type":"Polygon",
            "coordinates":[[[77.26255416870117,30.0199085571309],[77.26856231689453,30.038931791730118],[77.26564407348633,30.064191379496272],[77.23886489868164,30.066122729827196],[77.21105575561523,30.05052228481701],[77.20161437988281,30.025705085640663],[77.21792221069336,30.011733389737664],[77.23474502563477,30.007125271177625],[77.26255416870117,30.0199085571309]]]
        }
    },
    {
        "type":"Feature",
        "id":"KHB",
        "properties":{
            "name":"Khijrabad","density":353.4
        },
        "geometry":{
            "type":"Polygon",
            "coordinates":[[[77.49069213867188,30.30561404478868],[77.5030517578125,30.327249321016218],[77.47936248779297,30.36606228674695],[77.44640350341797,30.35628642525117],[77.40520477294922,30.338805935152212],[77.40829467773438,30.30027858504304],[77.4477767944336,30.27270741823115],[77.47352600097656,30.277154904692335],[77.49069213867188,30.30561404478868]]]
        }
    },
    {
        "type":"Feature",
        "id":"RAD",
        "properties":{
            "name":"Radaur","density":169.5
        },
        "geometry":{
            "type":"Polygon",
            "coordinates":[[[77.11097717285156,30.042944038957167],[77.12642669677734,29.997759725578906],[77.15492248535156,30.00043568594731],[77.20024108886719,30.022732549250424],[77.20848083496094,30.041160838027047],[77.2005844116211,30.06136856891663],[77.1799850463867,30.069985317427758],[77.1514892578125,30.07652166068723],[77.1181869506836,30.06701410957684],[77.11097717285156,30.042944038957167]]]
        }
    },
    {
        "type":"Feature",
        "id":"SAD",
        "properties":{
            "name":"Sadhaura","density":19.15
        },
        "geometry":{
            "type":"Polygon",
            "coordinates":[[[77.16865539550781,30.398937557618677],[77.1847915649414,30.34295413059721],[77.22084045410156,30.331694334016003],[77.26993560791016,30.355990171771825],[77.28641510009766,30.384130245890272],[77.27577209472656,30.419367961416675],[77.21534729003906,30.435353990118514],[77.16865539550781,30.398937557618677]]]
        }
    },
    {
        "type":"Feature",
        "id":"YNRS",
        "properties":{
            "name":"YamunanagarSadar","density":231.5
        },
        "geometry":{
            "type":"Polygon",
            "coordinates":[[[77.28881835937499,30.106858007571685],[77.28508472442627,30.102811223996447],[77.29950428009033,30.092489319305255],[77.32967376708984,30.09256358146139],[77.33173370361328,30.1097908939199],[77.32147693634033,30.11892312160151],[77.3096752166748,30.121892769814163],[77.29903221130371,30.118143574149297],[77.29255199432373,30.113466160231077],[77.28881835937499,30.106858007571685]]]
        }
    },
    {
        "type":"Feature",
        "id":"YNRC",
        "properties":{
            "name":"YamunanagarCity","density":231.5
        },
        "geometry":{
            "type":"Polygon",
            "coordinates":[[[77.29087829589844,30.115730650183107],[77.29259490966797,30.12040795686984],[77.30615615844727,30.124565376855344],[77.30873107910156,30.13673967129206],[77.3022937774658,30.143568496127823],[77.29199409484863,30.138224238628784],[77.28349685668945,30.131098111757005],[77.27877616882324,30.12196700987537],[77.29087829589844,30.115730650183107]]]
        }
    }
    ]
}

stamen = folium.Map(location=[30.374, 77.310], zoom_start=9.5, tiles="Stamen Toner")

FloatImage(url, bottom=0.7, left=86.3).add_to(stamen)

plugins.Search(yamunanagar, search_zoom=10, geom_type='Polygon').add_to(stamen)

folium.Marker(
    location=[30.29, 77.29],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis1)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.719688, 76.900044],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(ipc1)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.159, 77.360],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis2)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.719987, 76.9951],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(ipc2)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.244, 77.363],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis3)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.7190, 77.0859],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(ipc3)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.220, 77.171],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis4)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.7203, 77.1727],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(ipc4)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.133, 77.240],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis5)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.7169, 77.2553],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(ipc5)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.168, 77.301],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis6)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.7169, 77.3254],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(ipc6)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.023, 77.249],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis7)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.717, 77.4286],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(ipc7)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.29, 77.48],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis8)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.7169, 77.5016],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(ipc8)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.040, 77.170],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis9)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.7180, 77.5745],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(ipc9)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.38, 77.22],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis10)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.7156, 77.6461],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(ipc10)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.10, 77.30],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(vis11)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.7129, 77.7120],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(ipc11)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.7017, 77.7841],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(ipc12)), width=450, height=250))
).add_to(stamen)

folium.Marker(
    location=[30.7099, 77.8432],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(ipc13)), width=450, height=250))
).add_to(stamen)

fgd = folium.FeatureGroup(name="COLOR:CrimeDetails")

for lts, lns, ses, acs, pcs in zip(lats, lons, secs, acts, pocs):
    fgd.add_child(folium.CircleMarker(location=[lts, lns], radius = 41, popup=str(acs)+"  :  "+str(pcs),
    fill_color=color_producer(ses), fill=True,  color = 'grey', fill_opacity=0.7))
	
fgc = folium.FeatureGroup(name="CrimesinYNR")

for lt, ln, se, ac, pc in zip(lat, lon, sec, act, poc):
    fgc.add_child(folium.CircleMarker(location=[lt, ln], radius = 7, popup=str(ac)+" , Occured At :-  "+str(pc),
    fill_color=color_producer(se), fill=True,  color = 'grey', fill_opacity=2))

fgp = folium.FeatureGroup(name="INDIAMap")

fgp.add_child(folium.GeoJson(data=(open('india-composite.geojson', 'r', encoding='utf-8-sig').read())))  #Added a new child of GeoJson and in 'r',read mode &ENCODING REQUIRED

stamen.add_child(fgd)
stamen.add_child(fgc)
stamen.add_child(fgp)
stamen.add_child(folium.LayerControl())

stamen.save("MapCrimeB&W.html")
