
from sqlalchemy import create_engine

#Logging features for the code
import logging as log
FORMAT='%(asctime)s - %(message)s'
WARNINGFORMAT='WARNING:: %(asctime)s %(message)s'
log.basicConfig(level=log.INFO, format = FORMAT)
log.basicConfig(level=log.warning, format = WARNINGFORMAT)

db_uri = 'sqlite:///peerfit.db'
#engine = create_engine(db_uri)

class etl_sql():

    def __init__(self, host = None, database = None, engine = None,
                  port = None, user = None, password = None ):

        
          self.database = database
          self.engine = create_engine(db_uri)
          self.user = user
          self.password = password
          self.host = host

          
          log.info('Default host: %s'%self.host)
          self.query_dict = {}
          self.server = ''
          self.schema = ''
          self.port = ''

          self.cnxn = None
          #self.cur = None
          return
    def open_cnxn(self):
        self.conn = self.engine.connect()
        return
         
    def close_cnxn(self):
        """Closes open connections.  Not needed for now
        """
        #self.conn = self.engine.close()
        #self.engine.close()
        #self.open_cnxn_ind = 0
        return
          
    def upsert_exec(self, qry_label, params = (), commit = False, verbose = False, 
                         keep_connection = False, use_prior_connection = False):
        try:
             self.open_cnxn()  #try to open the cnxn 
        except Exception as ex:
             log.exception("Single Exec {}".format(ex))
        
        try:
            
            self.conn.execute(qry_label)
        
        except Exception as ex:
           log.exception("Single Exec {}".format(ex))
      
        finally:
            self.close_cnxn()
        
           
        return
