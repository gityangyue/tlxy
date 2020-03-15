import configparser

#第一步生成相应的ConfiguParser的实例
cfg = configparser.ConfigParser()

#生成之后需要读入相应的配置文件
cfg.read("cfg_test.cfg", encoding='UTF-8')

sp_name = cfg.get("SmallPlane", "name")
print(sp_name)

sp_width = cfg.getint("SmallPlane", "width")
print(sp_width)