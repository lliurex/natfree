import os
import subprocess as s

import n4d.server.core
import n4d.responses

class ClassroomManager:
        
    def __init__(self):
        
        self.core=n4d.server.core.Core.get_core()
        
    #def init
    
    def startup(self,options):
        if options["boot"]:
            try:
                classroom = self.core.get_variable("CLASSROOM")
                if classroom != "0":
                    self.core.set_variable("CLASSROOM",None)
            except Exception:
                pass
    #def init
    
    def free_classroom(self):
        
        ret=0

        # natfree manager things here ?
        # ret=os.system()
        
        p = s.Popen("natfree-adi unset",shell=True,stdout=s.PIPE,stderr=s.PIPE)
        p.communicate()
        ret = p.returncode
        if ret==0:
            return n4d.responses.build_successful_call_response()
        else:
            return n4d.responses.build_failed_call_response()

        
    #def free_classroom

    
    
#class ClassroomManager
