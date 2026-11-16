#!/bin/bash
# install-submit.sh — wire the tluf.org paper-submission API into nginx.
#
# Run as root on awsbox:
#   sudo bash /home/wbic16/tluf-submit/install-submit.sh
#
# What it does:
#   1. Checks the submission service answers on its loopback port
#      (it runs as wbic16's systemd user unit — no root needed for it).
#   2. Backs up the live, certbot-managed nginx config for tluf.org.
#   3. Inserts the /api/submit + /api/health proxy blocks into the
#      site's HTTPS server block (idempotent — safe to re-run; the
#      certbot TLS blocks are never touched).
#   4. Gates on `nginx -t`, then reloads nginx.
#   5. Verifies the public endpoints end to end.
set -e

CONF=/etc/nginx/sites-available/tluf.org
INSERT=/home/wbic16/tluf-submit/nginx-insert.py
STAMP=$(date +%Y%m%d-%H%M%S)

echo "== 1/5 service on loopback =="
if curl -fsS http://127.0.0.1:8643/api/health; then
  echo
else
  echo "WARNING: the submission service is not answering on 127.0.0.1:8643." >&2
  echo "It runs as wbic16's user unit; check: systemctl --user status tluf-submit" >&2
  echo "Continuing — the final public verification will fail if it stays down." >&2
fi

echo "== 2/5 backup =="
cp -a "$CONF" "$CONF.bak-$STAMP"
echo "backed up to $CONF.bak-$STAMP"

echo "== 3/5 insert proxy blocks =="
python3 "$INSERT" "$CONF"

echo "== 4/5 nginx -t and reload =="
nginx -t
systemctl reload nginx

echo "== 5/5 public verification =="
echo "-- https://tluf.org/api/health"
curl -fsS https://tluf.org/api/health
echo
echo "-- https://tluf.org/submit.html"
curl -fsSI https://tluf.org/submit.html | head -n 1
echo "DONE — the submission feature is wired."
