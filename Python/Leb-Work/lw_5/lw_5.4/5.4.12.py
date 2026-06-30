#12. Form a hierarchy (Grandparent $\rightarrow$ Parent $\rightarrow$ Child) and cross-verify relationships using
#issubclass().

class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

# Testing subclass relationships across multiple levels
print("Is Child a subclass of Parent?", issubclass(Child, Parent))
print("Is Child a subclass of Grandparent?", issubclass(Child, Grandparent))
print("Is Parent a subclass of Grandparent?", issubclass(Parent, Grandparent))
print("Is Grandparent a subclass of Child?", issubclass(Grandparent, Child))
