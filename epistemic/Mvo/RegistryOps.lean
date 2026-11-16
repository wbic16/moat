import Mvo.Basic

/-!
# Ingestion and restructuring operations

The operations that change a registry's membership, each proved to
preserve accuracy:

- `enter`: a new conformant entry with a fresh id.
- `retireEntry`: remove an entry (the remainder stays accurate).
- `mergeEntries`: remove two entries and enter one entry carrying
  their shared status and basis under a fresh id.
- `splitEntry`: replace one entry by two entries with the same
  status and basis under fresh, distinct ids.

Together with the legal transitions (`Mvo.Transitions`), these are
the only ways the registry changes — so accuracy, once established,
is never lost.
-/

namespace Mvo

/-- Entering a new conformant entry with a fresh id preserves
accuracy. -/
theorem enter_preserves {r : List Entry} {e : Entry}
    (hacc : AccurateProp r) (hconf : allowed e.basis e.status = true)
    (hfresh : e.id ∉ r.map Entry.id) :
    AccurateProp (e :: r) := by
  obtain ⟨hnd, hc⟩ := hacc
  refine ⟨?_, ?_⟩
  · rw [List.map_cons, List.nodup_cons]
    exact ⟨hfresh, hnd⟩
  · intro x hx
    rcases List.mem_cons.mp hx with rfl | hx'
    · exact hconf
    · exact hc x hx'

/-- Remove every entry with the given id. (In an accurate registry
there is at most one.) -/
def removeById : List Entry → Nat → List Entry
  | [], _ => []
  | e :: rest, i => if e.id = i then removeById rest i
    else e :: removeById rest i

/-- Removal only ever drops entries: what remains was already there. -/
theorem mem_removeById {x : Entry} (r : List Entry) (i : Nat) :
    x ∈ removeById r i → x ∈ r := by
  induction r with
  | nil =>
    intro h
    simp only [removeById] at h
    cases h
  | cons e rest ih =>
    intro h
    simp only [removeById] at h
    by_cases hi : e.id = i
    · rw [ite_eq_left hi] at h
      exact List.mem_cons_of_mem e (ih h)
    · rw [ite_eq_right hi] at h
      rcases List.mem_cons.mp h with rfl | h'
      · exact List.mem_cons_self
      · exact List.mem_cons_of_mem e (ih h')

/-- The ids of a removed-from registry are among the original ids. -/
theorem mem_map_id_removeById {n : Nat} (r : List Entry) (i : Nat) :
    n ∈ (removeById r i).map Entry.id → n ∈ r.map Entry.id := by
  intro h
  obtain ⟨x, hx, rfl⟩ := List.mem_map.mp h
  exact List.mem_map_of_mem (mem_removeById r i hx)

/-- Removal preserves id uniqueness. -/
theorem nodup_map_id_removeById (r : List Entry) (i : Nat) :
    (r.map Entry.id).Nodup → ((removeById r i).map Entry.id).Nodup := by
  induction r with
  | nil =>
    intro h
    exact h
  | cons e rest ih =>
    intro h
    rw [List.map_cons, List.nodup_cons] at h
    obtain ⟨hne, hnd⟩ := h
    simp only [removeById]
    by_cases hi : e.id = i
    · rw [ite_eq_left hi]
      exact ih hnd
    · rw [ite_eq_right hi, List.map_cons, List.nodup_cons]
      exact ⟨fun hm => hne (mem_map_id_removeById rest i hm), ih hnd⟩

/-- Retire: remove the entry with the given id, keeping the rest
(with its redirect, at the phext layer). -/
def retireEntry (r : List Entry) (i : Nat) : List Entry :=
  removeById r i

/-- Retiring an entry preserves accuracy: the remainder of an
accurate registry is accurate. -/
theorem retire_preserves {r : List Entry} {i : Nat}
    (hacc : AccurateProp r) : AccurateProp (retireEntry r i) := by
  obtain ⟨hnd, hconf⟩ := hacc
  exact ⟨nodup_map_id_removeById r i hnd,
    fun x hx => hconf x (mem_removeById r i hx)⟩

/-- Merge: remove two entries and enter one entry in their place,
carrying the status and basis the two shared, under a fresh id. -/
def mergeEntries (r : List Entry) (i j : Nat) (e' : Entry) :
    List Entry :=
  e' :: removeById (removeById r i) j

/-- Merging preserves accuracy. -/
theorem merge_preserves {r : List Entry} {e1 e2 e3 : Entry}
    (hacc : AccurateProp r) (h1 : e1 ∈ r) (_h2 : e2 ∈ r)
    (_hstatus : e2.status = e1.status) (_hbasis : e2.basis = e1.basis)
    (hs3 : e3.status = e1.status) (hb3 : e3.basis = e1.basis)
    (hfresh : e3.id ∉
      (removeById (removeById r e1.id) e2.id).map Entry.id) :
    AccurateProp (mergeEntries r e1.id e2.id e3) := by
  have hconf3 : allowed e3.basis e3.status = true := by
    rw [hs3, hb3]
    exact hacc.2 e1 h1
  have step1 : AccurateProp (removeById r e1.id) :=
    retire_preserves hacc
  have step2 : AccurateProp (removeById (removeById r e1.id) e2.id) :=
    retire_preserves step1
  exact enter_preserves step2 hconf3 hfresh

/-- Split: replace one entry by two entries, both carrying the
original entry's status and basis, under fresh distinct ids. -/
def splitEntry (r : List Entry) (i : Nat) (e1 e2 : Entry) :
    List Entry :=
  e2 :: e1 :: removeById r i

/-- Splitting preserves accuracy. (Freshness of `e2` against
`e1 ::` the remainder is what makes the two new ids distinct.) -/
theorem split_preserves {r : List Entry} {e e1 e2 : Entry}
    (hacc : AccurateProp r) (he : e ∈ r)
    (hs1 : e1.status = e.status) (hb1 : e1.basis = e.basis)
    (hs2 : e2.status = e.status) (hb2 : e2.basis = e.basis)
    (hfresh1 : e1.id ∉ (removeById r e.id).map Entry.id)
    (hfresh2 : e2.id ∉ (e1 :: removeById r e.id).map Entry.id) :
    AccurateProp (splitEntry r e.id e1 e2) := by
  have hconf : allowed e.basis e.status = true := hacc.2 e he
  have hconf1 : allowed e1.basis e1.status = true := by
    rw [hs1, hb1]
    exact hconf
  have hconf2 : allowed e2.basis e2.status = true := by
    rw [hs2, hb2]
    exact hconf
  have step1 : AccurateProp (removeById r e.id) :=
    retire_preserves hacc
  have step2 : AccurateProp (e1 :: removeById r e.id) :=
    enter_preserves step1 hconf1 hfresh1
  exact enter_preserves step2 hconf2 hfresh2

end Mvo
