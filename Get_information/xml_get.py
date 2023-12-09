import uiautomator2 as u2

d = u2.connect()

xml = d.dump_hierarchy()

with open('ui1.xml', 'w', encoding='utf-8') as f:
    f.write(xml)