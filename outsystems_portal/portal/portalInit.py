from django.shortcuts import redirect, render
from django.db import connection
from .query import queryForInit

def init(request):
    print('>>>>>>>>>>>>>>>>>>>>>>>123')
    with connection.cursor() as cursor:
        cursor.execute(queryForInit())
        records = cursor.fetchall()

    return render(request, 'template/outsystems-portal.html', {
        "recordList" : records,
    })