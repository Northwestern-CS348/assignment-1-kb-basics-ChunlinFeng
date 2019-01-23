import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        if len(self.facts) == 0:    self.facts.append(fact);
        else:
            whetherStore = 1  # flag to determine whether store the fact

            # check if the item is already in the fact_list
            for stored_facts in self.facts:
                whetherMatch = match(stored_facts.statement, fact.statement, None) # return false if it is a new fact

                if(whetherMatch != False):
                    whetherStore = 0 # do not save the fact
                    break

            if(whetherStore): self.facts.append(fact); # judge whether store it


        print("Asserting {!r}".format(fact))
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        if len(self.facts) == 0: return False;
        else:
            ListOfBindings = []
            for stored_facts in self.facts:
                whetherMatch = match(stored_facts.statement, fact.statement, None)

                if(whetherMatch != False): ListOfBindings.append(whetherMatch);

            if (len(ListOfBindings) == 0): return False;
            else: return ListOfBindings;

        print("Asking {!r}".format(fact))
