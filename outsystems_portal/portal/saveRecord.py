"""
@author: chris.john.avila@shi-g.com

"""
from django.shortcuts import redirect, render
from datetime import datetime
from .models import PORTAL_TBL
from django.db import connection
from .query import queryForInit, queryForCdCtgry

def save(request):
    title = request.POST.get('titleAdd')
    category = request.POST.get('categoryAdd')
    desc = request.POST.get('descAdd')
    idVal = request.POST.get('idVal')
    process = request.POST.get('process', '')
    
    now = datetime.now()
    
    print('>>>>>>>>>>>>' + process)

    if process == "Register":
        portabl_tbl = PORTAL_TBL()
        portabl_tbl.TITLE = title
        portabl_tbl.CATEGORY = category
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
        portabl_tbl.CATEGORY = category
        portabl_tbl.DESCRIPTION = desc
        portabl_tbl.UPDATE_USER_ID = 'cj'
        portabl_tbl.UPDATE_DATE = now
        portabl_tbl.save()
        success_message = "Edit completed successfully."

    # Query for IDE record list
    with connection.cursor() as cursor:
        cursor.execute(queryForInit('IDE'))
        ideRecords = cursor.fetchall()

    # Query for Widget record list
    with connection.cursor() as cursor:
        cursor.execute(queryForInit('Widget'))
        widgetRecords = cursor.fetchall()

    # Query for How to record list
    with connection.cursor() as cursor:
        cursor.execute(queryForInit('How to'))
        howToRecords = cursor.fetchall()

    # Query for Category list
    with connection.cursor() as cursor:
        cursor.execute(queryForCdCtgry())
        categoryRecords = cursor.fetchall()

    # return redirect('/outsystems')
    return render(request, 'template/outsystems-portal.html', {
        "ideRecordList" : ideRecords,
        "widgetRecordList" : widgetRecords,
        "howToRecordList" : howToRecords,
        "success_message": success_message,
        "categoryList" : categoryRecords,
    })