from abc import ABC, abstractmethod

# Product
class Computer:
    def __init__(self):
        self.parts = {}

    def add(self, part_type, part_spec):
        self.parts[part_type] = part_spec

    def show(self):
        print("\nComputer Specifications:")
        for part, spec in self.parts.items():
            print(f"{part}: {spec}")

# Abstract Builder
class ComputerBuilder(ABC):
    def __init__(self):
        self.computer = Computer()

    @abstractmethod
    def build_cpu(self):
        pass

    @abstractmethod
    def build_ram(self):
        pass

    @abstractmethod
    def build_storage(self):
        pass

    @abstractmethod
    def build_gpu(self):
        pass

    def get_result(self):
        return self.computer

# Concrete Builder 1
class GamingComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.add("CPU", "High-End Gaming CPU (e.g., Intel i9 or AMD Ryzen 9)")

    def build_ram(self):
        self.computer.add("RAM", "32GB DDR5")

    def build_storage(self):
        self.computer.add("Storage", "2TB NVMe SSD")

    def build_gpu(self):
        self.computer.add("GPU", "NVIDIA RTX 4090")

# Concrete Builder 2
class OfficeComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.add("CPU", "Mid-Range CPU (e.g., Intel i5)")

    def build_ram(self):
        self.computer.add("RAM", "16GB DDR4")

    def build_storage(self):
        self.computer.add("Storage", "512GB SSD")

    def build_gpu(self):
        self.computer.add("GPU", "Integrated Graphics")

# Director
class ComputerDirector:
    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder.build_cpu()
        self._builder.build_ram()
        self._builder.build_storage()
        self._builder.build_gpu()
