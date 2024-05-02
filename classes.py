import abc

class TempControlUnit:
    def __init__(self, TempIn, DavlIn):
        self.TempIn = TempIn
    def Temption(self, request):
        self.TempIn = request.args.get('TempIn', '')
        print('TempIn now is - ' + self.TempIn)

    def DavlAnalysis(self, request):
        self.DavlIn = request.args.get('DavlIn', '')
        print('davl now is - ' + self.DavlIn)

class KislorControlUnit:
    def __init__(self, physical, kislor):
        self.physical = physical
        self.kislor = kislor
        print(' has created')

    def Controlkislor(self, request):
        self.kislor = request.args.get('KislorIn', '')
        print('Kislor now is - ', self.kislor)

class SleepAl:
    def __init__(self, hours, alarm):
        self.hours = hours
        self.alarm = alarm
        print('has created')

    def Sleeping(self, request):
        self.hours = request.args.get('hours', '')
        print('Sleep hours now is - ' + self.hours)

class PulsAl:
    def __init__(self, steps, activity):
        self.steps = steps

    def Walking(self, request):
        self.steps = request.args.get('pulsIn', '')
        print('puls is -', self.steps)


class AllCommandsController:
    def __init__(self, temp_control_unit, davl_control_unit, kislor_control_unit, sleep_al, puls_al):
        self.temp_control_unit = temp_control_unit
        self.davl_control_unit = davl_control_unit
        self.kislor_control_unit = kislor_control_unit
        self.sleep_al = sleep_al
        self.puls_al = puls_al

    def startAll(self, request):
        TempIn = request.args.get('TempIn', '')
        pulsIn = request.args.get('pulsIn', '')
        hours = request.args.get('hours', '')
        DavlIn = request.args.get('DavlIn', '')
        print('Температура :', TempIn)
        print('Пульс :', pulsIn)
        print('Часы :', hours)
        print('Давление :', DavlIn)


pulsal = PulsAl(steps=None, activity=None)








