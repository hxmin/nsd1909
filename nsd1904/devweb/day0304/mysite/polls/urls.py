from django.conf.urls import url
from . import views   # 相对导入，导入当前目录中的views模块

urlpatterns = [
    # 正则表达式^$匹配空串，它从http://x.x.x.x/polls/后面开始匹配
    # 匹配到的URL，将调用views.index函数
    # name='index'，是给http://x.x.x.x/polls/起的名
    url(r'^$', views.index, name='index'),
]
