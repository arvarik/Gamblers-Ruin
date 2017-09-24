# Gamblers Ruin
## A Random Walk Down Despair

The term Gambler's Ruin has had many meanings throughout the years.
The most commonly used meaning is as follows:

*Despite any initial amount of wealth, a gambler will always eventually
go broke if he is consistently playing a game with a negative expected value*

This is an obvious corollay to the law of large numbers, as a gamblers wealth
will on average deviate by the expected value of the game.

Although there are older meanings of the term that are much interesting. The
original meaning of gambler's ruin is that a gambler who always raises his bet to
a fixed percentage of his wealth when he wins, but does not reduce his wealth when
he loses, will always go broke eventually. Another meaning is that a gambler with
finite wealth playing a game with 0 expected value, will always go broke eventually
when playing against an opponent with infinite wealth.

These latter two meanings are interesting because they can be modeled by something
known as a random walk. A random walk is one of the simplest forms of a stochastic
process. This project aims to model several stochastic processes through real world 
examples such as mimicing a gambler's eventual despair.


### Stochastic Processes Introduction
A stochastic process is any random occurrence usually represented by a
collection of random variables with a known probability distribution.
It is a mathematical object in the field of probability theory, and has many
real-world applications, especially in computer science and finance.

As said before, a random walk is one of the simplest stochastic process.
The simplest form of a random walk is a simple symmetric random walk, which
can easily be thought of as a fair-coin game.

Suppose you play a game where you win $1 if a fair coin (50-50 odds) lands on heads
but have to pay $1 if it lands on tails. It is a fair game since the expected value
of the game is $0.

The "walk" part of this model can be represented by a graph with the y-axis
representing your wealth, and the x-axis representing the number of games you have
played. As you play games, you always "walk" 1 unit right on the x-axis, and either
1 unit up or down depending on if you have won the game or not. The image below
shows a simple symmetric random walk.


![alt text](https://github.com/Arvind-Arik/Gamblers-Ruin/blob/master/assets/random_walk.png "Simple Symmetric Random Walk Example")


### More info
https://en.wikipedia.org/wiki/Gambler%27s_ruin

https://en.wikipedia.org/wiki/Stochastic_process

