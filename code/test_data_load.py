import subprocess
import time

def adb(cmd):
    subprocess.run(cmd, shell=True, check=True)

def test_server_data_load_with_network_toggle(driver):
    adb("adb shell am start -n com.android.settings/.Settings")
    time.sleep(1)
    adb("adb shell svc wifi disable")
    adb("adb shell svc data disable")
    time.sleep(1)
    adb("adb shell svc wifi enable")
    adb("adb shell svc data enable")
    time.sleep(1)
    assert "settings" in driver.current_package