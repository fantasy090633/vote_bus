# coding=utf-8
import urllib
import urllib2
import cookielib

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
url = 'http://www.njgjjt.com/bus/Default.aspx?BusNo=YG-6832&BusCode=2'
values = {
    '__VIEWSTATE': '/wEPDwULLTE2MzYyMDczMTcPZBYCAgMPZBYEAgEPEA8WCB4KRGF0YU1lbWJlcgUFVGFibGUeDURhdGFUZXh0RmllbGQFB09QVE5BTUUeDkRhdGFWYWx1ZUZpZWxkBQVPUFRJRB4LXyFEYXRhQm91bmRnZBAVAx7npLzorqnmlpHpqaznur/vvIzmlofmmI7ooYzovaYe5pyN5Yqh5oCB5bqm5aW977yM6K+t6KiA5bmz5ZKMHuWNq+eUn+a4hea0geS6ru+8jOeOr+Wig+iIkumAghUDAjUxAjUyAjUzFCsDA2dnZ2RkAgMPEA8WCB8ABQVUYWJsZR8BBQdPUFROQU1FHwIFBU9QVElEHwNnZBAVAx7mlpHpqaznur/kuonmiqLvvIzmgKXlgZzmgKXliLke5oCB5bqm5LiN5ZKM5ZaE77yM6K+06K+d55Sf56GsHuWNq+eUn+S4jea4hea0ge+8jOacieawtOacieWeohUDAjU0AjU1AjU2FCsDA2dnZ2RkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYIBQ9DaGVja0JveExpc3QxJDAFD0NoZWNrQm94TGlzdDEkMQUPQ2hlY2tCb3hMaXN0MSQyBQ9DaGVja0JveExpc3QxJDIFD0NoZWNrQm94TGlzdDIkMAUPQ2hlY2tCb3hMaXN0MiQxBQ9DaGVja0JveExpc3QyJDIFD0NoZWNrQm94TGlzdDIkMi9LRdpo9kbx0L21f1StByGtXg3rlORLoWuSW7pMUQV7',
    '__EVENTVALIDATION': '/wEWCQKz5NKLAwLww6rJCgKLrcjeBAK68e6eBgLtw6rJCgKIrcjeBAK38e6eBgLs0bLrBgKM54rGBrHYoRYjMswSAFnJa0IcvRlVcuXLXL1y4SATTdCvUfc2',
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
# print response.geturl()
print page