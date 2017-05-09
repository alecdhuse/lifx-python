import json
import random
import requests
import time

def aurora(headers, loops):
    """Creates an aurora borealis effect over the given amount of loops"""
    cycle_time = 10

    payload1 = {
        "from_color": "hue:184 saturation:0.97 brightness:0.1",
        "color": "hue:150 saturation:0.76 brightness:1.0",
        "cycles": 1.0,
        "period": cycle_time,
        "persist": True,
        "peak": 1.0
    }

    response = requests.post('https://api.lifx.com/v1/lights/all/effects/breathe', data=json.dumps(payload1), headers=headers)
    print ("%s - %s" % (response.status_code, response.text))
    time.sleep(cycle_time)

    payload2 = {
        "color": "hue:175 saturation:0.97 brightness:0.8",
        "cycles": 1,
        "period": cycle_time / 4,
        "persist": True,
        "peak": 1.0
    }

    payload3 = {
        "color": "hue:150 saturation:0.76 brightness:1.0",
        "cycles": 1,
        "period": cycle_time / 4,
        "persist": True,
        "peak": 1.0
    }

    for i in range(0,loops):
        response = requests.post('https://api.lifx.com/v1/lights/all/effects/breathe', data=json.dumps(payload2), headers=headers)
        print ("%s - %s" % (response.status_code, response.text))
        time.sleep(cycle_time / 4)

        response = requests.post('https://api.lifx.com/v1/lights/all/effects/breathe', data=json.dumps(payload3), headers=headers)
        print ("%s - %s" % (response.status_code, response.text))
        time.sleep(cycle_time / 4)

def party(headers, flashes):
    """Flashes the light while turning it multiple colors"""

    colors = [
        "red",
        "blue",
        "white",
        "orange",
        "yellow",
        "cyan",
        "purple",
        "green",
        "pink"
    ]

    color_index = 0
    period = 0.1

    for i in range(1, flashes):
        new_index = random.randint(0, 8)

        if color_index == new_index:
            new_index = (new_index + 1) % 8

        payload = {
            "from_color": colors[color_index],
            "color": colors[new_index],
            "cycles": 1.0,
            "period": period,
            "persist": True,
            "power_on": True
        }

        response = requests.post('https://api.lifx.com/v1/lights/all/effects/pulse', data=json.dumps(payload), headers=headers)
        print ("%s - %s" % (response.status_code, response.text))
        time.sleep(period)
        color_index = new_index

def sunrise(headers, seconds):
    """Create sunrise effect over the given amount of seconds"""
    half_time = seconds / 2.0

    payload1 = {
        "from_color": "hue:0 saturation:1.0 brightness:0.1",
        "color": "kelvin:2500 brightness:0.5",
        "cycles": 1.0,
        "period": half_time,
        "persist": True,
        "peak": 1.0
    }

    response = requests.post('https://api.lifx.com/v1/lights/all/effects/breathe', data=json.dumps(payload1), headers=headers)
    print ("%s - %s" % (response.status_code, response.text))

    time.sleep(half_time)

    payload2 = {
        "color": "kelvin:4000 brightness:1.0",
        "cycles": 1.0,
        "period": half_time,
        "persist": True,
        "peak": 1.0
    }

    response = requests.post('https://api.lifx.com/v1/lights/all/effects/breathe', data=json.dumps(payload2), headers=headers)
    print ("%s - %s" % (response.status_code, response.text))

def sunset(headers, seconds):
    """Create sunset effect over the given amount of seconds"""
    half_time = seconds / 2.0

    payload1 = {
        "from_color": "kelvin:4000 brightness:1.0",
        "color": "kelvin:2500 brightness:0.5",
        "cycles": 1.0,
        "period": half_time,
        "persist": True,
        "peak": 1.0
    }

    response = requests.post('https://api.lifx.com/v1/lights/all/effects/breathe', data=json.dumps(payload1), headers=headers)
    print ("%s - %s" % (response.status_code, response.text))

    time.sleep(half_time)

    payload2 = {
        "from_color": "kelvin:2500 brightness:0.5",
        "color": "hue:0 saturation:1.0 brightness:0.0",
        "cycles": 1.0,
        "period": half_time,
        "persist": True,
        "peak": 1.0
    }

    response = requests.post('https://api.lifx.com/v1/lights/all/effects/breathe', data=json.dumps(payload2), headers=headers)
    print ("%s - %s" % (response.status_code, response.text))

def main():
    headers = { "Authorization": "Bearer [api key here]]"}

    #aurora(headers, 10)
    sunrise(headers, 30)
    #sunset(headers, 30)
    #party(headers, 30)

main()
