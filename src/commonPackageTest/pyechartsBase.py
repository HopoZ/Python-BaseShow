from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts


line = Line() # 创建折线图对象
line.add_xaxis(["a","b","c"]) # 设置x轴
line.add_yaxis("y",[1,2,3]) # 设置y轴
line.set_global_opts(
    title_opts=TitleOpts(title="基本示例",pos_left="center",pos_bottom="1%"), # 设置标题并且设置标题位置
    legend_opts=LegendOpts(is_show=True), # 配置图例的各种属性
    toolbox_opts=ToolboxOpts(is_show=True), # 配置工具箱
    visualmap_opts=VisualMapOpts(is_show=True) # 配置视觉映射
)


line.render(path="./out/render.html") #渲染对象并保存为html文件
