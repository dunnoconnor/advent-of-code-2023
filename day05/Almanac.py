from Converter import Converter
from Seed import Seed
class Almanac:
    def __init__(self, nums:int)->None:
        self.seed_list = self.get_seeds(nums)
        self.see=[];
        self.soi=[];
        self.fer=[];
        self.wat=[];
        self.lig=[];
        self.tem=[];
        self.hum=[];
  
    def get_seeds(self,nums:int)->list:
        arr = [];
        for num in nums:
            arr.append(Seed(int(num)));
        return arr;

    def convert(self,curr_type:str,inputs:list) -> None:
        this_converter = Converter(int(inputs[0]),int(inputs[1]),int(inputs[2]));
        att = getattr(self, curr_type)
        att.append(this_converter)
    
    def set_seed_atrributes(self) -> None:
        for seed in self.seed_list:
            seed.set_attribute(self.see,"see","soi");
            seed.set_attribute(self.soi,"soi","fer");
            seed.set_attribute(self.fer,"fer","wat");
            seed.set_attribute(self.wat,"wat","lig");
            seed.set_attribute(self.lig,"lig","tem");
            seed.set_attribute(self.tem,"tem","hum");
            seed.set_attribute(self.hum,"hum","loc");
    
    def sort_coverts(self) -> None:
        self.see.sort()
        self.soi.sort()
        self.fer.sort()
        self.wat.sort()
        self.lig.sort()
        self.tem.sort()
        self.hum.sort()

    def print_attrs(self) -> None:
        for c in self.see:
            print(c.dest, c.source);
        for c in self.soi:
            print(c.dest, c.source);
        for c in self.fer:
            print(c.dest, c.source);
        for c in self.wat:
            print(c.dest, c.source);
        for c in self.lig:
            print(c.dest, c.source);
        for c in self.tem:
            print(c.dest, c.source);
        for c in self.hum:
            print(c.dest, c.source);

