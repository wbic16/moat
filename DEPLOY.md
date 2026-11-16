# DEPLOY — tluf.org deployment map

## What deploys where

| Source | Deploys to | Path / unit |
|---|---|---|
| wbic16/site-tluf-org@exo (`index.html`, `submit.html`) | awsbox (100.78.221.38 tailnet / 44.248.235.76 public) | docroot `/sites/web/tluf.org/` |
| wbic16/moat@exo `service/` | awsbox | `/home/wbic16/tluf-submit/` (wbic16-writable) |
| wbic16/site-quickfork-net@exo | awsbox | docroot `/sites/web/quickfork.net/` (index.html + assets; deployed by direct docroot install, not push-to-deploy) |

Site files are staged with mode 644 (files) / 755 (dirs). nginx on awsbox is
root-owned and certbot-managed; wbic16 has no passwordless sudo, so root
steps are Will's-hands, run from prepared kits — never worked around.

## The submissions service

- Unit: systemd user unit `tluf-submit.service` (enabled, running since
  2026-11-16 00:13 UTC), user wbic16.
- Listens on loopback only: 127.0.0.1:8643.
- Endpoints: `POST /api/submit`, `GET /api/health`.
- Queue: `/home/wbic16/tluf-submissions/` (empty at last check).
- The Python canonicalizer lives inside `service/tluf-submit.py`; the JS
  canonicalizer is `service/canon.js`, embedded verbatim into submit.html by
  `service/build-submit-page.py`. There is no separate canon file on awsbox —
  both canonicalizers travel inside the two deployed files.

## Repo ↔ awsbox byte identity (verified 2026-11-16)

awsbox `/home/wbic16/tluf-submit/` matches `service/` here, SHA-256:

- `tluf-submit.py` — 16946f68822fb94aef4aff6c4ad1acb7a8407f0cb75cfeac644e524000be759d
- `install-submit.sh` — 2fe194dd5dc4ee82a4aa8788738c76f04a83b741877b752ed4a04393a4f5c1e1
- `nginx-insert.py` — 3edbf2747447d9039fa8525479fc4c4f1f6709b9ea7863e71034e7c0a6edb3c1
- `submit.html` — c63dbf8c4b8a02222dd008e6944da9acc07ebb2a122152c292384e148ac9534f

awsbox docroot `/sites/web/tluf.org/` matches wbic16/site-tluf-org@exo and
the live fetch, SHA-256:

- `index.html` — aa114fe365c6d32e3f1a57e512b2d073d4b4c6ed56f008f4d5656366d31e8014
- `submit.html` — c63dbf8c4b8a02222dd008e6944da9acc07ebb2a122152c292384e148ac9534f

## The one outstanding root step (Will's-hands)

On awsbox, Will runs:

```
sudo bash /home/wbic16/tluf-submit/install-submit.sh
```

It inserts the `/api/` proxy blocks into the live certbot-managed nginx
config via `nginx-insert.py` (backup first, `nginx -t` gate, self-verifying;
it does not overwrite the live conf). Nothing else is outstanding: the
service is running and loopback-tested (arXiv locator → 201
`px2:arxiv:2611.14552`; bare numeric ID → 400 AMBIGUOUS-SOURCE).

## Post-step verification

1. `https://tluf.org/api/health` returns 200 publicly (today: 404).
2. One real end-to-end submission from https://tluf.org/submit.html.
3. Confirm the submission file lands in `/home/wbic16/tluf-submissions/`.
4. Then close task 42.9.6/12.6.15/5.8.10 in the house task register.
