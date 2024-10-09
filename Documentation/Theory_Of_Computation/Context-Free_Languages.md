CONTEXT-FREE GRAMMAR (CFG)
--------------------------

A context-free grammar is a 4-tuple (V,Σ,R,S), where

1. V is a finite set called the variables,
2. Σ is a finite set, disjoint from V, called the terminals,
3. R is a finite set of rules, with each rule being a variable and a string of variables and terminals, and
4. S ∈ V is the start variable.


DESIGNING CONTEXT-FREE GRAMMARS
-------------------------------

As with the design of finite automata, the design of context-free
grammars requires creativity. Indeed, context-free grammars are even
trickier to construct than finite automata because we are more
accustomed to programming a machine for specific tasks than we are to
describing languages with grammars. The following techniques are
helpful, singly or in combination, when you’re faced with the problem
of constructing a CFG.

First, many CFLs are the union of simpler CFLs. If you must construct
a CFG for a CFL that you can break into simpler pieces, do so and then
construct individual grammars for each piece. These individual
grammars can be easily merged into a grammar for the original language
by combining their rules and then adding the new rule S→S1|S2|···|Sk,
where the variables Si are the start variables for the individual
grammars. Solving several simpler problems is often easier than
solving one complicated problem.


CHOMSKY NORMAL FORM
-------------------

A context-free grammar is in Chomsky normal form if every rule is of
the form

  A → BC
  A → a

where a is any terminal and A, B, and C are any variables —- except
that B and C may not be the start variable. In addition, we permit the
rule S → ε, where S is the start variable.

Any context-free language is generated by a context-free grammar in
Chomsky normal form.

PROOF IDEA:

We can convert any grammar G into Chomsky normal form.  The conversion
has several stages wherein rules that violate the conditions are
replaced with equivalent ones that are satisfactory. First, we add a
new start variable. Then, we eliminate all ε-rules of the form A→ε. We
also eliminate all unit rules of the form A→B. In both cases we patch
up the grammar to be sure that it still generates the same
language. Finally, we convert the remaining rules into the proper
form.

PROOF:

First, we add a new start variable S0 and the rule S0→S, where S was
the original start variable. This change guarantees that the start
variable doesn’t occur on the right-hand side of a rule.  Second, we
take care of all ε-rules. We remove an ε-rule A→ε, where A is not the
start variable. Then for each occurrence of an A on the right-hand
side of a rule, we add a new rule with that occurrence deleted. In
other words, if R→uAv is a rule in which u and v are strings of
variables and terminals, we add rule R→uv. We do so for each
occurrence of an A, so the rule R→uAvAw causes us to add R→uvAw,
R→uAvw, and R→uvw. If we have the rule R→A, we add R→ε unless we had
previously removed the rule R→ε. We repeat these steps until we
eliminate all ε-rules not involving the start variable. Third, we
handle all unit rules. We remove a unit rule A→B. Then, whenever a
rule B→u appears, we add the rule A→u unless this was a unit rule
previously removed. As before, u is a string of variables and
terminals. We repeat these steps until we eliminate all unit rules.
Finally, we convert all remaining rules into the proper form. We
replace each rule A→u1u2···uk, where k≥3 and each ui is a variable or
terminal symbol, with the rules A→u1A1, A1→u2A2, A2→u3A3, ..., and
Ak−2→uk−1uk. The Ai’s are new variables. We replace any terminal ui in
the preceding rule(s) with the new variable Ui and add the rule Ui→ui.


PUSHDOWN AUTOMATON (PDA)
------------------------

A pushdown automaton is a 6-tuple (Q,Σ,Γ,δ,q0,F), where Q, Σ, Γ, and F
are all finite sets, and

1. Q is the set of states,
2. Σ is the input alphabet,
3. Γ is the stack alphabet,
4. δ: Q×Σε×Γε−→P(Q×Γε) is the transition function,
5. q0∈Q is the start state, and
6. F⊆Q is the set of accept states.

A pushdown automaton M=(Q,Σ,Γ,δ,q0,F) computes as follows. It accepts
input w if w can be written as w=w1w2···wm, where each wi∈Σε and
sequences of states r0,r1,...,rm ∈ Q and strings s0,s1,...,sm ∈ Γ∗
exist that satisfy the following three conditions. The strings si
represent the sequence of stack contents that M has on the accepting
branch of the computation.

1. r0=q0 and s0=ε. This condition signifies that M starts out
   properly, in the start state and with an empty stack.
2. For i=0,...,m−1, we have (ri+1,b) ∈ δ(ri,wi+1,a), where si=at and
   si+1=bt for some a,b∈Γε and t∈Γ∗. This condition states that M
   moves properly according to the state, stack, and next input
   symbol.
3. rm∈F. This condition states that an accept state occurs at the
   input end.


PUSHDOWN AUTOMATON IS EQUIVALENT WITH CONTEXT-FREE GRAMMARS
-----------------------------------------------------------

1. If a language is context free, then some pushdown automaton
   recognizes it.

2. If a pushdown automaton recognizes some language, then it is
   context free.

Because every regular language is recognized by a finite automaton and
every finite automaton is automatically a pushdown automaton that
simply ignores its stack, we now know that every regular language is
also a context-free language.


DETERMINISTIC PUSHDOWN AUTOMATON
--------------------------------

A deterministic pushdown automaton is a 6-tuple (Q,Σ,Γ,δ,q0,F), where
Q, Σ, Γ, and F are all finite sets, and

1. Q is the set of states,
2. Σ is the input alphabet,
3. Γ is the stack alphabet,
4. δ: Q×Σε×Γε −→ (Q×Γε) ∪ {∅} is the transition function,
5. q0 ∈ Q is the start state, and
6. F ⊆ Q is the set of accept states.

The transition function δ must satisfy the following condition. For
every q∈Q, a∈Σ, and x∈Γ, exactly one of the values δ(q,a,x), δ(q,a,ε),
δ(q,ε,x), and δ(q,ε,ε) is not ∅.