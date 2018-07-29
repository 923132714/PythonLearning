
import ssl
import urllib3
import http
from bs4 import BeautifulSoup
import xlsxwriter

#import workbook

def download(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    http = urllib3.PoolManager();
                                                                                                                                                                   # ip = ['121.34.156.197', '175.31.128.78', '124.219.217.120'];

    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64)'r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'https://www.douban.com/doulist/240962/?start=50&sort=seq&sub_type=',
        'Connection': 'keep-alive',
                                                                                                                                                                       # 'X-Forwarded-For': ip[0]
    }

    r = http.request("GET",url,headers=headers);#

    return r.data.decode('utf-8')
#用beautiful soup解析
def BeautifulSouplist(html):
    result= [];
    soup = BeautifulSoup(html, "lxml")

    #print(html);

    s = soup.find_all("div", "bd doulist-subject")#获得所有的
     
    if s == []:
        print('null')
        return None;

    else:

        #print(len(s))

        sz = len(s)

        for j in range(1, sz + 1):

            sp = BeautifulSoup(str(s[j - 1]))                                                                                                                  #, "html.parser"

            movie = [];

            #print("========")

            #print(sp)

            #print("========")

            imageurl = sp.img['src']  # 电影的封面

            bookUrl = sp.a['href']  # 电影的详细链接地址

            bookName = "";  # 电影的名字

            pingfen = "";  # 电影的评分

            movieYear = "";  # 电影的年份

            actors = "";

            books = sp.find_all("div", "title");#div的class是"title"的标签，返回的是数组。

            for book in books:

                bookName = book.a.string.strip()  #strip()，默认删除空白符（包括'\n', '\r',  '\t',  ' ')            

            infos = sp.div.find_all("span")

            # print(infos[1].string)

            pingfen = infos[1].string;

            # print((infos[2].string))

            abss = sp.find_all("div", "abstract");

            tag_soup = sp.find(class_="abstract")

            arr = tag_soup.contents;

            print(arr);

            k = 0;

            for string in arr:

                ss = str(string).strip();

                if not (ss == "<br/>"):

                    # print(ss)

                    if k == 1:

                        actors = ss;

                    if k == 4:

                        movieYear = ss;

                    k = k + 1;

            """
            print("=============")

            print(imageurl)

            print(bookUrl)

            print(str(bookName))

            print(str(movieYear))

            print(pingfen)

            print("=============")
            """


            movie.append(bookName);

            movie.append(actors);

            movie.append(movieYear);

            movie.append(pingfen);

            movie.append(bookUrl);

            movie.append(imageurl);

            #print(movie)

            result.append(movie);
            print(result)
        pass;

 

    return 1;
def test(html):
    soup = BeautifulSoup(html, "lxml")

   # print(html);

    s = soup.find_all("div", "bd doulist-subject")
    print(s)
    return 0
html=download(r'https://www.douban.com/doulist/240962/?start=50&sort=seq&sub_type=')
#BeautifulSouplist(download(r'https://www.douban.com/doulist/240962/?start=50&sort=seq&sub_type='))

#test(html)
BeautifulSouplist(html)