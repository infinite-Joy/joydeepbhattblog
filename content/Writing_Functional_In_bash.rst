source: http://www.cs.uku.fi/~mnykanen/FOH/lectures1.pdf

what is functional programming?

it is a programming paradigm where programs are written by defining functions or expressions which evaluates into the value corrsponding
to the argument. Same like maths. The value of the function will depends on the arguments provided.
So we can say that the functions answer the question "what is defined."

On the other hand in the procedural language this is like steps needed to get to the desired language. This is similar to answering
the question: "how to do it. tell me the steps"

On the outside it seems it feels like this should be easy. But in reality this is very hard to implement and reason about. 
Its because the reasoning surrounding the code correctness is harder. Why? Its because...
- its not enough to look at the code.
- you must also think of all the cases and take care be extra careful of all the edge cases and take care of them
- so the best case scenario becomes that the real functionality of the code is obfuscated by all the edge cases that would need to be handled

Result: Code reading is tougher; Code maintenance is tougher.


So how can we write more functional code? 

to do this we need to keep in mind what makes our code mre functional.

1. No state

As you know all variables in bash is global. this greatly hampers code reading.

# give some code examples here

2. no reassignment/ minimal assignment

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

3. if a program is referentially transparent then we can manipulate its programs as algebaic equations
bash-4.2$ x=10
bash-4.2$ echo $((x+1))
11

bash-4.2$ y="10"
bash-4.2$ echo $((y+1))
11

So as you can see that the two values are the same


4. lazy evaluation

Nice work using a function to delay evaluation

putting the code in a function will introduce lazy evaluation to it

http://unix.stackexchange.com/questions/60688/how-to-defer-variable-expansion

https://lists.gnu.org/archive/html/help-bash/2014-06/msg00013.html

[[ # does lazy evaluation ]] while [] doesnt

list expressions in bash: for i in $(seq $1); do a=$(f "$a"); done

# writing higher order functions:

If you don't need anything fancy like delaying the evaluation of the function name or its arguments, you don't need eval:
function x()      { echo "Hello world";          }
function around() { echo before; $1; echo after; }

around x


does what you want. You can even pass the function and its arguments this way:
function x()      { echo "x(): Passed $1 and $2";  }
function around() { echo before; "$@"; echo after; }

around x 1st 2nd


prints
before
x(): Passed 1st and 2nd
after

http://stackoverflow.com/questions/5672289/bash-pass-a-function-as-parameter

#####################################################

check out the following library for more advanced implementations of functional paradigms

https://github.com/spencertipping/bash-lambda

like futures, filtering and lambda functions
