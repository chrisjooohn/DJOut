"""
@author: chris.john.avila@shi-g.com

"""
from django.shortcuts import redirect, render
from django.db import connection
from .query import queryForInit, queryForCdCtgry

def init(request):
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
        cursor.execute(queryForInit('Howto'))
        howToRecords = cursor.fetchall()
    
    # Query for Category list
    with connection.cursor() as cursor:
        cursor.execute(queryForCdCtgry())
        categoryRecords = cursor.fetchall()

    return render(request, 'template/outsystems-portal.html', {
        "ideRecordList" : ideRecords,
        "widgetRecordList" : widgetRecords,
        "howToRecordList" : howToRecords,
        "categoryList" : categoryRecords,
    })