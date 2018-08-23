# -*- coding: utf-8 -*-

# Scrapy settings for jjbooks project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jjbooks'

SPIDER_MODULES = ['jjbooks.spiders']
NEWSPIDER_MODULE = 'jjbooks.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jjbooks (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
COOKIE = {'JJEVER': '%7B%22isKindle%22%3A%22%22%7D', 'Hm_lvt_f73ac53cbcf4010dac5296a3d8ecf7cb': '1533389717,1533473895', 'kohanasession': 'prte5fuvt9v6u2qnk4193nc7n4', 'CNZZDATA30079898': 'cnzz_eid%3D1703677789-1533468945-https%253A%252F%252Fwap.jjwxc.net%252F%26ntime%3D1533468945', 'kohanasession_data': 'c2Vzc2lvbl9pZHxzOjI2OiJwcnRlNWZ1dnQ5djZ1MnFuazQxOTNuYzduNCI7dG90YWxfaGl0c3xpOjE7X2tmX2ZsYXNoX3xhOjA6e311c2VyX2FnZW50fHM6MTA5OiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXT1c2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzY3LjAuMzM5Ni45OSBTYWZhcmkvNTM3LjM2IjtpcF9hZGRyZXNzfHM6MTQ6IjIyMy43My4yMjQuMTYxIjtsYXN0X2FjdGl2aXR5fGk6MTUzMzQ3MzkyMjtjYXB0Y2hhX3Jlc3BvbnNlfHM6NDA6ImUxYTQ0NWQyNjM2YTk3ZGU4Yjc5ZWYyZThiN2ZmMDg2MGQ5MWQ4NTUiOw%3D%3D', 'Hm_lpvt_f73ac53cbcf4010dac5296a3d8ecf7cb': '1533473922', 'UM_distinctid': '1650a2b05c67ba-03d35892952cc5-5e442e19-144000-1650a2b05c82d4'}

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jjbooks.middlewares.JjbooksSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jjbooks.middlewares.JjbooksDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'jjbooks.pipelines.JjbooksPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
