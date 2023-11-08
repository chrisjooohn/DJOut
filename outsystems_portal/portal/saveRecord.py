"""
@author: chris.john.avila@shi-g.com

"""
from django.shortcuts import redirect, render
from datetime import datetime
from .models import PORTAL_TBL
from django.db import connection
from .query import queryForInit

def save(request):
    title = request.POST.get('titleAdd')
    desc = request.POST.get('descAdd')
    idVal = request.POST.get('idVal')
    process = request.POST.get('process', '')
    now = datetime.now()
    
    print('>>>>>>>>>>>>' + process)

    if process == "Register":
        portabl_tbl = PORTAL_TBL()
        portabl_tbl.TITLE = title
        portabl_tbl.DESCRIPTION = desc
        portabl_tbl.INSERT_USER_ID = 'cj'
        portabl_tbl.INSERT_DATE = now
        portabl_tbl.UPDATE_USER_ID = 'cj'
        portabl_tbl.UPDATE_DATE = now
        portabl_tbl.save()
        success_message = "Data saved successfully."

    else:
        portabl_tbl = PORTAL_TBL.objects.get(ID = idVal)
        portabl_tbl.TITLE = title
        portabl_tbl.DESCRIPTION = desc
        portabl_tbl.UPDATE_USER_ID = 'cj'
        portabl_tbl.UPDATE_DATE = now
        portabl_tbl.save()
        success_message = "Edit completed successfully."

    with connection.cursor() as cursor:
        cursor.execute(queryForInit())
        records = cursor.fetchall()

    # return redirect('/outsystems')
    return render(request, 'template/outsystems-portal.html', {
        "recordList" : records,
        "success_message": success_message,
    })