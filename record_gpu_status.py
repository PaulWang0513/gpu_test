import time
import subprocess

def get_gpu_status():
    gpu_info = subprocess.check_output(['nvidia-smi', '--query-gpu=index,uuid,pci.bus_id,fan.speed,temperature.gpu', '--format=csv,noheader'])
    gpu_info = gpu_info.decode('utf-8').split('\n')[:-1]
    gpu_info = [x.split(', ') for x in gpu_info]
    return gpu_info


while True:
    today = time.strftime('%Y-%m-%d', time.localtime())
    # open file
    f = open('output_{}.txt'.format(today), 'a+')
    gpu_info = get_gpu_status()
    print(f"===== {time.strftime('%H:%M:%S', time.localtime())} =====", file=f)
    for info in gpu_info:
        print(f"GPU {info[0]} ({info[1]}) on PCI {info[2]}: {info[3]} fan speed, {info[4]}°C", file=f)
    f.close()
    # sleep 10 seconds
    time.sleep(10)
