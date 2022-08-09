## Parallelism vs Concurrency

Parallelism refers to the ability to execute programs, or some code, at the same time in more
than one core. The CPU has matured such that modern CPU's have multiple cores. Therefore,
your computer will be able to run programs in parallel on its own.

Concurrency is when two or more processes start, run in an alternating way through
"context-switching" and complete in an overlapping time period by managing access to shared
resources on a single core.

The difference between them? Parallelism executes multiple processes on multiple cores,
whereas concurrency can run more than one event at the same time on a single core while
sharing resources between the events.

## Process vs Thread vs Task

A thread is the smallest unit of execution that can be performed on a computer. Threads are
subcomponents of a process and are normally interdependent on one another, thus sharing
resources as well. Additionally, threads are can be referred to as a "lightweight process".
Lightweight processes run in the same address space, whereas heavyweight processes execute in their own distinct address spaces.

A process is an instance of a program that can be ran. When we write/execute code, a process
is created to execute all the tasks that we have instructed the computer to do through our code.
A process can have a single, primary thread or have several threads - each with its own
stack, program counter, and instruction register. These threads also share code, data, and
memory with one another.

A task, quite simply, is a set of program instructions that are loaded in memory.

TIP: Supplementary, Short CS Definitions for the above:
Stack - order of instructions to be executed
Program Counter (P.C.) - holds addresses of next instructions
Instruction Register (I.R.) - holds the encoded instructions