"""
@author: chris.john.avila@shi-g.com

"""
def queryForInit(category):

    sqlQuery = f'''
        SELECT ID, TITLE, DESCRIPTION, CATEGORY
        FROM ba_portal.portal_portal_tbl
        WHERE CATEGORY = '{ category }' ;
    '''
    print(sqlQuery)
    return sqlQuery 

def queryForCdCtgry():

    sqlQuery = f'''
        SELECT CD_CTGRY_NAME
        FROM ba_portal.portal_various_cd_tbl
        WHERE CD_CTGRY = '001';
    '''
    print(sqlQuery)
    return sqlQuery 