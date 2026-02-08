import platform

print(platform.system())        # 操作系统名称 (Windows/Linux/Darwin)
print(platform.release())       # 系统版本
print(platform.version())       # 详细版本
print(platform.machine())       # 机器架构 (x86_64, arm64)
print(platform.processor())     # CPU 信息
print(platform.node())          # 主机名
print(platform.platform())      # 完整平台信息