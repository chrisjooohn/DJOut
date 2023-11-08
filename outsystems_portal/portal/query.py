"""
@author: chris.john.avila@shi-g.com

"""
def queryForInit():

    sqlQuery = f'''
        SELECT ID, TITLE, DESCRIPTION
        FROM ba_portal.portal_portal_tbl;
    '''
    print(sqlQuery)
    return sqlQuery 