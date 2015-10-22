Title: Investigating France's elections against gross domestic product
Status: published
Category: Data science
Slug: pib-elections
Summary: Finding the correlation between GDP evolution and presidential election results

I've recently been doing some reading on forecasting electoral results, and I came accross an article from [Libération](http://liberation.fr) about vote functions applied to the 2002 french presidential elections. Yes, the same elections that ended up with an extreme-right party leader on the second round.

The article, " [Pour l'Iowa, avantage Jospin](http://www.liberation.fr/tribune/2002/03/21/pour-l-iowa-avantage-jospin_397638) ", was written by Michael S. Lewis-Beck and Christine Fauvelle-Aymar, two economists working on the Iowa forcasting algorithms back in the late 90's. The basic idea of those algorithms was using economic and political results to predict voting behaviours. In their Libération article, they apply some simple vote functions to try to predict the 2002 results.

Anyway, early in the article they write that the correlation between the economic situation in France and presidential election results is around 0.7. I set off to try to reproduce these results. You can [view the detailed notebook](http://nbviewer.ipython.org/github/gaspaio/notebooks/blob/master/elections/PIB.ipynb), but here's a short version.

The gross domestic product (PIB in french) is an easy indicator of the economic health of the country. [The official numbers from INSEE](http://www.bdm.insee.fr/bdm2/affichageSeries?idbank=001690224&codeGroupe=1540) are released quarterly :

![GDP in France since 1958]({filename}/images/pib_pib.png)

To measure the economic situation of the country at a given time, we can take diffs and look at the PIB variations over time :

![GDP in France since 1958]({filename}/images/pib_evol.png)

Predictive models that use economic information to forecast election results are based on the hypothesis that a given political color tends to be reelected if all goes well, economy-wise, and vice-versa. So, in theory, elections where there is a presidential color switch should be immediately preceded by periods where PIB variation is negative.

After collecting the relevant election dates and results :

![GDP in France and Presidential elections]({filename}/images/pib_evol_pres.png)

The blues area is the time where a France had a right wing president (from De Gaule to Sarkozy), and the pink areas indicates a left wing president (from Mitterrand to Holand). The white vertical lines are election dates.

The **Point-biserial correlation coefficient** between PIB evolution sign and presidential color switches is : $r_{pb} = -0.45$.

So, indeed, correlation is negative : when PIB goes down, presidents tend to be ejected. This fact explains 45% of the variance in presidential election results.

We can scatter-plot this relationship :

![GDP in France and Presidential elections]({filename}/images/pib_evol_pres_scat.png)

Clearly, most elections with a negative of low PIB variation resulted in a presidential colour switch. On the other hand, the result if highly biased by what is called the "Trente glorieuses" (the thirty glorious years). From 1945 to 1975, french economy grew considerably (PIB variation > 1% per quarter), with a stable right-wing gouvernment until the early eighties. This kind of growth is not likelly to come back anytime soon, so one should storngly question the predictive power of my little investigation.

I still would like to known where Lewis-Beck and Christine Fauvelle-Aymar got the 70% correlation between economy and presidential election behaviour.

**Resources :**

* [IPython Notebook](http://nbviewer.ipython.org/github/gaspaio/notebooks/blob/master/elections/PIB.ipynb)
* [IPython Notebook sources](https://github.com/gaspaio/notebooks/tree/master/elections)
