"""Controls page for Volt Guard power mode configuration."""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QFrame
from src.theme import TITLE_STYLE, SUBTITLE_STYLE, SECTION_TITLE_STYLE, BIG_BUTTON_STYLE, CARD_STYLE, INPUT_STYLE


class ControlsPage(QWidget):
    def __init__(self, client, parent=None):
        super().__init__(parent)
        self._client = client
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 24, 32, 24)
        layout.setSpacing(24)
        header = QLabel("Controls")
        header.setStyleSheet(TITLE_STYLE)
        layout.addWidget(header)
        desc = QLabel("Select and apply power modes for the system.")
        desc.setStyleSheet(SUBTITLE_STYLE)
        layout.addWidget(desc)

        frame = QFrame()
        frame.setStyleSheet(CARD_STYLE)
        fl = QVBoxLayout(frame)
        fl.setSpacing(12)
        fl.addWidget(QLabel("Power Mode"))
        fl.itemAt(fl.count()-1).widget().setStyleSheet(SECTION_TITLE_STYLE)

        row = QHBoxLayout()
        row.addWidget(QLabel("Mode:"))
        self.mode_cb = QComboBox()
        self.mode_cb.addItems(["Low (15W)", "Medium (30W)", "High (45W)", "Max (60W)"])
        self.mode_cb.setStyleSheet(INPUT_STYLE)
        row.addWidget(self.mode_cb)
        row.addStretch()
        fl.addLayout(row)

        self.apply_btn = QPushButton("Apply Power Mode")
        self.apply_btn.setStyleSheet(BIG_BUTTON_STYLE)
        self.apply_btn.clicked.connect(lambda: self._client.set_power_mode(self.mode_cb.currentIndex()))
        fl.addWidget(self.apply_btn)
        layout.addWidget(frame)
        layout.addStretch()
