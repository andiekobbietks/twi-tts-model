#!/bin/bash

# Instance configuration
LOCATION="Manchester"
GPU_TYPE="A40"
OS="Ubuntu 22.04 x64"
BACKUP="enabled"

# Startup script
cat << 'EOF' > startup.sh
#!/bin/bash
apt update && apt upgrade -y
apt install -y nvidia-driver-535
apt install -y nvidia-cuda-toolkit
apt install -y python3-pip python3-venv
nvidia-smi
EOF
