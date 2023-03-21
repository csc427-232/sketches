
## Turing Machine Simulator Syntax 

The file `turing_machine_simulator.py` as two classes, `Turing Machine` and `MachineParser`.

The simulator class instantiates an object containing the rules, the states and alphabets, 
and can run and depict the run. To ease programming, the parser class creates the Turing Machine
and writes its program from a description given in the following syntax.



The file is a sequence of stanzas. Each stanza starts with a head line starting 
in the first column. The first word in the head line as a keyword indicating 
the type of stanza. A stanza may have continuation lines, each are indented.

The # character starts a comment, and the comment extends to the end of the line. 
Since the # is used for this  purpose it cannot be a tape symbol. If you wish to code programs 
in the textbook that use the # symbol, substitute with one of the allowed punctuations. 
I tend to use the ampersand, &amp; as a pound sign substitute.

The grammar:

<pre>
  M -> (Stanza [emptyline])*
  Stanza -> StartStanza | TapesStanza | AcceptStanza | RejectStanza | StateStanza
  StartStanza -> "start:" Ident
  TapesStanza -> "tapes:" number
  AcceptStanza -> "accept:" Ident (\n\t Ident)*
  RejectStanza -> "reject:" Ident (\n\t Ident)*
  StateStanza -> "state:" Ident (\n\t StateTransition)+
  StateTransition -> (Symbol|Special){k} (Symbol|Special){k} Action{k} Ident
  Symbol -> tape symbols are alphanumeric or punctuation ! $ % & ( ) * + , - . or /
  Special -> the : and _
  Action -> the characters l, r and n or uppercase L, R and N.
  Ident -> a nonempty string of alphanumerics
</pre>

There must be exactly one start, accept and reject stanzas.

The tape stanza must occur before any state stanza.

The underscore (_) substitutes for the blank. It is the default chacters of all unfilled cells on the tape.
Using the blank for the initial tape contents is allowed, it will be rewritten to the underscore character.

An Ident is the label of a state.

A StateStanza names to from state after the colon and each StateTransition line gives
one transition per line,

<pre>    read-symbol write-symbol action new-state </pre>

For general `k` tapes,

<pre> read-tape-1 ... read-tape-k write-tape-1 .. write-tape-k action-tape-1 ... action-tape-k new-state </pre>

The action is either l, r or n, meaning move left, move right, or no move. 
If the code for the action captialized (L, R, or N) the machine configuration is printed after the transition.

The colon (:) is a wildcard. Its use among the k read symbols matches any symbol. 
Four use cases are allowed, and are listed in the priority the case is applied,

    No wildcards. An exact match of the k type symbols has top precedence.
    One wildcard. An exact match for all but one symbol is tried if 
       there is no exact match.
    k-1 wildcards. An exact match for exactly one symbol, the k-1 are wildcards, 
       is tried next.
    All wildcards. The default matches anything.

When the wildcard appearing as a write symbol, it is set equal to the read symbol, on the corresponding tape.
Priority within one of the four classes is right to left.

A missing transition halts with reject. This and the wildcard are convenience features to
shorten the TM programs.

If the machine rejects, it can be queried for the cause of the reject,

    Reject becaues halted in a reject state.
    Reject because of a missing transition.
    Reject bedcause the computation terminated for excessive computation steps.

The method is_exception classes the first two rejects as correct computations, and the last as an exception.

See these [examples](https://github.com/csc427-232/sketches/blob/main/turing_machine_sketch.ipynb).

