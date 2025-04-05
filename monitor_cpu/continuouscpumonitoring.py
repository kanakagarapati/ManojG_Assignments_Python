import psutil
#import platform
import time

cup_threshold = 80.0
def get_cpu_usage_continuously_with_exception_handling(threshold=cup_threshold):
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            if cpu_usage > threshold:
                print(f"\033[91mWarning: CPU usage is above {threshold}%: {cpu_usage}%!\033[0m")
            else:
                print(f"CPU Usage: {cpu_usage}%")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as ex:
        print(f"An error occurred: {ex}")
print("CPU Usage Monitoring", get_cpu_usage_continuously_with_exception_handling())