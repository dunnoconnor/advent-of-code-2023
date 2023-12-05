from Converter import Converter
from Seed import Seed
class Almanac:
    def __init__(self, nums:list)->None:
        self.seed_list = nums;
        self.see=[];
        self.soi=[];
        self.fer=[];
        self.wat=[];
        self.lig=[];
        self.tem=[];
        self.hum=[];
        self.min_loc=999999999;
  
    # def get_seeds(self,nums:int)->list:
    #     arr = [];
    #     for num in nums:
    #         arr.append(Seed(int(num)));
    #     return arr;

    def convert(self,curr_type:str,inputs:list) -> None:
        this_converter = Converter(int(inputs[0]),int(inputs[1]),int(inputs[2]));
        att = getattr(self, curr_type)
        att.append(this_converter)
    
    def set_seed_atrributes(self) -> None:
        for ran in self.seed_list:
            for s in range(ran[0],ran[1]): 
                this_seed=Seed(s);
                i=0;
                attr_list =["see","soi","fer","wat","lig","tem","hum","loc"];
                while i<len(attr_list)-1:
                    convs = getattr(self, attr_list[i]);
                    this_seed.set_attribute(convs,attr_list[i],attr_list[i+1]);
                    i+=1;
                if this_seed.loc<self.min_loc:
                    self.min_loc = this_seed.loc;
