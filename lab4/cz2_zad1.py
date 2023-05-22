from collections import Counter

def Sequential_covering(Target_attribute, Attributes, Examples, Threshold):
    
    def classify_examples(rule, examples):
        decision_values = [example[Target_attribute] for example in examples]
        return all([rule['decision'] == decision_value for decision_value in decision_values])
    
    def performance(rule, examples):
        correctly_classified = [example for example in examples if classify_examples(rule, [example])]
        return len(correctly_classified) / len(examples)
    
    def learn_one_rule(Target_attribute, Attributes, Examples):
        remaining_attributes = set(Attributes) - set([Target_attribute])
        best_rule = None
        best_coverage = 0
        
        for attribute in remaining_attributes:
            attribute_values = set([example[attribute] for example in Examples])
            for value in attribute_values:
                covered_examples = [example for example in Examples if example[attribute] == value]
                rule = {'attribute': attribute, 'value': value, 'decision': None}
                rule['decision'] = Counter([example[Target_attribute] for example in covered_examples]).most_common(1)[0][0]
                rule_coverage = len(covered_examples)
                if rule_coverage >= best_coverage:
                    best_rule = rule
                    best_coverage = rule_coverage
        
        return best_rule
    
    Learned_rules = []
    Rule = learn_one_rule(Target_attribute, Attributes, Examples)
    
    while performance(Rule, Examples) > Threshold :
        Learned_rules.append(Rule)
        Examples = [example for example in Examples if not classify_examples(Rule, [example])]
        Rule = learn_one_rule(Target_attribute, Attributes, Examples)

    Learned_rules.append(Rule)
    Learned_rules = sorted(Learned_rules, key=lambda rule: performance(rule, Examples), reverse=True)
    
    return Learned_rules


Target_attribute = 'Decision'
Attributes = ['Attribute1', 'Attribute2', 'Attribute3']
Examples = [
    {'Attribute1': 'wysoka', 'Attribute2': 'bliski', 'Attribute3': 'średni', 'Decision': 'tak'},
    {'Attribute1': 'wysoka', 'Attribute2': 'bliski', 'Attribute3': 'średni', 'Decision': 'tak'},
    {'Attribute1': 'wysoka', 'Attribute2': 'bliski', 'Attribute3': 'średni', 'Decision': 'tak'},
    {'Attribute1': 'więcej', 'Attribute2': 'daleki', 'Attribute3': 'silny', 'Decision': 'nie pewne'},
    {'Attribute1': 'więcej', 'Attribute2': 'daleki', 'Attribute3': 'silny', 'Decision': 'nie'},
    {'Attribute1': 'więcej', 'Attribute2': 'daleki', 'Attribute3': 'lekki', 'Decision': 'nie'},
    {'Attribute1': 'wysoka', 'Attribute2': 'bliski', 'Attribute3': 'średni', 'Decision': 'tak'},
    {'Attribute1': 'więcej', 'Attribute2': 'daleki', 'Attribute3': 'lekki', 'Decision': 'nie'},
    {'Attribute1': 'więcej', 'Attribute2': 'daleki', 'Attribute3': 'lekki', 'Decision': 'tak'}
]
Threshold = 0.5

rules = Sequential_covering(Target_attribute, Attributes, Examples, Threshold)
print(rules)