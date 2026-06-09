#!/usr/bin/env bash
set -euo pipefail

REPO_SLUG="${AITS_REPO_SLUG:-126mingxuan/ai-assisted-therapy-support}"
REPO_REF="${AITS_REPO_REF:-main}"

cleanup_dir=""
cleanup() {
  if [[ -n "${cleanup_dir}" && -d "${cleanup_dir}" ]]; then
    rm -rf "${cleanup_dir}"
  fi
}
trap cleanup EXIT

if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "Python is required to install this Codex skill." >&2
  exit 1
fi

SCRIPT_PATH="${BASH_SOURCE[0]:-}"
REPO_DIR=""

if [[ -n "${SCRIPT_PATH}" && -f "${SCRIPT_PATH}" ]]; then
  CANDIDATE_DIR="$(cd "$(dirname "${SCRIPT_PATH}")" && pwd)"
  if [[ -d "${CANDIDATE_DIR}/skill/psychology-reflection" ]]; then
    REPO_DIR="${CANDIDATE_DIR}"
  fi
fi

if [[ -z "${REPO_DIR}" && -d "./skill/psychology-reflection" && -f "./scripts/install_codex_skill.py" ]]; then
  REPO_DIR="$(pwd)"
fi

if [[ -z "${REPO_DIR}" ]]; then
  if ! command -v curl >/dev/null 2>&1; then
    echo "curl is required for one-line installation." >&2
    exit 1
  fi
  if ! command -v tar >/dev/null 2>&1; then
    echo "tar is required for one-line installation." >&2
    exit 1
  fi

  cleanup_dir="$(mktemp -d)"
  archive="${cleanup_dir}/repo.tar.gz"
  url="https://github.com/${REPO_SLUG}/archive/refs/heads/${REPO_REF}.tar.gz"

  echo "Downloading ${REPO_SLUG}@${REPO_REF}..."
  curl -fsSL "${url}" -o "${archive}"
  tar -xzf "${archive}" -C "${cleanup_dir}"
  REPO_DIR="$(find "${cleanup_dir}" -maxdepth 1 -type d -name '*ai-assisted-therapy-support*' | head -n 1)"

  if [[ -z "${REPO_DIR}" || ! -d "${REPO_DIR}/skill/psychology-reflection" ]]; then
    echo "Could not find the skill package in the downloaded repository." >&2
    exit 1
  fi
fi

"${PYTHON_BIN}" "${REPO_DIR}/scripts/install_codex_skill.py" "$@"
