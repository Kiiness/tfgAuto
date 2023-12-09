import uiautomator2 as u2
import re
# 连接设备
d = u2.connect()

print(d.app_current())
