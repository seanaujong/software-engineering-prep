# Sets

> All of mathematics can be described with sets.

A `set` is a collection of things called `elements`.

Example: the collection of all integers, $\Z = \{...,-1,0,1,...\}$

- the dots (`...`) indicate a pattern of numbers that continue forever in both positive and negative directions
- A set is `infinite` if it has infinitely many elements, otherwise it is `finite`

Two sets are `equal` if they contain the exact same elements, regardless of order

- $A = \{1,2,3,4\} = \{4,3,2,1\}$
  - $2 \in A$
  - $5 \notin A$
- $\{...,-2,-1,0,1,2,...\} = \{0,-1,1,-2,2,...\}$
- $\N = \{1,2,3,...\}$
  - the set of natural numbers (positive whole numbers)
- $\R =$ set of real numbers

The `cardinality` or `size` of a finite set is the number of how many elements it has.

- $|A| = 4$

The `empty set` is the set with no elements. The empty set is the only set with a cardinality of 0. Think of the empty set as an empty box. The `box analogy` can help us think about sets.

- $\empty = \{\}, |\empty| = 0$
- $\empty \neq \{\empty\}$

`Set-builder notation` is used to describe sets that are too big or complex to list between braces.

- $X = \{expression : rule\}$
- $E = \{..., -4, -2, 0, 2, 4, ...\}= \{2n : n \in \Z\} = \{n : n = 2k, k \in \Z\}$
  - $E$ equals the set of all things of form $2n$ such that $n$ is an element of $\Z$
  - Can also be written as $E = \{n \in \Z\ |\ n\ is\ even\}$

---

Example: Describe the set $A = \{7a + 3b : a, b \in \Z\}$

- This set contains all numbers of form $7a + 3b$, where $a$ and $b$ are integers.
- Each such number $7a + 3b$ is an integer, so $A$ contains only integers.
- But which integers? If $n$ is any integer, then
    - $n = 7n + 3(-2n) = 7a + 3b$, where
    - $a = n$ and
    - $b = -2n$
- Therefore $n \in A$
- We've now shown that $A$ contains only integers, and also that every integer is an element of $A$.
- Therefore $A = \Z$

[Why choose $a = n, b = -2n$?](https://math.stackexchange.com/questions/3739448/describe-the-set-a-7a-3b-a-b-in-mathbbz)

---

We close this section with a summary of special sets:

- The empty set: $\empty = \{\}$
- The natural numbers: $\N = \{1,2,3,4,5\}$
- The integers: $\Z = \{...,-3,-2,-1,0,1,2,3,...\}$
- The rational numbers: $\mathbb{Q} = \{x : x = \frac{m}{n}, where\ m,n \in \Z\ and\ n \neq 0\}$
- The real numbers: $\R$

Notice that $\mathbb{Q}$ is the set of all numbers in $\R$ that can be expressed as a fraction of two integers.
