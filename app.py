from flask import Flask, request, render_template, jsonify
import classes


app = Flask(__name__)

tempcontrolunit = classes.TempControlUnit(7, 8)
davlcontrolunit = classes.KislorControlUnit(2, 4)
sleepal = classes.SleepAl(' ', ' ')
kislor_control_unit = classes.KislorControlUnit(10, 1)
pulsal = classes.PulsAl(' ', ' ')
all_commands_controller = classes.AllCommandsController(tempcontrolunit, davlcontrolunit, kislor_control_unit,sleepal, pulsal)


@app.route('/ControlCommands')
def all_commands():
    all_commands_controller.startAll(request)
    return {}


@app.route('/Temp')
def Tempcontrol():
    tempcontrolunit.Temption(request)
    return {}

@app.route('/Davl')
def davlvits():
    all_commands_controller.temp_control_unit.DavlAnalysis(request)
    return {}

@app.route('/Kislor')
def kisrolHealth():
    all_commands_controller.kislor_control_unit.Controlkislor(request)
    return {}

@app.route('/Sleeping')
def Sleeping():
    all_commands_controller.sleep_al.Sleeping(request)
    return {}

@app.route('/Puls')
def Walking():
    all_commands_controller.puls_al.Walking(request)
    return {}

@app.route('/')
def hello_world():
    return render_template('emulator.html')

if __name__ == '__main__':
    app.run()







