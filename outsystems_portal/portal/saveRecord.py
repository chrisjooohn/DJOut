from django.shortcuts import redirect, render
from datetime import datetime
from .models import PORTAL_TBL
from django.db import connection
from .query import queryForInit

def save(request):
    title = request.POST.get('title')
    desc = request.POST.get('desc')

    portabl_tbl = PORTAL_TBL()
    now = datetime.now()
    portabl_tbl.TITLE = title
    portabl_tbl.DESCRIPTION = desc
    portabl_tbl.INSERT_USER_ID = 'cj'
    portabl_tbl.INSERT_DATE = now
    portabl_tbl.UPDATE_USER_ID = 'cj'
    portabl_tbl.UPDATE_DATE = now
    portabl_tbl.save()

    with connection.cursor() as cursor:
        cursor.execute(queryForInit())
        records = cursor.fetchall()

    # return redirect('/outsystems')
    return render(request, 'template/outsystems-portal.html', {
        "recordList" : records,
    })