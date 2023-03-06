
## Turing Machine Simulator Syntax 

The Turing Machine Simulator has two classes. The first is the Turing Machine Simulator. The object takes a 
Python dictionary describing the states and transitions. The second object is a parser that takes a text
description and creates the dictionary object needed by the Turing Machine. This makes it easier to write
the program.

This is a description of the syntax and language features of the parser.

The file is a sequence of stanzas. Each stanza starts with a head line starting 
in the first column. The first word in the head line as a keyword indicating 
the type of stanza. A stanza may have continuation lines, each are indented.

The # character starts a comment, and the comment extends to the end of the line. 
Since the # is used for this 
purpose it cannot be a tape symbol. If you wish to code programs in the textbook that use
the # symbol, substitute with one of the allowed punctuations.

The syntax can be described by the following grammar.

- __M__ -> (__Stanza__ [emptyline])*
- __Stanza__ -> __StartStanza__ | __TapesStanza__ | __AcceptStanza__ | __RejectStanza__ | __StateStanza__
- __StartStanza__ -> "start:" __Ident__
- __TapesStanza__ -> "tapes:" number
- __AcceptStanza__ -> "accept:" __Ident__ (\n\t __Ident__)*
- __RejectStanza__ -> "reject:" __Ident__ (\n\t __Ident__)*
- __StateStanza__ -> "state:" __Ident__ (\n\t __StateTransition__)+
- __StateTransition__ -> (__Symbol__|__Special__){k} (__Symbol__|__Special__){k} __Action__ __Ident__
- __Symbol__ -> tape symbols are alphanumeric or punctuation ! $ % & ( ) * + , - . or /
- __Special__ -> the : and _
- __Action__ -> the characters l, r and n or uppercase L, R and N.
- __Ident__ -> a nonempty string of alphanumerics

There must be exactly one start, accept and reject stanzas.

The tape stanza must occur before any state stanza.

The underscore (_) substitutes for the blank. It is the default chacters of all unfilled cells on the tape.
Using the blank for the initial tape contents is allowed, it will be rewritten to the underscore character.

An Ident is the label of a state.

A StateStanza names to from state after the colon and each StateTransition line gives
one transition according to the syntax (for the case of k=1):

<pre>    read-symbol write-symbol action new-state </pre>

For the case of k&gt;1, 
The StateTransition line is interpreted as first the k tape symbols to match on the k tapes; then the k tape symbols to write on the k tapes, then the k actions to undertake on the k tapes.

The action is either l, r or n, meaning move left, move right, or no move. As a debuging feature, if the code for the action captialized the machine configuration is printed after the transition.

The colon (:) is a wildcard. It's use among the k read symbols matches any symbol. Four use cases are allowed, and are listed in the priority the case is applied,

    No wildcards. An exact match of the k type symbols has top precedence.
    One wildcard. An exact match for all but one symbol is tried if 
       there is no exact match.
    k-1 wildcards. An exact match for exactly one symbol, the k-1 are wildcards, 
       is tried next.
    All wildcards. The default matches anything.

When the wildcard appearing as a write symbol, it is set equal to the read symbol, on the corresponding tape.

A missing transition halts with reject. This and the wildcard are convenience features to
shorten the TM programs.

If the machine rejects, it can be queried for the cause of the reject,

    Reject becaues halted in a reject state.
    Reject because of a missing transition.
    Reject bedcause the computation terminated for excessive computation steps.

The method is_exception classes the first two rejects as correct computations, and the last as an exception.
