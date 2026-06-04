#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Installing Psychology Reflection for Codex..."
echo
"${SCRIPT_DIR}/install.sh" "$@"
echo
echo "Installation complete."
echo "You can close this window."
read -r -p "Press Return to exit..." _
