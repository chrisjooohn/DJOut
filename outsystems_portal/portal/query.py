
def queryForInit():

    sqlQuery = f'''
        SELECT ID, TITLE, DESCRIPTION
        FROM ba_portal.portal_portal_tbl;
    '''
    print(sqlQuery)
    return sqlQuery 