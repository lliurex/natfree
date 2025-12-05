import n4d.responses
import subprocess as s 

class NatfreeADI:
    def __init__(self):
        pass

    def unset(self):
        p = s.Popen("/usr/bin/natfree-adi unset", shell=True, stdout=s.PIPE, stderr=s.PIPE)
        out, err = p.communicate()
        if p.returncode != 0:
            return n4d.responses.build_successful_call_response(True, "ADI unset successfully")
        else:
            return n4d.responses.build_failed_call_response(p.returncode, err.decode().strip())

    def set(self, kart):
        p = s.Popen(f"/usr/bin/natfree-adi set {kart}", shell=True, stdout=s.PIPE, stderr=s.PIPE)
        out, err = p.communicate()
        if p.returncode == 0:
            return n4d.responses.build_successful_call_response(True, "ADI set successfully")
        else:
            return n4d.responses.build_failed_call_response(p.returncode, err.decode().strip())

