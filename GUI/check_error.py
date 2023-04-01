import re
class check_error:

    def check_phone(self, input):
        input = input.upper()
        if re.match("^(0|\\+84)(\\s|\\.)?((3[2-9])|(5[689])|(7[06-9])|(8[1-689])|(9[0-46-9]))(\\d)(\\s|\\.)?(\\d{3})(\\s|\\.)?(\\d{3})$", input):
            return True
        else :
            return False

    def check_email(self, input):
        if (re.match("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"
                + "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$", input)) :
            return True
        else :
            return False
        
    def check_cmnd(self, input):
        if (re.match("^[0-9]{9}$|^[0-9]{12}$", input)) :
            return True
        else :
            return False