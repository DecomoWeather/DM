from get_weather import fetchWeather
import json
from config import weather_kb


class DM_WEATHER:
    def __init__(self):
        pass



    def reponse(self,dct):
        new_dct={'diaact':'inform','inform_slots':''}
        code_day=dct['inform_slots']['time']
        location=dct['inform_slots']['location']
        act=dct['request_slots']['weather_action']
        result=fetchWeather(location)
        re=json.loads(result)
        weather=re['results'][0]['daily'][code_day]
        if act!={}:
            #for a in act:
                flag=weather_kb[weather['text_day']+'天']['weather_action'][act]
                new_dct['inform_slots']={'weather':weather,'time':code_day,
                                     'location':location,'weather_action':flag}
        else:
            new_dct['inform_slots']={'weather':weather,'time':code_day,'location':location}
        return new_dct




if __name__=='__main__':
    dd={'intent':'weather','diaact':'request',
        'request_slots':{'weather_action':'打伞'},
        'inform_slots':{'time':1,'location':'beijing'}
        }
    dmw=DM_WEATHER()
    ne=dmw.reponse(dd)
    print(ne)
