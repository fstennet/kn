class command():
    def __init__(self, domain, question):
        if domain == None or question == None:
            raise Exception(f"Must provide domain and question parameters.\nDomain: {domain}\nQuestion: {question}")
        
        self.domain = domain
        self.question = question