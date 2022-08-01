from encodings import utf_8

import requests

import pandas as pd

application_key='b6209a9e7f6b840538c6416af6199d99'

# input_filename ="下载的数据.xls"
#
# output_filename="result.xls"
#
# txt = pd.read_excel(input_filename,engine="xlrd")

def getParam():

    # url = 'http://api.tianditu.gov.cn/geocoder?ds={"keyWord":"'+searchWord+'"}&tk='+application_key
    # url = 'http://api.tianditu.gov.cn/v2/search?postStr={"keyWord":"北京大学","dataTypes":"110100","level":12,"mapBound":"116.02524,39.83833,116.65592,39.99185","queryType":1,"start":0,"count":10}&type=query&tk='+application_key
    # url = 'http://api.tianditu.gov.cn/geocoder?postStr={"lon":116.37304,"lat":39.92594,"ver":1}&type=geocode&tk='+application_key
    # url = ‘https://api.map.baidu.com/reverse_geocoding/v3/?ak=wsdVftuokWcVsGIyOqR2nMwKW13UMQI1&output=json&coordtype=wgs84ll&location=31.225696563611,121.49884033194’
    # url = "https://api.map.baidu.com/reverse_geocoding/v3/?ak=wsdVftuokWcVsGIyOqR2nMwKW13UMQI1&output=json&coordtype=wgs84ll&location=31.225696563611,121.49884033194"
    url = "http://api.map.baidu.com/telematics/v2/reverserGeocoding/?ak=ZlLK3cDNkqTGLeU7qhTgUlZv&coordtype=wgs84ll&location=31.225696563611,121.49884033194"
    try:

        response = requests.request('GET',url)

        response.encoding = 'utf-8'

        location = response.json()

        print(location)

        # print(location['pois'][1]['name'])
        # print(location['pois'][1]['typeCode'])

        # return location['location']
        return

    except Exception as ex:

        print(ex)

    # csvFile = open('error.csv','a',encoding='utf-8')
    #
    # csvFile.write(url+',')

    return ''

# shp_lat_list = []
#
# shp_lon_list = []
#
# for address in txt.values:
#
#      shape = getParam(address[4].strip())
#
#      #print(shape)
#
#      shp_lat_list.append(shape['lat'])
#
#      print(shp_lat_list)
#
#      shp_lon_list.append(shape['lon'])
#
# txt['lat'] = shp_lat_list
#
# txt['lon'] = shp_lon_list
#
# txt.to_excel(output_filename)

if __name__ == '__main__':
    getParam()