:- [labels].

sentence(s(NP, VP)) -->
    noun_phrase(NP),
    verb_phrase(VP).

pronoun_phrase(P) -->
    pronoun(P).
pronoun_phrase(s(P, NP)) -->
    pronoun(P),
    noun_phrase(NP).

noun_phrase(np(N)) -->
    noun(N).
noun_phrase(np(P)) -->
    pronoun(P).
noun_phrase(np(P, NP)) -->
    pronoun(P),
    noun_phrase(NP).
noun_phrase(npcj(N, C, NP)) -->
    noun(N),
    conjunction(C),
    noun_phrase(NP).
noun_phrase(npcj(N, C, VP)) -->
    noun(N),
    conjunction(C),
    verb_phrase(VP).
noun_phrase(np(D, NP)) -->
    det(D),
    noun_phrase(NP).
noun_phrase(np(ADJ, NP)) -->
    adj(ADJ),
    noun_phrase(NP).
noun_phrase(np(N, P, VP)) -->
    noun(N),
    pronoun_phrase(P),
    verb_phrase(VP).
noun_phrase(np(N, PP)) -->
    noun(N),
    preposition_phrase(PP).


verb_phrase(vp(V)) -->
    verb(V).
verb_phrase(vp(ADV, VP)) -->
    abverb(ADV),
    verb_phrase(VP).
verb_phrase(vp(V, NP)) -->
    verb(V),
    noun_phrase(NP).    
verb_phrase(vp(V, NP, PP)) -->
    verb(V),
    noun_phrase(NP),
    preposition_phrase(PP).
verb_phrase(vpcj(V, C, VP)) -->
    verb(V),
    conjunction(C),
    verb_phrase(VP).
verb_phrase(vp(V, PP)) -->
    verb(V),
    preposition_phrase(PP).


preposition_phrase(pp(Pre, NP)) -->
    preposition(Pre),
    noun_phrase(NP). 
preposition_phrase(pp(Pre, S)) -->
    preposition(Pre),
    sentence(S).