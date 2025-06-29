from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts

#EXP json的格式类似于字典，或者多个字典组成的列表
import json
json.dumps({"a":1}) # 转化python数据为json数据,可添加参数ensure_ascii=False来保证中文内容不被转义
json.loads('{"a":1}') # 转化json数据为python数据

#EXP 处理json格式
# 读入数据
us_f = open("./resource/折线图数据/美国.txt","r",encoding="UTF-8")
us_data = us_f.read()
us_f.close()

jp_f = open("./resource/折线图数据/日本.txt","r",encoding="UTF-8")
jp_data = jp_f.read()
jp_f.close()

in_f = open("./resource/折线图数据/印度.txt","r",encoding="UTF-8")
in_data = in_f.read()
in_f.close()


# 规范化为json格式
us_data = us_data.replace("jsonp_1629344292311_69436(","")
us_data = us_data[:-2]
jp_data = jp_data.replace("jsonp_1629350871167_29498(","")
jp_data = jp_data[:-2]
in_data = in_data.replace("jsonp_1629350745930_63180(","")
in_data = in_data[:-2]

# json转换为python的dict
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 分析获取必要信息
us_trend_data = us_dict["data"][0]["trend"]
x_data = us_trend_data["updateDate"][:314] #只取一年数据，前314个,三个国家时间一致，写一份
us_y_data = us_trend_data["list"][0]["data"][:314]

jp_trend_data = jp_dict["data"][0]["trend"]
jp_y_data = jp_trend_data["list"][0]["data"][:314]

in_trend_data = in_dict["data"][0]["trend"]
in_y_data = in_trend_data["list"][0]["data"][:314]

# 生成可视化图标

line =Line()
line.add_xaxis(x_data)
line.add_yaxis("美国确诊人数",us_y_data)
line.add_yaxis("日本确诊人数",jp_y_data)
line.add_yaxis("印度确诊人数",in_y_data)
line.render(path="./out/JSONrender.html")




