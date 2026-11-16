#!/bin/bash
# Fallback starter for the tluf-submit service, for use if the systemd
# user unit is unavailable. The preferred path is the user unit:
#   cp tluf-submit.service ~/.config/systemd/user/
#   systemctl --user daemon-reload
#   systemctl --user enable --now tluf-submit.service
# This script starts the same service under nohup and waits for health.
set -e
DIR=/home/wbic16/tluf-submit
PIDFILE="$DIR/tluf-submit.pid"
if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
  echo "already running (pid $(cat "$PIDFILE"))"
  exit 0
fi
mkdir -p /home/wbic16/tluf-submissions
cd "$DIR"
TLUF_SUBMIT_PORT=8643 TLUF_SUBMIT_DIR=/home/wbic16/tluf-submissions \
  nohup /usr/bin/python3 "$DIR/tluf-submit.py" >> "$DIR/tluf-submit.log" 2>&1 &
echo $! > "$PIDFILE"
for i in 1 2 3 4 5 6 7 8 9 10; do
  if curl -fsS http://127.0.0.1:8643/api/health >/dev/null 2>&1; then
    echo "tluf-submit healthy on 127.0.0.1:8643 (pid $(cat "$PIDFILE"))"
    exit 0
  fi
  sleep 0.5
done
echo "service did not answer /api/health — see $DIR/tluf-submit.log" >&2
exit 1
