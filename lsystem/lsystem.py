class Lsystem():
    # This holds the production rules.
    rules = {}
    
    # Generates the L-system according to the input string, and the number of iterations you want to run for.
    def run(self, input, iterations):
        # For each iteration, apply the production rules and return the resulting string.
        current_string = input
        new_string = ''
        print(current_string)
        for i in range(0,iterations):
            for x in current_string:
                if(x in self.rules):
                    new_string += self.rules[x]
                else:
                    new_string += x
            current_string = new_string
            new_string = ''
            print(current_string)
        return current_string
    
    # Enables you to establish the rules for the L-system. Pass in the symbol and its replacement.
    def addRule(self, symbol, replacement):
        self.rules[symbol] = replacement

# Create a demo L-system with symbols A, B, C.
lsystem = Lsystem()
lsystem.addRule('A', 'B')
lsystem.addRule('C', 'BA')
lsystem.run('BABACAB', 10)
    
