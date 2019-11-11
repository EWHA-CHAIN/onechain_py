'use strict'
# timeutil.py
import datetime
import json
def get_epochtime_ms():
    return round(datetime.datetime.utcnow().timestamp() )

'''function getCurrentTimestamp() {
    return round(new Date().getTime() / 1000);
}'''

def getCurrentVersion():
    fs=open('./package.json','r')
    packageJson = fs.read()
    json_data = open(packageJson).read()
    data = json.loads(json_data)
    currentVersion = data['version']
    return currentVersion

'''function getCurrentVersion() {
    fs=open('./package.json','r')
    packageJson = fs.read()
    currentVersion = JSON.parse(packageJson).version;
    return currentVersion;
}
'''

def hexToBinary(s): 
    lookupTable = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    

    ret = ""
    for i in range(1, s.len):
       if (lookupTable[s[i]]): ret += lookupTable[s[i]]
       else: return None
    return ret



'''module.exports = {
    getCurrentTimestamp,
    getCurrentVersion,
    hexToBinary
};'''