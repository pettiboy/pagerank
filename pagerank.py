import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    distribution = dict()
    final_distribution = dict()
    
    if len(corpus[page]) > 0:
        linked_pages_probability = damping_factor / len(corpus[page])

        for page_linked in corpus[page]:
            distribution[page_linked] = linked_pages_probability
        
        additional_probability = (1 - damping_factor) / len(corpus)

        for a_page in corpus:
            if a_page in distribution:
                distribution[a_page] += additional_probability
            else:
                distribution[a_page] = additional_probability
    
    # if page has no outgoing links, all pages have equal probability
    else:
        for each_page in corpus:
            distribution[each_page] = 1 / len(corpus)

    return distribution



def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """    
    random_page = random.choice(list(corpus.keys()))
    samples = list()
    samples.append(random_page)

    for i in range(n):
        trans_model = transition_model(corpus, random_page, damping_factor)
        keys = list()
        values = list()

        for key, value in trans_model.items():
            keys.append(key)
            values.append(value)

        next_page = random.choices(keys, weights=values, k=1)[0]
        samples.append(next_page)
        random_page = next_page

    pageranks = dict()
    for page in corpus:
        pageranks[page] = samples.count(page) / len(samples)

    return pageranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    keep_looping = True
    pageranks = dict()

    for page in corpus.keys():
        pageranks[page] = 1 / len(corpus.keys())

    while keep_looping:

        pagerank_copy = pageranks.copy()

        for page in corpus:
            summation = 0
            for link in corpus:
                if page in corpus[link]:
                    summation += pagerank_copy[link] / len(corpus[link])
                if not corpus[link]:
                    summation += pagerank_copy[link] / len(corpus)
        
            fixed_value = (1 - damping_factor) / len(corpus)
            pageranks[page] = fixed_value + (damping_factor * summation)

            if abs(pagerank_copy[page] - pageranks[page]) < 0.001:
                keep_looping = False       

    return pagerank_copy

if __name__ == "__main__":
    main()
