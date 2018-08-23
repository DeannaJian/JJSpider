# -*- coding: utf-8 -*-


class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict


if __name__ == "__main__":
    cookie = "Hm_lvt_f73ac53cbcf4010dac5296a3d8ecf7cb=1533389717,1533473895; UM_distinctid=1650a2b05c67ba-03d35892952cc5-5e442e19-144000-1650a2b05c82d4; CNZZDATA30079898=cnzz_eid%3D1703677789-1533468945-https%253A%252F%252Fwap.jjwxc.net%252F%26ntime%3D1533468945; JJEVER=%7B%22isKindle%22%3A%22%22%7D; kohanasession=prte5fuvt9v6u2qnk4193nc7n4; kohanasession_data=c2Vzc2lvbl9pZHxzOjI2OiJwcnRlNWZ1dnQ5djZ1MnFuazQxOTNuYzduNCI7dG90YWxfaGl0c3xpOjE7X2tmX2ZsYXNoX3xhOjA6e311c2VyX2FnZW50fHM6MTA5OiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXT1c2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzY3LjAuMzM5Ni45OSBTYWZhcmkvNTM3LjM2IjtpcF9hZGRyZXNzfHM6MTQ6IjIyMy43My4yMjQuMTYxIjtsYXN0X2FjdGl2aXR5fGk6MTUzMzQ3MzkyMjtjYXB0Y2hhX3Jlc3BvbnNlfHM6NDA6ImUxYTQ0NWQyNjM2YTk3ZGU4Yjc5ZWYyZThiN2ZmMDg2MGQ5MWQ4NTUiOw%3D%3D; Hm_lpvt_f73ac53cbcf4010dac5296a3d8ecf7cb=1533473922"

    trans = transCookie(cookie)
    print trans.stringToDict()

    '''Result:
    {'JJEVER': '%7B%22isKindle%22%3A%22%22%7D', 'Hm_lvt_f73ac53cbcf4010dac5296a3d8ecf7cb': '1533389717,1533473895', 'kohanasession': 'prte5fuvt9v6u2qnk4193nc7n4', 'CNZZDATA30079898': 'cnzz_eid%3D1703677789-1533468945-https%253A%252F%252Fwap.jjwxc.net%252F%26ntime%3D1533468945', 'kohanasession_data': 'c2Vzc2lvbl9pZHxzOjI2OiJwcnRlNWZ1dnQ5djZ1MnFuazQxOTNuYzduNCI7dG90YWxfaGl0c3xpOjE7X2tmX2ZsYXNoX3xhOjA6e311c2VyX2FnZW50fHM6MTA5OiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXT1c2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzY3LjAuMzM5Ni45OSBTYWZhcmkvNTM3LjM2IjtpcF9hZGRyZXNzfHM6MTQ6IjIyMy43My4yMjQuMTYxIjtsYXN0X2FjdGl2aXR5fGk6MTUzMzQ3MzkyMjtjYXB0Y2hhX3Jlc3BvbnNlfHM6NDA6ImUxYTQ0NWQyNjM2YTk3ZGU4Yjc5ZWYyZThiN2ZmMDg2MGQ5MWQ4NTUiOw%3D%3D', 'Hm_lpvt_f73ac53cbcf4010dac5296a3d8ecf7cb': '1533473922', 'UM_distinctid': '1650a2b05c67ba-03d35892952cc5-5e442e19-144000-1650a2b05c82d4'}
    '''
