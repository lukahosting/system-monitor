import sys
import psutil
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer

class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Luka Hosting Server System Monitor")
        self.layout = QVBoxLayout()
        self.labels = {
            "RAM Usage": QLabel(),
            "CPU Usage": QLabel(),
            "SSD Usage": QLabel(),
            "CPU Temperature": QLabel()
        }
        for label in self.labels.values():
            self.layout.addWidget(label)
        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)  # 1 saniyede bir güncelleme yapılacak

    def update_stats(self):
        # RAM kullanımını al
        ram_usage = psutil.virtual_memory().percent
        self.labels["RAM Usage"].setText(f"RAM Usage: {ram_usage}%")

        # CPU kullanımını al
        cpu_usage = psutil.cpu_percent()
        self.labels["CPU Usage"].setText(f"CPU Usage: {cpu_usage}%")

        # SSD kullanımını al
        ssd_usage = psutil.disk_usage("/").percent
        self.labels["SSD Usage"].setText(f"SSD Usage: {ssd_usage}%")

        # CPU sıcaklığını al
        cpu_temp = psutil.sensors_temperatures()["coretemp"][0].current
        self.labels["CPU Temperature"].setText(f"CPU Temperature: {cpu_temp}°C")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    monitor = SystemMonitor()
    monitor.show()
    sys.exit(app.exec_())
