import Mvo.Basic

/-!
# Legal transitions

A status may only change along the edges of `LegalTransition`, and
every edge names the receipt that licenses it: no edge enters `true`
except verification, no edge enters `false` except refutation, and
`fiction` never goes directly to `true` — a construction is first
taken up as an unsettled proposal (`unknown`), and only a later
verification can settle it. The identity (no change) is legal.

This layer proves that applying a legal transition to one entry of an
accurate registry — replacing that entry, found by id — yields an
accurate registry.
-/

namespace Mvo

/-- A legal change from entry `e` to entry `e'`: same id, and the
(status, basis) change is one of the receipt-licensed edges. -/
inductive LegalTransition : Entry → Entry → Prop where
  /-- No change. -/
  | identity (e : Entry) : LegalTransition e e
  /-- A verification receipt arrives: unsettled → true/verified. -/
  | verify {e e' : Entry} (hid : e.id = e'.id)
      (hfrom : e.status = .unknown)
      (hstatus : e'.status = .true) (hbasis : e'.basis = .verified) :
      LegalTransition e e'
  /-- A refutation receipt arrives: unsettled → false/refuted. -/
  | refuteUnknown {e e' : Entry} (hid : e.id = e'.id)
      (hfrom : e.status = .unknown)
      (hstatus : e'.status = .false) (hbasis : e'.basis = .refuted) :
      LegalTransition e e'
  /-- A refutation receipt arrives: true → false/refuted (the claim
  is demoted; its history is kept). -/
  | refuteTrue {e e' : Entry} (hid : e.id = e'.id)
      (hfrom : e.status = .true)
      (hstatus : e'.status = .false) (hbasis : e'.basis = .refuted) :
      LegalTransition e e'
  /-- A refutation receipt is invalidated: false → unknown, held as
  attributed, reopened, synthesis, or estimate. -/
  | reopenFalse {e e' : Entry} (hid : e.id = e'.id)
      (hfrom : e.status = .false)
      (hstatus : e'.status = .unknown)
      (hbasis : e'.basis = .attributed ∨ e'.basis = .open ∨
        e'.basis = .synthesis ∨ e'.basis = .estimate) :
      LegalTransition e e'
  /-- A construction is taken up as a real proposal: fiction →
  unknown, held as attributed or synthesis. -/
  | reopenFiction {e e' : Entry} (hid : e.id = e'.id)
      (hfrom : e.status = .fiction)
      (hstatus : e'.status = .unknown)
      (hbasis : e'.basis = .attributed ∨ e'.basis = .synthesis) :
      LegalTransition e e'
  /-- A claim is reclassified as exposition: unknown →
  fiction/construction. -/
  | fictionalize {e e' : Entry} (hid : e.id = e'.id)
      (hfrom : e.status = .unknown)
      (hstatus : e'.status = .fiction) (hbasis : e'.basis = .construction) :
      LegalTransition e e'

/-- A legal transition never changes the entry's id. -/
theorem LegalTransition.id_eq {e e' : Entry} (h : LegalTransition e e') :
    e.id = e'.id := by
  cases h with
  | identity => rfl
  | verify hid => exact hid
  | refuteUnknown hid => exact hid
  | refuteTrue hid => exact hid
  | reopenFalse hid => exact hid
  | reopenFiction hid => exact hid
  | fictionalize hid => exact hid

/-- The target of a legal transition out of a conformant entry is
conformant: every edge lands on a (status, basis) pair the `allowed`
table accepts. -/
theorem LegalTransition.conformant {e e' : Entry}
    (h : LegalTransition e e')
    (hc : allowed e.basis e.status = true) :
    allowed e'.basis e'.status = true := by
  cases h with
  | identity => exact hc
  | verify hid hfrom hstatus hbasis => rw [hstatus, hbasis]; decide
  | refuteUnknown hid hfrom hstatus hbasis => rw [hstatus, hbasis]; decide
  | refuteTrue hid hfrom hstatus hbasis => rw [hstatus, hbasis]; decide
  | reopenFalse hid hfrom hstatus hbasis =>
    rw [hstatus]
    rcases hbasis with h | h | h | h <;> rw [h] <;> decide
  | reopenFiction hid hfrom hstatus hbasis =>
    rw [hstatus]
    rcases hbasis with h | h <;> rw [h] <;> decide
  | fictionalize hid hfrom hstatus hbasis => rw [hstatus, hbasis]; decide

/-- Replace the entry whose id is `e'.id` by `e'`, leaving every other
entry untouched. (In an accurate registry ids are unique, so at most
one entry is replaced.) -/
def replaceById (r : List Entry) (e' : Entry) : List Entry :=
  r.map fun e => if e.id = e'.id then e' else e

theorem replaceById_cons (e : Entry) (rest : List Entry) (e' : Entry) :
    replaceById (e :: rest) e' =
      (if e.id = e'.id then e' else e) :: replaceById rest e' :=
  rfl

/-- Replacement never changes the registry's id list. -/
theorem replaceById_map_id (r : List Entry) (e' : Entry) :
    (replaceById r e').map Entry.id = r.map Entry.id := by
  induction r with
  | nil => rfl
  | cons e rest ih =>
    rw [replaceById_cons, List.map_cons, List.map_cons, ih]
    by_cases h : e.id = e'.id
    · rw [ite_eq_left h, h]
    · rw [ite_eq_right h]

/-- Every entry of a replaced registry is either the replacement or
was already there. -/
theorem mem_replaceById {y : Entry} {r : List Entry} {e' : Entry}
    (h : y ∈ replaceById r e') : y = e' ∨ y ∈ r := by
  obtain ⟨x, hx, hxy⟩ := List.mem_map.mp h
  by_cases hcond : x.id = e'.id
  · rw [ite_eq_left hcond] at hxy
    exact Or.inl hxy.symm
  · rw [ite_eq_right hcond] at hxy
    exact Or.inr (hxy ▸ hx)

/-- Applying a legal transition to one entry of an accurate registry
yields an accurate registry. -/
theorem replace_preserves {r : List Entry} {e e' : Entry}
    (hacc : AccurateProp r) (he : e ∈ r) (hleg : LegalTransition e e') :
    AccurateProp (replaceById r e') := by
  obtain ⟨hnd, hconf⟩ := hacc
  refine ⟨?_, ?_⟩
  · rw [replaceById_map_id]
    exact hnd
  · intro y hy
    rcases mem_replaceById hy with rfl | hyr
    · exact hleg.conformant (hconf e he)
    · exact hconf y hyr

end Mvo
