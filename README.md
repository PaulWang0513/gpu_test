# gpu_test
These scripts are used to check the GPU status of the server.
Because these scripts will not be terminated automatically, it is recommended to run them using `screen` or `tmux` to avoid being interrupted by the terminal.
- screen command
    - outside the screen
        - `screen` to start a new screen
        - `screen -ls` to list all existing screens
        - `screen -r [screen_id]` to resume a screen
    - inside the screen
        - `Ctrl + a` then `d` to detach the screen
        - `Ctrl + a` then `:quit` to terminate the screen

## gpu_test.py
This script use huggingface gpt2-xl model to generate random text to check the GPU can work properly.
To run this script, run `python3 gpu_test.py --device [gpu_id]` in the terminal.

## record_gpu_status.py
This script will record the status (fan speed, temperature) of the GPUs every 10 seconds.
To run this script, simply run `python3 record_gpu_status.py` in the terminal.

## gpu_test.sh
This is a sample shell script to run the above two scripts together conveniently.