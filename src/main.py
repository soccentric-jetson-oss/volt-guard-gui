import sys; from PySide6.QtWidgets import *; from PySide6.QtCore import QTimer
import grpc; from src.client import volt_guard_pb2, volt_guard_pb2_grpc

class VoltGuardApp(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Volt Guard"); self.setMinimumSize(600,400)
        self.stub = None; self._ui(); self._connect()
        t = QTimer(self); t.timeout.connect(self._refresh); t.start(3000)
    def _ui(self):
        w=QWidget(); self.setCentralWidget(w); l=QVBoxLayout(w); l.setContentsMargins(20,20,20,20)
        l.addWidget(QLabel("Volt Guard — Power Management"))
        f=QFrame(); f.setFrameStyle(QFrame.StyledPanel); fl=QFormLayout(f)
        self.mode_cb=QComboBox(); self.mode_cb.addItems(["Low (15W)","Med (30W)","High (45W)","Max (60W)"])
        fl.addRow("Power Mode:",self.mode_cb)
        self.apply_btn=QPushButton("Apply Mode"); self.apply_btn.clicked.connect(self._apply)
        fl.addRow(self.apply_btn)
        l.addWidget(f)
        self.sensors=QLabel("Temp: -- | Voltage: -- | Current: -- | Power: --")
        self.sensors.setStyleSheet("color:#888;font-size:14px;padding:10px;")
        l.addWidget(self.sensors)
        l.addStretch()
    def _connect(self):
        try:
            ch=grpc.insecure_channel("localhost:50055")
            self.stub=volt_guard_pb2_grpc.VoltGuardStub(ch)
            r=self.stub.HealthCheck(volt_guard_pb2.Empty(),timeout=2)
            self.sensors.setText(f"Connected (v{r.version})")
        except: self.sensors.setText("Disconnected")
    def _refresh(self):
        if not self.stub: return
        try:
            r=self.stub.GetSensors(volt_guard_pb2.Empty(),timeout=2)
            self.sensors.setText(f"Temp: {r.temp_celsius}°C | Voltage: {r.voltage_mv}mV | Current: {r.current_ma}mA | Power: {r.power_mw}mW")
        except: self.sensors.setText("Disconnected")
    def _apply(self):
        if not self.stub: return
        modes=[15000,30000,45000,60000]
        r=self.stub.SetPowerMode(volt_guard_pb2.PowerMode(mode=self.mode_cb.currentIndex(),power_mw=modes[self.mode_cb.currentIndex()]),timeout=5)
        self.sensors.setText("Mode applied" if r.success else f"Error: {r.error}")

app=QApplication(sys.argv); w=VoltGuardApp(); w.show(); sys.exit(app.exec())
