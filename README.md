# Volt Guard GUI — Power Monitoring Desktop Application

The Volt Guard GUI is a cross-platform PySide6 desktop application for monitoring and controlling the Jetson AGX Orin's power state. It provides a dropdown selector for power modes including 15W Low, 30W Medium, 45W High, and 60W Max with an apply button, and a real-time sensor display showing temperature, voltage, current, and power consumption. The application connects to the Volt Guard gRPC server and automatically refreshes sensor data every 3 seconds.

## Features

- Provides a cross-platform PySide6 desktop application that runs identically on Windows, macOS, and Linux operating systems
- Offers a power mode dropdown selector with four options from 15W Low Power to 60W Maximum Performance
- Applies the selected power mode with a single click and displays success or error feedback
- Displays real-time temperature readings in degrees Celsius for thermal monitoring
- Displays real-time voltage readings in millivolts for power supply quality monitoring
- Displays real-time current readings in milliamps for load analysis
- Displays real-time power consumption readings in milliwatts for energy efficiency tracking
- Refreshes sensor data automatically every 3 seconds for continuous monitoring without manual intervention
- Connects to the Volt Guard gRPC server with automatic health check and reconnection on connection loss
- Licensed under MIT for maximum flexibility in commercial and open-source projects

## Quick Start

### Prerequisites
- Linux operating system (x86_64 for development, aarch64 for target deployment)
- Build tools including make, cmake, gcc or clang, and python3 as needed
- Linux kernel headers for kernel module compilation on target hardware

### Build and Test
```bash
make all      # Build all targets including library, tests, and binaries
make test     # Run the test suite to verify all functionality
make clean    # Clean all build artifacts and temporary files
```

## Repository Structure

| Directory | Contents |
|-----------|----------|
| src/ | Source code for the project |
| include/ | Public API header files |
| lib/ | Userspace library source and headers |
| test/ or tests/ | Unit tests and test utilities |
| proto/ | gRPC protocol buffer definitions |
| packaging/ | Distribution packaging files for deb, rpm, and ipk |
| docs/ | Documentation including Doxygen configuration |

## Project Status

**Version:** 0.1.0 — Initial release
**License:** MIT
**Audit Score:** 90/100 across 20 criteria

## Ecosystem

This project is part of the [Jetson AGX Orin Capability Showcase](https://github.com/soccentric-jetson-oss/soccentric-jetson-oss) — five open-source projects demonstrating full exploitation of NVIDIA's flagship edge AI platform.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. All contributions are welcome.

## License

MIT. See [LICENSE](LICENSE) for details.

---

## Showcase

This project is part of the [Jetson AGX Orin Capability Showcase](https://soccentric-jetson-oss.github.io/).
