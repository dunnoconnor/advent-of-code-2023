
class Seed:
    def __init__(self, num:int)->None:
        self.see=num;
        self.soi=None;
        self.fer=None;
        self.wat=None;
        self.lig=None;
        self.tem=None;
        self.hum=None;
        self.loc=None;

    def set_attribute(self,convs:list,s_att_name:str,d_att_name:str) -> tuple:
        s_att = getattr(self, s_att_name);
        for c in convs:
            if s_att in range(c.source,c.source+c.ran):
                diff = s_att - c.source;
                setattr(self, d_att_name, c.dest+diff);
                break;
            else:
                setattr(self, d_att_name, s_att);