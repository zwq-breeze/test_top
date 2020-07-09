import json

from django.shortcuts import render,redirect,HttpResponse
from app.models import User_grade


def up_grade(request):
    """
    新增或更新客户分数
    :param request:
    :return: 是否更新成功
    """
    # if request.method == "GET":
    #     obj_list = User_grade.objects.values()
    #     # print(obj_list)
    #     return HttpResponse("ok")

    if request.method == "POST":
        # print(request.POST)
        user_name = request.POST.get("name")
        user_grade = request.POST.get("grade")
        obj = User_grade.objects.filter(name=user_name)
        if not obj:
            # 新增
            User_grade.objects.create(name=user_name, grade=float(user_grade))
        else:
            # 更新
            obj.update(name=user_name, grade=float(user_grade))
        return HttpResponse("updata grade ok")


def get_top(request):
    if request.method == "GET":
        start = request.GET.get('start')
        end = request.GET.get('end')
        current_user = request.GET.get('name')
        all_top = User_grade.objects.all().order_by('-grade').values("name", "grade")
        # print(all_top)
        # 当前客户端排名
        current_user_info = {}
        for index, item_dic in enumerate(list(all_top)):
            if item_dic["name"] == current_user:
                item_dic["ranking"] = index + 1
                item_dic["grade"] = float(item_dic["grade"])
                current_user_info = item_dic
        # top榜
        if start and end:
            start = int(start)
            end = int(end)
            if start < len(all_top) and end <= len(all_top):
                all_top = all_top[start-1:end]
            elif start < len(all_top) and end > len(all_top):
                all_top = all_top[start-1:len(all_top)]
            else:
                return HttpResponse("约束超过范围")
        else:
            start = 1

        top = list(all_top)
        for index, item_dic in enumerate(top):
            item_dic["ranking"] = start + index
            item_dic["grade"] = float(item_dic["grade"])

        res = {
            "top": top,
            "current_user_info": current_user_info
        }
        return HttpResponse(json.dumps(res, ensure_ascii=False))
