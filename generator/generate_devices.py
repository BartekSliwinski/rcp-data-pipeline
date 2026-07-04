import config
import pandas as pd


def generate_devices():
    df = pd.DataFrame({
        "DeviceID": range(1, config.NUM_OF_DEVICES+1),
        "Location": config.DEVICES,
    })
    return df


if __name__ == "__main__":
    device_df = generate_devices()
    print(device_df)
    device_df.to_csv("output/devices.csv", index=False)