/-!
# Minimum Viable Oracle — the basic model

Every claim-bearing unit of research.phext carries exactly one `Status`
(the model's stance toward the claim) and one `Basis` (why it holds
that status). The basis constrains the status through the `allowed`
table; that table *is* the receipt rule, so basis-conformance implies
receipt-backing: a True entry can only carry `stipulation`/`verified`,
a False entry only `refuted`, a Fiction entry only `construction`.

This layer proves the bookkeeping model accurate: a decidable checker
`accurate`, its soundness against `AccurateProp`, and the empty
registry. Transitions and restructuring live in `Mvo.Transitions` and
`Mvo.RegistryOps`.
-/

namespace Mvo

/-- The model's stance toward a claim: established, refuted, recorded
but not settled, or a deliberate construction. -/
inductive Status where
  | true
  | false
  | unknown
  | fiction
  deriving DecidableEq, Repr

/-- Why an entry holds its status. The basis is the receipt kind:
`stipulation` (we define it so), `verified` (a verification receipt
exists), `refuted` (a refutation receipt exists), `attributed` (a
source asserts it, unsettled), `open` (an open question), `synthesis`
(our inference, labelled), `estimate` (a calibrated judgement),
`construction` (deliberately invented for exposition). -/
inductive Basis where
  | stipulation
  | verified
  | refuted
  | attributed
  | open
  | synthesis
  | estimate
  | construction
  deriving DecidableEq, Repr

/-- One claim-bearing unit of the registry: its identity, its stance,
and the basis for that stance. -/
structure Entry where
  id : Nat
  status : Status
  basis : Basis
  deriving DecidableEq, Repr

/-- The assignment table: which status a basis may carry. -/
def allowed : Basis → Status → Bool
  | .stipulation, .true => true
  | .verified, .true => true
  | .refuted, .false => true
  | .attributed, .unknown => true
  | .open, .unknown => true
  | .synthesis, .unknown => true
  | .estimate, .unknown => true
  | .construction, .fiction => true
  | _, _ => false

/-- A registry is accurate when its ids are unique and every entry's
status is allowed for its basis. Receipt-backing is implied by
conformance given the table: the only bases that may carry `true` are
`stipulation` and `verified`, the only basis for `false` is `refuted`,
and the only basis for `fiction` is `construction`. -/
def AccurateProp (r : List Entry) : Prop :=
  (r.map Entry.id).Nodup ∧ ∀ e ∈ r, allowed e.basis e.status = true

/-- Accuracy is decidable: uniqueness is decidable over `Nat` ids and
conformance is a bounded check over a finite list. The instance does
not synthesize through the `AccurateProp` definition on its own, so it
is given explicitly against the unfolded body. -/
instance (r : List Entry) : Decidable (AccurateProp r) :=
  inferInstanceAs (Decidable ((r.map Entry.id).Nodup ∧
    ∀ e ∈ r, allowed e.basis e.status = true))

/-- The decidable accuracy checker. -/
def accurate (r : List Entry) : Bool :=
  decide (AccurateProp r)

/-- The checker is sound: a registry it accepts is accurate. -/
theorem accurate_sound {r : List Entry} (h : accurate r = true) :
    AccurateProp r :=
  of_decide_eq_true h

/-- The empty registry is accurate. -/
theorem empty_accurate : AccurateProp [] :=
  accurate_sound (by decide)

end Mvo
