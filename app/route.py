from app import test_app
from flask import render_template

# PyEcharts数据可视化（1）——配置项
# https://blog.csdn.net/shi_jiaye/article/details/130347614
#
# PyEcharts数据可视化（2）——图表1
# https://blog.csdn.net/shi_jiaye/article/details/130369563

# numpy基本知识
# https://blog.csdn.net/shi_jiaye/article/details/112973431
#
# Pandas基础知识
# https://blog.csdn.net/shi_jiaye/article/details/113195919

# matplotlib基本知识
# https://blog.csdn.net/shi_jiaye/article/details/112912551


@test_app.route('/')
def index():
    return render_template("index.html")


# 画echart图
from random import randrange
from pyecharts import options as opts
from pyecharts.charts import Bar

from pyecharts.charts import Pie
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode

# # 随机产生同属性的7个名词
# Faker.choose()
#
# Faker.values()  # 随机的7个数
#
# # 组合数据
# list(zip(Faker.choose(),Faker.values()))

def drawPie():
    c = (
        Pie()
        .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])#可更改
        .set_colors(["blue", "green", "cyan", "red", "pink", "orange", "purple"])#颜色可添加
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-标题"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        # .render("简单多饼状图.html")
    )
    print([list(z) for z in zip(Faker.choose(), Faker.values())])  # 数据格式参考
    return c


fn = """
    function(params) {
        if(params.name == '其他')
            return '\\n\\n\\n' + params.name + ' : ' + params.value + '%';
        return params.name + ' : ' + params.value + '%';
    }
    """

def new_label_opts():
    return opts.LabelOpts(formatter=JsCode(fn), position="center")


def drawPieDuo():

    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(["剧情", "其他"], [25, 75])],
            center=["20%", "30%"],
            radius=[60, 80],
            # label_opts=new_label_opts(),
        )
        .add(
            "",
            [list(z) for z in zip(["奇幻", "其他"], [24, 76])],
            center=["55%", "30%"],
            radius=[60, 80],
            # label_opts=new_label_opts(),
        )
        .add(
            "",
            [list(z) for z in zip(["爱情", "其他"], [14, 86])],
            center=["20%", "70%"],
            radius=[60, 80],
            # label_opts=new_label_opts(),
        )
        .add(
            "",
            [list(z) for z in zip(["惊悚", "其他"], [11, 89])],
            center=["55%", "70%"],
            radius=[60, 80],
            # label_opts=new_label_opts(),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Pie-多饼图基本示例"),
            legend_opts=opts.LegendOpts(
                type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
            ),
        )
        # .render("mutiple_pie.html")
    )
    return c

def bar_base() -> Bar:
    LA = [11,22,33,44,55,66]
    LB = [33,22,55,77,99,88]
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A",LA)
        .add_yaxis("商家B",LB)
        # .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        # .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c

@test_app.route("/bar")
def test():
    return render_template("bar.html")

@test_app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()

@test_app.route("/pie")
def pie():
    return render_template("pie.html")

@test_app.route("/pieChart")
def get_pie_chart():
    c = drawPie()
    opt = c.dump_options_with_quotes()
    print(opt)
    return opt


# drawPieDuo 多个饼图
@test_app.route("/pieduo")
def PieDuo():
    return render_template("pieduo.html")

@test_app.route("/PieDuoChart")
def get_PieDuo_chart():
    c = drawPieDuo()
    return c.dump_options_with_quotes()