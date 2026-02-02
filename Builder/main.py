from builder import GamingComputerBuilder, OfficeComputerBuilder, ComputerDirector

if __name__ == "__main__":
    director = ComputerDirector()

    print("--- Building Gaming Computer ---")
    gaming_builder = GamingComputerBuilder()
    director.construct(gaming_builder)
    computer1 = gaming_builder.get_result()
    computer1.show()

    print("\n" + "="*30 + "\n")

    print("--- Building Office Computer ---")
    office_builder = OfficeComputerBuilder()
    director.construct(office_builder)
    computer2 = office_builder.get_result()
    computer2.show()
