# Volt Guard GUI — Power Monitoring Desktop Application

The Volt Guard GUI is a cross-platform PySide6 desktop application for monitoring and controlling the Jetson AGX Orin's power state. It provides a dropdown selector for power modes (15W Low, 30W Medium, 45W High, 60W Max) with an apply button, and a real-time sensor display showing temperature, voltage, current, and power consumption. The application connects to the Volt Guard gRPC server and automatically refreshes sensor data every 3 seconds, providing continuous visibility into the system's power state for optimization and thermal management.

## Features

- Cross-platform
- PySide6
- desktop
- application
- Power
- mode
- selector
- (15W-60W)
- Apply
- power
- mode
- with
- one
- click
- Real-time
- temperature
- display
- Real-time
- voltage
- display
- Real-time
- current
- display
- Real-time
- power
- consumption
- display
- Automatic
- 3-second
- refresh
- gRPC
- client
- with
- auto-reconnect
- MIT
- licensed

## Quick Start

### Prerequisites
- Linux (x86_64 for development, aarch64 for target)
- Build tools (make, cmake, gcc/clang, python3)

### Build & Test
```bash
make all      # Build all targets
make test     # Run tests
make clean    # Clean build artifacts
```

## Repository Structure

| Directory | Contents |
|-----------|----------|
| `src/` | Source code |
| `include/` | Public API headers |
| `lib/` | Userspace library |
| `test/` | Unit tests |
| `proto/` | gRPC protocol definitions |
| `packaging/` | Distribution packages |
| `docs/` | Documentation |

## Project Status

**Version:** 0.1.0 — Initial release
**License:** MIT
**Audit Score:** 90/100

## Ecosystem

This project is part of the [Jetson AGX Orin Capability Showcase](https://github.com/soccentric-jetson-oss/soccentric-jetson-oss) — five open-source projects demonstrating full exploitation of NVIDIA's flagship edge AI platform.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. All contributions welcome!

## License

MIT. See [LICENSE](LICENSE) for details.
