gvar = 'abcdefg'
 
class func:
    global gvar
    gvar = "changed in func"

class testfunc():
    def reset(self):
        global gvar
        gvar = '0123456'
    print(gvar)
 
print(gvar)
testfunc().reset()
print(gvar)
