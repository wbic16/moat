import Mvo.RegistryData

-- The `decide` evaluation behind the instance theorem recurses over
-- the registry (uniqueness is a bounded check over every id pair, via
-- the decidability instances), which exceeds the elaborator's default
-- recursion depth at real registry scale (192 entries). Raise it for
-- this file; the kernel re-checks the resulting proof regardless.
set_option maxRecDepth 32768

-- The same `decide` evaluation grows with the registry: at 525
-- entries (Paper 015, 2026-11-11) the `whnf` heartbeat budget of
-- 200000 is exceeded while the 492-entry registry still fit.
-- Raise it here too; the kernel re-checks regardless.
set_option maxHeartbeats 1600000

/-!
# The instance theorem

The current registry — the data in `Mvo.RegistryData` — is accurate,
proved through the decidable checker, so the Lean kernel itself
re-verifies the data. After every ingestion, transition, or
restructure, the registry data is regenerated and this theorem is
re-proved; if it does not prove, the change is not done.
-/

namespace Mvo

/-- The current registry satisfies `AccurateProp`. -/
theorem currentRegistry_accurate : AccurateProp currentRegistry :=
  accurate_sound (by decide)

end Mvo
