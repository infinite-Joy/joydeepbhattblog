First and foremost I would like to say is that although parallelism and concurrency are orthogonal concepts I am going to use them as if they have the same meaning and use them interchangeably throughout the post.

In recent times I have seen a lot of and interest towards parallelism. The argument is that the times are past us where the processors will gain significant in clock speeds and we have reached the limitations imposed by physics on how much fast a processor can get. Unless a total engineering paradigm shift in the way the processors are manufactured is done we are stuck with our current processing speeds.

Multi-cores and parallel processing has long been sought as the solution to this. According to `Wikipedia`_ the first multiprocessors were manufactured in the mid 1980s by the Rockwell International where they manufactured versions of the 6502 with two 6502 cores on one chip as the R65C00, R65C21, and R65C29, sharing the chip's pins on alternate clock phases. Later on the the later part of the 1990’s the big technological companies like Intel, AMD and IBM started investing in the multiple core processors. Nowadays even the smartphone with their RISC technologies have multiple cores in them.

So where does it leaves us. Many of us might be thinking how to tap this seemingly endless power if instructions running in parallel and make our programs infinitely faster. Isn't that the dream? I am of the opinion that this is not the fairy land as it seems. As is said in `this academic paper`_ and reiterated in `this coding horror blog post`_,
<blockquote>the primary hurdles in computer science are..
<p style="text-align: left;">assignment and sequence
recursion / iteration
concurrency.</p>
</blockquote>
<p style="text-align: left;">
Most of people I have met who are seasoned programmers are comfortable with assignment/sequencing and iteration. It takes some time to master and understand recursion but still it is within our logical minds to understand them. Concurrency on the other hand is a whole new beast. As they say its like a nuclear fuel which is very powerful if used in a controlled manner with sufficient checks and balances but will blow up if used carelessly leaving behind unfathomable destruction which will linger for 50 years in its wake.</p>
While I was reading Coders At Work - Reflections on the Craft of Programming - Peter Seibel the thing that struck me again and again is that so many programmers were talking about the bug that was most tough for them to debug was when it had a race condition. Taking from `Introduction to Algorithms – Thomas H. Cormen`_
<blockquote>A multi-threaded algorithm is deterministic if it always does the same thing on the same input, no matter how the instructions are scheduled on the multicore computer. It is non-deterministic if its behaviour might vary from run to run. Often a multi-threaded algorithm that is meant to be deterministic fails to be, because it contains a “deterministic race”.

Race conditions are the bane of concurrency. Famous race bugs include the Therac-25 radiation therapy machine, which killed three people and injured several others, and the North American blackout of 2003, which left over 50 million people without power. These pernicious bugs are notoriously hard to find. You can run tests in the lab for days without a single failure and only to discover your software sporadically crashes in the field.

A deteminacy race occurs when two logically parallel instructions access the same memory location and one of them involves a write.</blockquote>
Now you might think that we will check for such conditions in our code and will be careful not to involve a write. But with increasing code reuse and functionalities getting abstracted away all the time this might be harder than it seems.

Considering the above arguments I think the following rules should be followed.
<ul>
	<li>Always take the algorithmic approach to make the present program fastest. Algorithms are harder to understand but they have the have the advantage that they will give consistent results for similar output.</li>
	<li>Try to learn Haskell and incorporate functional programming concepts in our code. This will lower the amount of side-effects in our methods which will result both in more robust code and better understanding of what our code does.</li>
	<li>Concurrency maybe a good solution only in such cases as network calls which tend to be much slower and should be removed from the logical parts of the program.</li>
</ul>
There are the general thoughts. We should avoid concurrency as far as possible and in situations where they are absolutely necessary we should delegate them away to frameworks and the os as far as possible. I will highly recommend usage of frameworks and languages like `erlang`_. All in all concurrency is a highly treacherous path and must be trod with the utmost care and precaution.

.. _Wikipedia: https://en.wikipedia.org/wiki/Multi-core_processor
.. _this academic paper: http://www.cs.mdx.ac.uk/research/PhDArea/saeed/
.. _this coding horror blog post: http://blog.codinghorror.com/separating-programming-sheep-from-non-programming-goats/
.. _Introduction to Algorithms – Thomas H. Cormen: http://www.mif.vu.lt/~valdas/ALGORITMAI/LITERATURA/Cormen/Cormen.pdf
.. _erlang: http://www.erlang.org/
