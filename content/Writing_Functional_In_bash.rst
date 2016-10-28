Writing Functional In Bash
#######################################################

:date: 2016-10-20 10:20
:modified: 2016-10-20 00:04
:tags: programming, bash
:category: Programming
:slug: writing-functional-in-bash
:authors: Joydeep Bhattacharjee
:summary: bash in functional style


What is functional programming?
-------------------------------------------------------

It is a programming paradigm where programs are written by defining functions or expressions which evaluates into the value corrsponding
to the argument. Same like maths. The value of the function will depends on the arguments provided.
So we can say that the functions answer the question "what is defined."

On the other hand in the procedural language this is like steps needed to get to the desired language. This is similar to answering
the question: "how to do it. tell me the steps"

On the outside it seems it feels like this should be easy. But in reality this is very hard to implement and reason about.

Its because of the reasoning surrounding the code correctness is harder. Its not enough to look at the code. You must also think of all the cases and take care be extra careful of all the edge cases and take care of them. So the best case scenario becomes that the real functionality of the code is obfuscated by all the edge cases that would need to be handled

Result: Code reading is tougher; Code maintenance is tougher.

So how can we write more functional code? 

To do this we need to keep in mind what makes our code mre functional.

1. No state
------------------------------------------------------

As you know all variables in bash by default is global. This greatly hampers code reading. Now to be fair there is the ``local`` keyword but we all know that no one uses it.

So instead of the following happening where a local assignment can change the value of a global variable.

.. code-block:: bash

    a=1
    
    function nolocal {
        a=2
    }

    nolocal
    echo $a # output 2

We will do the following.

.. code-block:: bash

    a=1
    
    function nolocal {
        echo $1
    }

    echo $(nolocal 2) # output 2
    echo $a # output 1

2. no reassignment/ minimal assignment
--------------------------------------------------------

.. code-block:: bash

    using pipes
    function last_difference
    {
        grep -n "${pattern}" "${parse_file}" \
            | tail -1 | awk '{print $1}' |\
            cut -d ":" -f1
    }


    function all_differences
    {
        cat "${parse_file}" | awk 'NR>="$(last_difference)"'
    }


    function duplicates
    {
        echo "" > _tmp_dup.txt
        while read x; do
            # take only the paths
            echo "${x}" | awk '{print $3}' >> _tmp_dup.txt
        done

        # get only the duplicates
        cat _tmp_dup.txt | awk '++A[$1]==2'
    }


    function only_once
    {
        diff  <(all_differences | awk '{print $3}' | uniq )\
             <(all_differences | duplicates)
    }

    execution order - using | pipe
    
3. Referential transparency
-------------------------------------------------------------

If a program is referentially transparent then we can manipulate its programs as algebaic equations.::

    bash-4.2$ x=10
    bash-4.2$ echo $((x+1))
    11

    bash-4.2$ y="10"
    bash-4.2$ echo $((y+1))
    11

    So as you can see that the two values are the same


4. Lazy evaluation
-------------------------------------------------------------

One of the ways lazy evaluation is achieved is using the eval function although this is not generally approved of. Functions are another great way to achieve lazy programming as the functions are not actually evaluated till they are called.

Nice work using a function to delay evaluation putting the code in a function will introduce lazy evaluation to it

Also lets look into ``[[``. This does lazy evaluation ``]]``. Simple ``[]`` is not capable of doing lazy evaluation.

If you come from other functional languages then you must be familiar with the list expressions In bash it is implemented using the following construct.::

    for i in $(seq $1); do a=$(f "$a"); done

5. Writing higher order functions:
-------------------------------------------------------------

If you don't need anything fancy like delaying the evaluation of the function name or its arguments, you don't need eval.

.. code-block:: bash

    function x()      { echo "Hello world";          }
    function around() { echo before; $1; echo after; }

    around x


does what you want. You can even pass the function and its arguments this way:

.. code-block:: bash

    function x()      { echo "x(): Passed $1 and $2";  }
    function around() { echo before; "$@"; echo after; }

    around x 1st 2nd


prints.::

    before
    x(): Passed 1st and 2nd
    after

Finally for the more advanced enthusiastes I will urge you to check out the `bash-lambda`_ library for more advanced implementations of functional paradigms, like futures, filtering and lambda functions.

References:

- http://www.cs.uku.fi/~mnykanen/FOH/lectures1.pdf
- http://stackoverflow.com/questions/5672289/bash-pass-a-function-as-parameter
- http://unix.stackexchange.com/questions/60688/how-to-defer-variable-expansion
- https://lists.gnu.org/archive/html/help-bash/2014-06/msg00013.html

Older: `Migrating From Bitbucket To Github`_
---------------------------------------------------------------------------

.. _bash-lambda: https://github.com/spencertipping/bash-lambda
.. _Migrating From Bitbucket To Github: http://joydeepbhatt.com/migrating-from-bitbucket-to-github.html
