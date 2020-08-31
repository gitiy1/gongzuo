import re

# 登录地址
LOGIN_URL = 'https://my.freenom.com/dologin.php'

# 域名状态地址
DOMAIN_STATUS_URL = 'https://my.freenom.com/domains.php?a=renewals'

# 域名续期地址
RENEW_DOMAIN_URL = 'https://my.freenom.com/domains.php?submitrenewals=true'

# token 正则
token_ptn = re.compile('name="token" value="(.*?)"', re.I)

# 域名信息正则
domain_info_ptn = re.compile(
    r'<tr><td>(.*?)</td><td>[^<]+</td><td>[^<]+<span class="[^<]+>(\d+?).Days</span>[^&]+&domain=(\d+?)">.*?</tr>',
    re.I)

# 登录状态正则
login_status_ptn = re.compile('<a href="logout.php">Logout</a>', re.I)
