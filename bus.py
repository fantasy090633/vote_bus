# coding=utf-8
import urllib
import urllib2
import cookielib

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
url = 'http://www.njgjjt.com/bus/Default.aspx?BusNo=YG-6851&BusCode=3'
values = {
    '__VIEWSTATE': '/wEPDwUJOTAyMzQ1MjYzD2QWAgIBD2QWBAIBDxAPFggeCkRhdGFNZW1iZXIFBVRhYmxlHg1EYXRhVGV4dEZpZWxkBQdPUFROQU1FHg5EYXRhVmFsdWVGaWVsZAUFT1BUSUQeC18hRGF0YUJvdW5kZ2QQFQMe56S86K6p5paR6ams57q/77yM5paH5piO6KGM6L2mHuacjeWKoeaAgeW6puWlve+8jOivreiogOW5s+WSjB7ljavnlJ/muIXmtIHkuq7vvIznjq/looPoiJLpgIIVAwI1MQI1MgI1MxQrAwNnZ2dkZAIDDxAPFggfAAUFVGFibGUfAQUHT1BUTkFNRR8CBQVPUFRJRB8DZ2QQFQMe5paR6ams57q/5LqJ5oqi77yM5oCl5YGc5oCl5Yi5HuaAgeW6puS4jeWSjOWWhO+8jOivtOivneeUn+ehrB7ljavnlJ/kuI3muIXmtIHvvIzmnInmsLTmnInlnqIVAwI1NAI1NQI1NhQrAwNnZ2dkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WCAUPQ2hlY2tCb3hMaXN0MSQwBQ9DaGVja0JveExpc3QxJDEFD0NoZWNrQm94TGlzdDEkMgUPQ2hlY2tCb3hMaXN0MSQyBQ9DaGVja0JveExpc3QyJDAFD0NoZWNrQm94TGlzdDIkMQUPQ2hlY2tCb3hMaXN0MiQyBQ9DaGVja0JveExpc3QyJDLKtGAd8leHmM7eq1wrrOwXEkmxhysmgvQvvi32rWpCoA==',
    '__EVENTVALIDATION': '/wEWCQKB57DKCALww6rJCgKLrcjeBAK68e6eBgLtw6rJCgKIrcjeBAK38e6eBgLs0bLrBgKM54rGBkmWj6/3nQq8g/X6Mgy6kdowp+BHEcBwH4mq6o2jfXUZ',
    'CheckBoxList1$0': 'on',
    'CheckBoxList1$1': 'on',
    'CheckBoxList1$2': 'on',
    'TextBox1': '',
    'Button1': '提交'
}
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = opener.open(req)
page = response.read()
print page