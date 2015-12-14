Title: Calculating fixed-rate mortgage loans
Status: draft
Date: 2015-09-15 11:00
Category: Maths
Slug: math-mortgages

_intro_ - Understanding how real-estate mortgages are computed, and what is the best strategy to redeem them.

## The basic maths

Imagine you get a one month loan of an amount _L_, at a monthly interest rate _i_. In this situation a single payment _P_ at the end of the first and only month should suffice to pay back the load (_L_) and the interests on that loan. That is :

$$ L \cdot (1+i) - P = 0 \iff L = \frac{P}{1+i} $$

_i.e._ the loan is equal to the payment's present value.

Now suppose you get a two month loan. By the same reasoning, the following is true :

$$ (L \cdot (1+i) - P) \cdot (1+i) - P = 0 $$

With a little bit of manipulation we get :

$$ L = \frac{P}{1+i} + \frac{P}{(1+i)^2} $$

The general expression for a loan over _n_ months is :

$$ L = \frac{P}{1+i} + \frac{P}{(1+i)^2} \dotsc \frac{P}{(1+i)^n} $$

Which is a geométric series of reason $r = \frac{1}{1+i}. It is equal to :

$$ L = P \frac{r - r^{n+1}}{1-r} $$

Replacing r, and massaging the thing a little bit :

$$ i \frac{L}{P} = \frac{(1+i)^n - 1}{(1+i)^n} $$

On can now solve this equation to get the monthy payments _P_ for a given loan, the duration of the loan, etc.

## Applications


