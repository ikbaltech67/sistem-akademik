from collections import deque

class StudentQueue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, student_name):
        self.queue.append(student_name)
        print(f"[QUEUE] Mahasiswa '{student_name}' berhasil ditambahkan ke antrean.")

    def dequeue(self):
        if self.is_empty():
            print("[QUEUE] Antrean kosong! Tidak ada mahasiswa untuk dilayani.")
            return None
        served_student = self.queue.popleft()
        print(f"[QUEUE] Melayani mahasiswa: '{served_student}'.")
        return served_student

    def peek(self):
        if self.is_empty():
            print("[QUEUE] Antrean kosong.")
            return None
        print(f"[QUEUE] Mahasiswa di posisi terdepan: '{self.queue[0]}'.")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0


class UndoStack:
    def __init__(self):
        self.stack = []

    def push(self, activity):
        self.stack.append(activity)
        print(f"[STACK] Aktivitas dicatat: '{activity}'.")

    def undo(self):
        if self.is_empty():
            print("[STACK] Tidak ada aktivitas untuk di-undo.")
            return None
        undone_activity = self.stack.pop()
        print(f"[STACK] Berhasil membatalkan aktivitas: '{undone_activity}'.")
        return undone_activity

    def is_empty(self):
        return len(self.stack) == 0



if __name__ == "__main__":
    print("=== SIMULASI SISTEM ANTREAN MAHASISWA ===")
    service_queue = StudentQueue()
    service_queue.enqueue("Andi")
    service_queue.enqueue("Budi")
    service_queue.enqueue("Citra")
    service_queue.peek()
    service_queue.dequeue()
    
    print("\n=== SIMULASI FITUR UNDO PETUGAS ===")
    undo_system = UndoStack()
    undo_system.push("Input Data: Andi")
    undo_system.push("Validasi Berkas: Budi")
    undo_system.push("Cetak Transkrip: Citra")
    undo_system.undo()
