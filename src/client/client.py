"""Volt Guard GUI - gRPC client wrapper."""

import grpc
from src.client import volt_guard_pb2, volt_guard_pb2_grpc


class VoltGuardClient:
    """Thread-safe gRPC client for Volt Guard server."""

    POWER_MODES = [15000, 30000, 45000, 60000]

    def __init__(self, address: str = "localhost:50055", timeout: float = 2.0):
        self._address = address
        self._timeout = timeout
        self._channel = None
        self._stub = None
        self._connected = False

    @property
    def connected(self) -> bool:
        return self._connected

    def connect(self) -> bool:
        try:
            self._channel = grpc.insecure_channel(self._address)
            self._stub = volt_guard_pb2_grpc.VoltGuardStub(self._channel)
            resp = self._stub.HealthCheck(
                volt_guard_pb2.Empty(), timeout=self._timeout
            )
            self._connected = resp.status == "SERVING"
        except Exception:
            self._connected = False
        return self._connected

    def set_power_mode(self, mode_index: int) -> dict:
        if not self._stub:
            return {"success": False, "error": "Not connected"}
        try:
            power_mw = self.POWER_MODES[mode_index] if mode_index < len(self.POWER_MODES) else 15000
            resp = self._stub.SetPowerMode(
                volt_guard_pb2.PowerMode(mode=mode_index, power_mw=power_mw),
                timeout=5.0,
            )
            return {"success": resp.success, "error": ""}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_sensors(self) -> dict:
        if not self._stub:
            return {"temp_celsius": 0, "voltage_mv": 0, "current_ma": 0, "power_mw": 0}
        try:
            resp = self._stub.GetSensors(
                volt_guard_pb2.Empty(), timeout=self._timeout
            )
            return {
                "temp_celsius": resp.temp_celsius,
                "voltage_mv": resp.voltage_mv,
                "current_ma": resp.current_ma,
                "power_mw": resp.power_mw,
            }
        except Exception:
            self._connected = False
            return {"temp_celsius": 0, "voltage_mv": 0, "current_ma": 0, "power_mw": 0}
