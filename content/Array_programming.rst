Array Programming
##################################

I recently went to an amazing workshop given by the famous Morten Kormberg. It was on APL language. There he introduced us the the concept of array programming. So lets dive into the related concepts.

Array programming is brought about as opposed to scalar programming. Scalar programming a paradigm in thinking where even if the data-stucture is brought in the form of a list (or other traditional datastructures), the operation on the data is done element wise. For example if we try to give an example to express the addition of two vectors or two lists, then in scalar scalar languages it would become in a  similar psedo-code as shown below.::

    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            a[i][j] += b[i][j];

In APL the whole array would be thought about in chunks. Hence the addition of two vectors can be seen like below.::

        1 2 3 + 4 5 6
    5 7 9

Python always had similar array proogramming constructs using the map, lambda, reduce keywords.::

    map(function, list)

But this construct was limited since you could only apply it to a unidimensional vector and hence was not true array programming. Thus traditionally python has been scalar. But with the advent of the numpy package and we could do so much more. Given `below example`_ for the same addition of two vectors in numpy.::

    >>> import numpy
    >>> a=numpy.array([0,1,2])
    >>> b=numpy.array([3,4,5])
    >>> a+b
    array([3, 5, 7])
    >>>

The premise of array programming is that everything is a vector. A scalar is a vector of 0 dimensions. Similarly other datastructures are just higher dimensional vectors. Hence in array programming the programmer will think on whole aggregates of data instead of breaking the data to individual "scalar" parts to be consumed by the algorithm.

Now the question comes why should you as a programmer leave the current "safe" and familiar paradigm and start thinking in more abstract vectors. Lets look at the advantages.

- Array programming model is a more high-level model and frees you from the task of breaking down or looping on the individual data point. You can just pass the whole matrix to the algorithm/function. Thus you will be delegating the unnecassy work to the compiler/interpreter and will be free to concentrate more on the more advanced portions of your respective problem.
- You will be using the a well built library/interpreter to do the complex calculations which will definitely be faster that the simple loop constructs that you will be creating.
- Less code and hence less code debt. Less maintenence cost.
- The code is more amenable to formal proofs. You can employ algorithms that have been proven to be true and the algorithms can be written in one line. Instead of writing 10 lines to show matrix multiplication you can for example just write ``a +.* b`` in APL.

Apart from these obvio

.. _below example: http://stackoverflow.com/questions/845112/concise-vector-adding-in-python/845139#845139

References:

http://www.eecg.toronto.edu/~jzhu/csc326/readings/iverson.pdf
http://www.cs.odu.edu/~cs381/cs381content/induction/use_of_induction_loop.html
