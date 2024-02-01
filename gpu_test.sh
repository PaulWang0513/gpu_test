(trap 'kill 0' SIGINT; \
python3 gpu_test.py --device 0 \
    &
python3 gpu_test.py --device 1 \
    &
python3 record_gpu_status.py \
    & \
wait)