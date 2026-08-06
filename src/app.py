"""Volt Guard GUI - Main application window."""

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QFormLayout,
    QLabel, QPushButton, QComboBox, QFrame
)
from PySide6.QtCore import QTimer
from src.client.client import VoltGuardClient


class VoltGuardApp(QMainWindow):
    """Main application window for Volt Guard GUI."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Volt Guard")
        self.setMinimumSize(600, 400)
        self._client = VoltGuardClient()
        self._setup_ui()
        self._client.connect()
        self._update_sensors()

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._refresh)
        self._timer.start(3000)

    def _setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(20, 20, 20, 20)

        layout.addWidget(QLabel("Volt Guard — Power Management"))

        # Power mode selection
        form_frame = QFrame()
        form_frame.setFrameStyle(QFrame.StyledPanel)
        form = QFormLayout(form_frame)

        self.mode_cb = QComboBox()
        self.mode_cb.addItems(["Low (15W)", "Med (30W)", "High (45W)", "Max (60W)"])
        form.addRow("Power Mode:", self.mode_cb)

        self.apply_btn = QPushButton("Apply Mode")
        self.apply_btn.clicked.connect(self._on_apply)
        form.addRow(self.apply_btn)
        layout.addWidget(form_frame)

        # Sensor display
        self.sensors_label = QLabel("Temp: -- | Voltage: -- | Current: -- | Power: --")
        self.sensors_label.setStyleSheet("color:#616161; font-size:14px; padding:10px;")
        layout.addWidget(self.sensors_label)
        layout.addStretch()

    def _update_sensors(self):
        if self._client.connected:
            sensors = self._client.get_sensors()
            self.sensors_label.setText(
                f"Temp: {sensors['temp_celsius']}°C | "
                f"Voltage: {sensors['voltage_mv']}mV | "
                f"Current: {sensors['current_ma']}mA | "
                f"Power: {sensors['power_mw']}mW"
            )
        else:
            self.sensors_label.setText("Disconnected")

    def _refresh(self):
        if not self._client.connected:
            self._client.connect()
        self._update_sensors()

    def _on_apply(self):
        result = self._client.set_power_mode(self.mode_cb.currentIndex())
        if result["success"]:
            self.sensors_label.setText("Mode applied")
        else:
            self.sensors_label.setText(f"Error: {result['error']}")
