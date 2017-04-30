Title: Adding checks against random data for shell submissions
Date: 2017-04-30
Slug: randomizers

One of the nice features of coding challenge sites like [hackerrank](https://hackerrank.com) is that
when you submit an algorithm it will also be checked against random data. This
validates the performance of the algorithm and will test it against different inputs.
[CMD Challenge](https://cmdchallenge.com) is a web application that executes shell commands
remotely in a Docker container. When it was initially
launched, all the checker did was validate the output of the execution
against a list of strings, expressed in YAML.

For example, the ["hello world" challenge](https://cmdchallenge.com/#/hello_world):

```yaml
  - slug: hello_world
    description: |
      Print "hello world".
      Hint: There are many ways to print text on
      the command line, one way is with the 'echo'
      command.
    expected_output:
      lines:
        - 'hello world'

```

When the user submits "`echo hello world`" the command is executed remotely and
the response is validated against the string "`hello world`". This worked fine for commands
that only needed to be verified by checking their output, but what about commands that
modify files on disk? For these types of challenges there are a
[a set of shell scripts](https://github.com/jarv/cmdchallenge/tree/master/ro_volume/cmdtests)
that also run inside the container and will return non-zero if any of pre-determined tests fail.
This is how the ["delete files"](https://cmdchallenge.com/#/delete_files),
["remove files with extension"](https://cmdchallenge.com/#/remove_files_with_extension)
challenges and other similar ones work to ensure the bash one-line command you entered
is correct.

This solves most of the validation but what about this challenge?

```yaml
  - slug: sum_all_numbers
    description: |
      The file sum-me.txt has a list of numbers,
      one per line. Print the sum of these numbers.
    expected_output:
      lines:
        - "42"
```

One way you can "trick" the site is to simply enter the command "`echo 42`" which
is the correct sum of the numbers in "`sum-me.txt`".
In fact, a lot of random internet people did exactly that
as you can see from a small subset of submissions that were previously
marked as "correct":

```bash
echo 42
echo '42'
echo "42"
echo "4""2"
expr 41 + 1
echo $(( 29 + 13))
etc. etc.
```

So the next natural thing to do is to add a way to randomize the data that the
command is operating on. Just like scripts added to run tests, now there are
bash scripts for every challenge that allow you to manipulate files before
running the command again.  Only if the output is still correct 
(and tests pass, if they are present) will
then the challenge be marked as correct.

For example, for the ["sum all numbers"](https://cmdchallenge.com/#/sum_all_numbers) challenge
the script looks like this:

```bash
#!/bin/bash
echo $(( $RANDOM % 1000 )) >> sum-me.txt
paste -sd+ sum-me.txt | bc
exit 0
```

<div style="float: right;margin-right: 1em; margin-left: .5em;">
    <a href="https://cmdchallenge.com/#/sum_all_numbers"><img src="https://i.imgur.com/rkqKXjW.png" alt="randomizers" /></a>
</div>

Now if you type the command "`echo 42`" the randomizer check will fail since will also verify that
the command can run against the modified "`sum-me.txt`" file.
Currently, there are a randomizer scripts added for a subset of challenges.
If you want to contribute and add more please feel free to send a [pull request](https://github.com/jarv/cmdchallenge/pulls).
If you would like to
read some more about how the site is built in an AWS free tier account see the earlier post on 
[building cmdchallenge](/building-cmdchallenge.html). If you liked this write up let me know
by following [@thecmdchallenge](https://twitter.com/thecmdchallenge) on twitter or drop
me mail at <a href="mailto:info@cmdchallenge.com">info@cmdchallenge.com</a>.

Thanks!

