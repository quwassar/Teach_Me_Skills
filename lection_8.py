class Processors():
    def __init__(self, architecture: str, **kwargs):
        self.architecture = architecture
        super().__init__(**kwargs)
    
    def get_type_processor(self):
        return f'Processor have architecture {self.architecture}'
    

class ARM():
    def __init__(self, type_cores: str, **kwargs):
        self.type_cores = type_cores
        super().__init__(**kwargs)

class Hybrid(Processors, ARM):
    def __init__(self, brand: str, model: str, **kwargs):
        self.brand = brand
        self.model = model
        super().__init__(**kwargs)

intel_hybrid = Hybrid(type_cores='low 8, power 8', model='i9', architecture='Hybrid x86', brand='Intel')

print(intel_hybrid.brand)
print(intel_hybrid.model)
print(intel_hybrid.architecture)
print(intel_hybrid.type_cores)
