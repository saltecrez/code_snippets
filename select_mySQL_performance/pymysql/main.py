#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "June 2018"

'''
Threaded version of a Mysql DB connection.
Test the performance by changing nr_threads.
The pure-Python MySQL client library used here is PyMySQL.
The function do_work is performing the single SELECT query
on the DB and measuring how long the operation takes.
A foor loop creates a list of all the SELECT queries.
These are passed to do_work as a single chunk and 
execute through map_async.
'''

import os
import shutil
import read_tools
import pymysql
import mysql_tools
from glob import glob
from datetime import datetime
import multiprocessing
from multiprocessing import Pool
from multiprocessing import cpu_count

nr_threads = 1

CWD = os.getcwd()
logfile = open(CWD + '/' + "logfile.txt",'a')

cnf = read_tools.read_json('conf.json',CWD,logfile) 

cameras_path = cnf['camerasfolder'];   ingest_path = cnf['ingestfolder']
db_host      = cnf['dbhost'];          db_pwd      = cnf['dbpwd']
db_user      = cnf['dbuser'];          db_name     = cnf['dbname']
tb_name      = cnf['tbname'];          thumbs_path = cnf['thumbsfolder']

cameras_path_list = glob(cameras_path + '/*/')

current_month = datetime.today().strftime('%Y%m')
cameras_month_path = [i + current_month for i in cameras_path_list]
print "number of cpus", multiprocessing.cpu_count()

def do_work(query):
    t1 = datetime.now()
    con = pymysql.connect(db_host,db_user,db_pwd,db_name) 
    print("PID %d: using connection %s" % (os.getpid(), con))
    c = con.cursor()
    c.execute(query)
    res = c.fetchall()
    c.close()
    con.close()
    t2 = datetime.now()
    delta = t2-t1
    print "do_work() performance: ", delta

for j in range(len(cameras_month_path)):
    fits_captures = glob(cameras_month_path[j] + '/*.fit')
    selects = []
    for j in fits_captures:
	fits_name = os.path.basename(j)
	print fits_name
	sql = """select id from CAM where EXP_ID='%s';""" % (fits_name)
	selects.append(sql)
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pool = multiprocessing.Pool(processes=nr_threads)
    pool.map_async(do_work, selects).get(timeout=20)
    pool.close()
    pool.join()

logfile.close()
