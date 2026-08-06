"""Dashboard page for Volt Guard power management."""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from src.theme import TITLE_STYLE, SUBTITLE_STYLE
from src.widgets import BigButtonBox, MacCard


class DashboardPage(QWidget):
    def __init__(self, client, parent=None):
        super().__init__(parent)
        self._client = client
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 24, 32, 24)
        layout.setSpacing(24)
        header = QLabel("Dashboard")
        header.setStyleSheet(TITLE_STYLE)
        layout.addWidget(header)
        desc = QLabel("Monitor and control power states on Jetson AGX Orin.")
        desc.setStyleSheet(SUBTITLE_STYLE)
        layout.addWidget(desc)
        btn_row = QHBoxLayout()
        btn_row.setSpacing(20)
        self.apply_box = BigButtonBox("Apply Power Mode", "Set the system power envelope.\nChoose from 15W to 60W in Controls.", "Apply Mode", "primary")
        btn_row.addWidget(self.apply_box)
        self.reset_box = BigButtonBox("Reset", "Reset power management to default settings.\nAll rails will return to safe state.", "Reset", "danger")
        btn_row.addWidget(self.reset_box)
        layout.addLayout(btn_row)
        cards_row = QHBoxLayout()
        cards_row.setSpacing(16)
        self.temp_card = MacCard("Temperature", "0", "°C", "#F57C00")
        self.voltage_card = MacCard("Voltage", "0", "mV")
        self.current_card = MacCard("Current", "0", "mA")
        self.power_card = MacCard("Power", "0", "mW")
        cards_row.addWidget(self.temp_card)
        cards_row.addWidget(self.voltage_card)
        cards_row.addWidget(self.current_card)
        cards_row.addWidget(self.power_card)
        layout.addLayout(cards_row)
        layout.addStretch()
