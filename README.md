# Pagerank

## Disclaimer

This is a [CS50 AI](https://cs50.harvard.edu/ai/2020/) project.
If you currently a CS50 AI student it is against the [Acadmic Honestly](https://cs50.harvard.edu/x/2021/honesty/) to view the solution.
Learn more about this problem set [here](https://cs50.harvard.edu/ai/2020/projects/2/pagerank/).

## Usage

### clone this repository

```
git clone git@github.com:pettiboy/pagerank.git
```

### run

```
python3 pagerank.py corpus2
```

## About

> When search engines like Google display search results, they do so by placing more “important” and higher-quality pages higher in the search results than less important pages. But how does the search engine know which pages are more important than other pages?
>
> One heuristic might be that an “important” page is one that many other pages link to, since it’s reasonable to imagine that more sites will link to a higher-quality webpage than a lower-quality webpage. We could therefore imagine a system where each page is given a rank according to the number of incoming links it has from other pages, and higher ranks would signal higher importance.
>
> But this definition isn’t perfect: if someone wants to make their page seem more important, then under this system, they could simply create many other pages that link to their desired page to artificially inflate its rank.
>
> For that reason, the PageRank algorithm was created by Google’s co-founders (including Larry Page, for whom the algorithm was named). In PageRank’s algorithm, a website is more important if it is linked to by other important websites, and links from less important websites have their links weighted less. This definition seems a bit circular, but it turns out that there are multiple strategies for calculating these rankings.
