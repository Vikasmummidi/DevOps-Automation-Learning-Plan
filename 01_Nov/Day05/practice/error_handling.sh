set -euo pipefail
# -e exit on error
# -u unset variable error
# -o pipefail pipeline or error

command || { "echo command failed"; exit 1; }
