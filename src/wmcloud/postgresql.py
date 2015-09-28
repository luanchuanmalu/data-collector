# -*- coding: utf-8 -*-  
  
import pg  

  
def operate_postgre_tbl_product():  
      
    #�������ݿ�    
    try:  
        pgdb_conn = pg.connect(dbname = 'keystonedata', host = '192.168.58.132', user = 'keystone', passwd = 'keystone')  
    except Exception, e:
        print "connect failed"        
        return       
          
    #ɾ����  
    sql_desc = "DROP TABLE IF EXISTS tbl_product3;"  
    try:  
        pgdb_conn.query(sql_desc)  
    except Exception, e:  
        print 'drop table failed'     
        return    
    
    #������  
    sql_desc = '''CREATE TABLE tbl_product3( 
        i_index INTEGER, 
        sv_productname VARCHAR(32) 
        );'''  
    try:      
        pgdb_conn.query(sql_desc)  
    except Exception, e:  
        print 'create table failed'
        pgdb_conn.close()    
        return          
        
    #�����¼     
    sql_desc = "INSERT INTO tbl_product3(sv_productname) values('apple')"  
    try:  
        pgdb_conn.query(sql_desc)  
    except Exception, e:  
        print 'insert record into table failed'  
        pgdb_conn.close()    
        return      
       
    #��ѯ�� 1         
    sql_desc = "select * from tbl_product3"  
    for row in pgdb_conn.query(sql_desc).dictresult():  
        print row  
   
    #��ѯ��2          
    sql_desc = "select * from tbl_test_port"  
    for row in pgdb_conn.query(sql_desc).dictresult():  
        print row           
       
    #�ر����ݿ�����       
    pgdb_conn.close()          
  
if __name__ == '__main__':   
         
    #�������ݿ�  
    operate_postgre_tbl_product()  