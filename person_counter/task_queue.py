import threading
import time

# Kolejka w pamięci
task_queue = {}
results = {}

def add_task(task_id, func, args=()):
    """Dodaje zadanie do kolejki."""
    task_queue[task_id] = "PENDING"

    def process_task():
        time.sleep(2)  # Symulacja opóźnienia
        try:
            result = func(*args)
            results[task_id] = {"status": "COMPLETED", "result": result}
        except Exception as e:
            results[task_id] = {"status": "FAILED", "error": str(e)}
        finally:
            del task_queue[task_id]

    # Wykonywanie w oddzielnym wątku
    thread = threading.Thread(target=process_task)
    thread.start()


def get_task_status(task_id):
    """Pobiera status zadania."""
    if task_id in task_queue:
        return {"status": task_queue[task_id]}
    return results.get(task_id)
