import requests
from urllib.parse import urlencode
# 余票查询模块

class Check():
    def __init__(self, date, start, end, purpose):
        self.base_url = 'https://kyfw.12306.cn/otn/leftTicket/queryA?'
        self.url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018'
        self.date = date
        self.start_station = start
        self.end_station = end
        if purpose == '学生':
            self.purpose = '0X00'
        else:
            self.purpose = purpose

        #查找出车站的英文简称，用于构造cookie、完整的余票查询链接
    def look_up_station(self):
        response1 = requests.get(self.url)
        a = response1.text.split('@')
        a.pop(0)
        for each in a:
            i = each.split('|')
            if self.start_station == i[1]:
                self.start_station = i[2]
            elif self.end_station == i[1]:
                self.end_station = i[2]
        return [self.start_station, self.end_station]

    def get_info(self):
        start_end = self.look_up_station()
        #构造请求参数
        data = {
        'leftTicketDTO.train_date':self.date,
        'leftTicketDTO.from_station':start_end[0],
        'leftTicketDTO.to_station':start_end[1],
        'purpose_codes':self.purpose
        }
        url = self.base_url + urlencode(data)
        response = requests.get(url)
        json = response.json()
        maps = json['data']['map']
        count = 0       #用于对车次编号
        for each in json['data']['result']:
            count += 1
            s = each.split('|')[3:]
            info = {
            'train':s[0],
            'start_end':maps[s[3]] + '-' + maps[s[4]],
            'time':s[5] + '-' + s[6],
            '历时':s[7],
            '一等座':s[-5],
            '二等座':s[-6]
            }
            try:
                #余票的结果有3种：有、一个具体的数字(如：18、6等)、无，判断如果余票是有或者一个具体的数字就直接输出对应的车次信息，然后返回
                if info['二等座'] == '有' or int(info['二等座']):
                    print('[%d]' % count, info)
                    return count
            except ValueError:
                continue
