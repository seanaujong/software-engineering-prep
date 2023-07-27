# Propositional Logic

The rules of logic give precise meaning to mathematical statements, distinguishing between valid and invalid mathematical arguments. The rules of logic are used in the construction and verification of correct computer programs.

## Propositions

Propositions are the basic building blocks of logic.

`proposition` - a declarative sentence that is either true or false, but not both

- a `declarative` sentence declares a fact

Examples: "Washington, D.C. is the capital of the USA" and "2 + 2 = 3"

Examples of non-propositions: "What time is it?" and "Read this carefully."

New propositions, called `compound propositions`, are formed from existing propositions using `logical operators`.

### Truth Tables

![](img/1-truth-table.png) ![](img/2-3-truth-table.png)

A truth table lists every possible input combination to a system, along with the outputs. `Table 2` has a row for each of the possible combinations of truth values of `p` and `q`. Each row shows the truth value of `p AND q` given the truth values of `p` and `q` for that row.

## Conditional Statements

![](img/4-5-truth-table.png)

A `conditional statement` like `p -> q` asserts that if `p` is true, then `q` MUST be true as well. We say that "`p` implies `q`".

We know `p -> q` is false in the scenario where `p` is true but `q` is false. In this scenario, we say that "`p` does not `imply` `q`".

### Example: Politician Pete's Promise

> Politician Pete promises, "If I am elected, then I will lower taxes."

- `p`: "Pete is elected"
- `q`: "Pete will lower taxes"
- `p -> q`: "If Pete is elected, then Pete will lower taxes"

We say that `p -> q` does not hold when Pete breaks his promise. Consider the following scenarios:

- "Pete is not elected; taxes are lowered"
    - Promise kept
    - Here, Pete does not have the chance to keep his promise, but taxes happen to get lowered anyways
- "Pete is not elected; taxes are not lowered"
    - Promise kept
    - Why? Because Pete only promised to lower taxes if he got elected!

Notice how in these two scenarios, we don't expect anything from Pete if he doesn't get elected. However, what if he actually does get elected?

- "Pete is elected; taxes are lowered"
    - Promise kept
    - Pete actually follows through on his promise!
- "Pete is elected; taxes are not lowered"
    - Promise broken!
    - This is the only scenario where we can conclusively say that Pete is a dirty liar

### Inverse, Converse, and Contrapositive

We can form some new conditional statements starting from `p -> q`.

- `inverse` - `~p -> ~q`
- `converse` - `q -> p`
- `contrapositive` - `~q -> ~p`

The contrapositive always has the same truth value as `p -> q`. Why? Because the contrapositive is false only when `~q` is true but `~p` is false.

- In other words, the contrapositive is false only when `q` is false but `p` is true ("Pete was elected, but taxes were not lowered").
- When two compound propositions always have the same truth values, we call them `equivalent`

The inverse and the converse, on the other hand, never have the same truth value as `p -> q`. This means they are only true when `p` is true but `q` is false ("Pete was elected, but taxes were not lowered").

<img src="img/inverse-converse-contrapositive-truth-table.png" width="250"/>

#### Inverse, Converse, and Contrapositive Example

> "The home team wins whenever it is raining"

- `p`: "It is raining"
- `q`: "The home team wins"
- `p -> q`: "If it is raining, then the home team wins"
- `~p -> ~q`: "If it is not raining, then the home team will not win"
- `q -> p`: "If the home team wins, then it is raining"
- `~q -> ~p`: "If the home team does not win, then it is not raining"

### Biconditionals

The `biconditional statement`, `p <-> q`, asserts that `p` and `q` have the same truth values. We say that "p holds if and only if q holds".

`p <-> q` has the same truth value as `(p -> q) AND (q -> p)`

> "You can take the flight iff you buy a ticket"

This statement is true when we don't take the flight and don't buy a ticket. This statement is still true when we take the flight and we buy a ticket. However, this statement is false when we take the flight but don't buy a ticket (if the trip is free). This statement is also false when we don't take the flight but buy a ticket (if the airline bumps you)
