#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "December 2019"

import os
from mapping import AFO
from mapping import ECH
from mapping import SBI
from database import MySQLDatabase

class Queries(object):
    def __init__(self, session, table_object, string):
        self.session = session
        self.table_object = table_object
        self.string = string
        self.rows = self.session.query(self.table_object)
        self.flt = self.rows.filter(self.table_object.file_name == self.string)

    def match_file_name(self):
        for j in self.flt:
            if j.file_name:
                return True
            else:
                return False

    def get_storage_path(self):
        for j in self.flt:
            path = j.storage_path + j.file_path
            full_path = os.path.join(path,str(j.file_version),j.file_name)
            return full_path

if __name__ == "__main__":
    user = 'archa'
    pwd = 'Archa123.'
    host = 'localhost'
    dbname = 'metadata_asiago'
    port = '3307'
    session = MySQLDatabase(user,pwd,host,port,dbname).create_session()
#    print(Queries(session,AFO,'AF597076.fits.gz').match_file_name())

