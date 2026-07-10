import config
import pandas as pd


def generate_devices():
    df = pd.DataFrame({
        "DeviceID": range(1, config.NUM_OF_DEVICES+1),
        "DeviceName": config.DEVICES,
    })
    return df