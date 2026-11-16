import Mvo

/-!
Trust-surface check. Run with `lake env lean checks/Axioms.lean`
after `lake build`. Expected: only the standard axioms
(`propext`, `Classical.choice`, `Quot.sound`) — no `sorryAx`, no
`Lean.ofReduceBool` (which would mean `native_decide` dependence).
-/

open Mvo

#print axioms accurate_sound
#print axioms empty_accurate
#print axioms LegalTransition.id_eq
#print axioms LegalTransition.conformant
#print axioms replace_preserves
#print axioms enter_preserves
#print axioms retire_preserves
#print axioms merge_preserves
#print axioms split_preserves
#print axioms currentRegistry_accurate
