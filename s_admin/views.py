from django.shortcuts import render, redirect

from django.contrib import messages
from s_admin.forms import *
from s_admin.models import *


def admin_login(request):
    return render(request, "s_admin/login.html")


def admin_login_check(request):
    ausername = request.POST.get("admin_username")
    apassword = request.POST.get("admin_password")
    try:
        AdminLoginModel.objects.get(username=ausername, password=apassword)
        request.session['status'] = True
        return redirect('admin_home')

    except AdminLoginModel.DoesNotExist:
        messages.error(request, "Sorry Invalid Details")
        return redirect('admin_login')


def admin_home(request):
    return render(request, "s_admin/admin_home.html")


def admin_logout(request):
    request.session['status'] = False
    return redirect('admin_login')


# ----------------------------------------------------------------------------------------------------------------------------
# State <===============================

def open_state(request):
    return render(request, 's_admin/open_state.html', {"sf": StateForm(), "sdata": StateModel.objects.all()})


def save_state(request):
    sf = StateForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_state')
    else:
        return render(request, "s_admin/open_state.html", {"sf": sf})


def update_state(request):
    sno = request.GET.get("sno")
    sname = request.GET.get("sname")
    d1 = {"sno": sno, "sname": sname}
    return render(request, "s_admin/open_state.html", {"update_data": d1, "sdata": StateModel.objects.all()})


def update_state_data(request):
    sno = request.POST.get("s1")
    sname = request.POST.get("s2")
    StateModel.objects.filter(state_no=sno).update(state_name=sname)
    return redirect('open_state')


def delete_state(request):
    sno = request.GET.get("sno")
    StateModel.objects.filter(state_no=sno).delete()
    return redirect('open_state')


# ----------------------------------------------------------------------------------------------------------------------------

# City <=================

def open_city(request):
    return render(request, 's_admin/open_city.html', {"sf": CityForm(), "sdata": CityModel.objects.all()})


def save_city(request):
    sf = CityForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_city')
    else:
        return render(request, "s_admin/open_city.html", {"sf": sf})


def update_city(request):
    sno = request.GET.get("sno")
    sname = request.GET.get("sname")
    d1 = {"sno": sno, "sname": sname}
    return render(request, "s_admin/open_city.html", {"update_data": d1, "sdata": CityModel.objects.all()})


def update_city_data(request):
    sno = request.POST.get("s1")
    sname = request.POST.get("s2")
    CityModel.objects.filter(state_no=sno).update(state_name=sname)
    return redirect('open_city')


def delete_city(request):
    sno = request.GET.get("sno")
    CityModel.objects.filter(state_no=sno).delete()
    return redirect('open_city')


# -----------------------------------------------------------------------------------------------------------------
# Area <==============

def open_area(request):
    return render(request, 's_admin/open_area.html', {"sf": AreaForm(), "sdata": AreaModel.objects.all()})


def save_area(request):
    sf = AreaForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_area')
    else:
        return render(request, "s_admin/open_area.html", {"sf": sf})


def update_area(request):
    sno = request.GET.get("sno")
    sname = request.GET.get("sname")
    d1 = {"sno": sno, "sname": sname}
    return render(request, "s_admin/open_area.html", {"update_data": d1, "sdata": AreaModel.objects.all()})


def update_area_data(request):
    sno = request.POST.get("s1")
    sname = request.POST.get("s2")
    AreaModel.objects.filter(state_no=sno).update(state_name=sname)
    return redirect('area_city')


def delete_area(request):
    sno = request.GET.get("sno")
    AreaModel.objects.filter(state_no=sno).delete()
    return redirect('area_city')


# ---------------------------------------------------------------------------------------------------------------------
# Type <================

def open_type(request):
    return render(request, 's_admin/open_type.html',
                  {"sf": RestaurantTypeForm(), "sdata": RestaurantTypeModel.objects.all()})


def save_type(request):
    sf = RestaurantTypeForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_type')
    else:
        return render(request, "s_admin/open_type.html", {"sf": sf})


def update_type(request):
    sno = request.GET.get("sno")
    sname = request.GET.get("sname")
    d1 = {"sno": sno, "sname": sname}
    return render(request, "s_admin/open_type.html", {"update_data": d1, "sdata": TypeModel.objects.all()})


def update_type_data(request):
    sno = request.POST.get("s1")
    sname = request.POST.get("s2")
    TypeModel.objects.filter(state_no=sno).update(state_name=sname)
    return redirect('type_city')


def delete_type(request):
    sno = request.GET.get("sno")
    TypeModel.objects.filter(state_no=sno).delete()
    return redirect('type_city')

