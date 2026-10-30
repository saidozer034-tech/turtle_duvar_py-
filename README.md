# Duvardan Kaçan Kaplumbağa Ödevi

Bu paket ROS 2 Humble üzerinde `turtlesim` simülasyonu kullanarak kaplumbağanın duvarlara (1.0 ve 10.0 sınırlarına) yaklaştığında otomatik olarak yön değiştirmesini sağlar.

## Çalıştırma Adımları
```bash
ros2 run turtlesim turtlesim_node
ros2 run turtle_duvar_py duvar_kacan
