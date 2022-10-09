# from bs4 import BeautifulSoup
# import requests
# from fake_useragent import UserAgent
#
# url = "https://browser-info.ru/"
#
# req = requests.get(url).text
# # print(req)
# # print(type(req))
#
# soup = BeautifulSoup(req, "lxml")
# block = soup.find("div", id="tool_padding")
# check_js = block.find("div", id="javascript_check")
# result_js = check_js.find_all("span")
# print(result_js)
#
# total = result_js[1].get_text()
# print(total)
#
# ua = UserAgent()
# print(ua.random)


a = 123456789
b = f"{a:,}"
print(b)