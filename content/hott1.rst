Homotopy Type Theory: 0.Prehistory
##################################

:Status: published
:tags: foundations
:category: research
:author: Andrei Halanay

.. class:: center

*This series of posts documents my attempt to understand Univalent foundations
and Homotopy Type Theory. In this one I present the motivations of V.A.Voevodsky
for introducing the Univalent Foundations.*

Our `story <https://www.ias.edu/ideas/2014/voevodsky-origins>`_ begins with `this paper
<http://www.sciencedirect.com/science/article/pii/0001870886900812>`_ by Spencer
Bloch. It is one of the founding stones in the area of motivic cohomology, but
unfortunately a fundamental result was shown to be false by A.A. Suslin, shortly
after publication, and there was no alternative proof. So the paper turned into
a collection of conjectures. Only in 1993 a correct proof was published.

In order to progress in this area, V.A. Voevodsky, A.A. Suslin and Eric
Friedlander took a different path, which avoided the work of Bloch and relied on
a paper of Voevodsky written in 1992-1993 and published in 1995. While giving a
series of lectures presenting the results in this paper at the IAS in 2000,
Voevodsky discovered a gap in it. Fortunately he was able to prove a weaker
result and to recover the main results. As a consequence of this fact, he was
shocked that despite many groups of mathematicians studied his paper nobody was
able to spot the mistake, and took his results for granted.

An even scarier chain of events began with the publication of a preprint of
Carlos Simpson, stating that the fundamental result in a paper by Voevodsky and
M.M. Kapranov is wrong. Simpson was not able to identify the mistake and he only
produced a counter-example. In fact it was not clear if there really was a
mistake in the paper of Kapranov and Voevodsky or one in the example of Simpson.
In 2013 Voevodsky finally came to the conclusion that indeed there is a mistake
in their paper, but as this `question
<https://mathoverflow.net/questions/234492/what-is-the-mistake-in-the-proof-of-the-homotopy-hypothesis-by-kapranov-and-voev>`_
shows it is not easy to understand what precisely is wrong.

This state of affairs in which significant mistakes in important and rather
widely read (at least by the standards of mathematics) went undetected for
decades was a shock to Voevodsky who began thinking about how to correct
this. The obvious solution was to use computers to check the proofs. 

At this time (some twenty years ago) there was very little interest of "real"
mathematicians for computer proof-assistants. They were used mostly by computer
scientists for formal verification of software and hardware. A more serious
problem was find a new foundation of mathematics as the classical
Zermelo-Fraenkel axioms together with the axiom of choice was not appropriate
for Voevodsky's needs and also do not play very well with various attempts of
formalization in a computer-friendly way.

The most promising candidate was the Calculus of Inductive Constructions, which
was developed in the same time with the `Coq <https://coq.inria.fr>`_ proof
assistant. Coq is rather well known among computer scientists as the language
used in the `Software Foundations <https://softwarefoundations.cis.upenn.edu/>`_
course and as the basis of the book `Certified Programming with Dependent Types <http://adam.chlipala.net/cpdt/cpdt.pdf>`_
by Adam Chlipala. Voevodsky chose this framework for his work on building a new
foundational system for mathematics which he called **univalent foundations**.

The Calculus of Inductive Constructions is a form a **type theory** more
precisely a form of inductive type theory, a foundational system alternative to
set theory. Type theory will be the object of the next post.
