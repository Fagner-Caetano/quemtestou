import time
import datetime

count = 1
try:
    print("Container iniciado. Pressione Ctrl+C para encerrar.")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{current_time}] O container rodou {count}x...")
        count += 1
        time.sleep(5)  # intervalo de 5 segundos.
except KeyboardInterrupt:
    print("\nContainer encerrado pelo usuário.")

