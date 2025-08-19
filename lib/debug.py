#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()
    
from author import Author
from magazine import Magazine
from article import Article

a1 = Author("Alice")
a2 = Author("Bob")

m1 = Magazine("TechMag", "Technology")
m2 = Magazine("HealthMag", "Health")

ar1 = a1.add_article(m1, "The Future of AI")
ar2 = a1.add_article(m2, "Healthy Living Tips")
ar3 = a2.add_article(m1, "AI and Society")
ar4 = a1.add_article(m1, "AI in Healthcare")

print("Articles by Alice:", [a.title for a in a1.articles()])
print("Magazines Alice writes for:", [m.name for m in a1.magazines()])
print("Articles in TechMag:", m1.article_titles())
print("Contributors in TechMag:", [a.name for a in m1.contributors()])
print("Alice's Topic Areas:", a1.topic_areas())
print("Top Publisher:", Magazine.top_publisher().name)
