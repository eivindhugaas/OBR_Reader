import unittest
from SmootheningFunctions import smoothening as smth
smth=smth()
class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.dict1={1:{19.1: -8.4, 19.2: -14.2, 19.3: -11.1},2:{19.1: -13.5, 19.2: -12.2, 19.3: -16.1},4:{19.1: -8.1, 19.2: -2.2, 19.3: -1.1},5:{19.1: -3.7, 19.2: -12.7, 19.3: -1.1}}
        self.dict2={1:{19.15: -10.4, 19.25: -12.2, 19.35: -8.1},2:{19.15: -13.0, 19.25: -14.25, 19.35: -18.1},4:{19.15: -4.1, 19.25: -1.6, 19.35: -0.1},5:{19.15:-6.7, 19.25: -6.7, 19.35: 1.1}}
        
        self.dictremoved={1:{19.1: 0., 19.3: -10},2:{19.0: 0., 19.1: -1., 19.2: -2.},4:{19.1: -8.1, 19.2: -2.2, 19.3: -1.1},5:{19.1: -3.7, 19.2: -12.7, 19.3: -1.1}}

        self.dictinterpolated={1:{19.1: 0.,19.2:-5., 19.3:-10.},2:{19.1: -1., 19.2: -2., 19.3:-3.},4:{19.1: -8.1, 19.2: -2.2, 19.3: -1.1},5:{19.1: -3.7, 19.2: -12.7, 19.3: -1.1}}

        
        self.dictlist=[self.dict1,self.dict2]
        self.combineddict={1:{19.1: -8.4,19.15: -10.4, 19.2: -14.2, 19.25: -12.2, 19.3: -11.1, 19.35: -8.1},2:{19.1: -13.5,19.15: -13.0, 19.2: -12.2, 19.25: -14.25, 19.3: -16.1,19.35: -18.1},4:{19.1: -8.1,19.15: -4.1, 19.2: -2.2,19.25: -1.6, 19.3: -1.1, 19.35: -0.1},5:{19.1: -3.7,19.15:-6.7, 19.2: -12.7, 19.25: -6.7, 19.3: -1.1, 19.35: 1.1}}
        self.summeddict=  {1:{19.1: -8.4,19.15: -10.4, 19.2: -14.2, 19.25: -12.2, 19.3: -11.1, 19.35: -8.1},2:{19.1: -21.9,19.15: -23.4, 19.2: -26.4, 19.25: -26.45, 19.3: -27.2,19.35: -26.2},4:{19.1: -8.1,19.15: -4.1, 19.2: -2.2,19.25: -1.6, 19.3: -1.1, 19.35: -0.1},5:{19.1: -11.8,19.15:-10.8, 19.2: -14.9, 19.25: -8.3, 19.3: -2.2, 19.35: 1.0}}
          
        self.ndiff={1: {19.1: 0.0, 19.15: 0.0, 19.2: 0.0, 19.25: 0.0, 19.3: 0.0, 19.35: 0.0}, 2: {19.1: 0.0, 19.15: 0.0, 19.2: 0.0, 19.25: 0.0, 19.3: 0.0, 19.35: 0.0}, 4: {19.1: -0.3, 19.15: -6.3, 19.2: -12.0, 19.25: -10.6, 19.3: -10.0, 19.35: -8.0}, 5: {19.1: -9.8, 19.15: -6.3, 19.2: 0.5, 19.25: -7.55, 19.3: -15.0, 19.35: -19.2}}
        self.nnoise={1:{19.1: 0,19.15: 0, 19.2: 0, 19.25: 0, 19.3: 0, 19.35: 0},2:{19.1: 0.,19.15: 0., 19.2: 0., 19.25: 0., 19.3: 0.,19.35: 0.},4:{19.1: 0.,19.15: 0., 19.2: 1.,19.25: 1., 19.3: 1., 19.35: 0.},5:{19.1: 1.,19.15: 0., 19.2: 0., 19.25: 0., 19.3: 1., 19.35: 1.0}}
        self.nonlynoise={1:{},2:{},4:{19.2: 1.,19.25: 1., 19.3: 1.},5:{19.1: 1., 19.3: 1., 19.35: 1.}}
       
        self.mdiff={1:{},2:{},4:{},5:{}}
        self.mnoise={1:{19.1: 0.,19.15: 0., 19.2: 1., 19.25: 1., 19.3: 0., 19.35: 0.},2:{19.1: 1.,19.15: 1., 19.2: 1., 19.25: 1., 19.3: 1., 19.35: 1.},4:{19.1: 0.,19.15: 0., 19.2: 0.,19.25: 0., 19.3: 0., 19.35: 0.},5:{19.1: 0.,19.15: 0., 19.2: 1., 19.25: 0., 19.3: 0., 19.35: 0.}}
        self.monlynoise={1:{19.2: 1., 19.25: 1.},2:{19.1: 1.,19.15: 1., 19.2: 1., 19.25: 1., 19.3: 1., 19.35: 1.},4:{},5:{19.2: 1.}}
        
        self.ddiff={1: {19.1: 0.0, 19.15: 0.0, 19.2: 0.0, 19.25: 0.0, 19.3: 0.0, 19.35: 0.0}, 2: {19.1: -5.1, 19.15: -2.6, 19.2: 2., 19.25: -2.05, 19.3: -5., 19.35: -10.}, 4: {19.1: 0., 19.15: 0., 19.2: 0., 19.25: 0., 19.3: 0., 19.35: 0.}, 5: {19.1: 4.4, 19.15: -2.6, 19.2: -10.5, 19.25: -5.1, 19.3: 0., 19.35: 1.2}}
        self.dnoise={1:{19.1: 0,19.15: 0, 19.2: 0, 19.25: 0, 19.3: 0, 19.35: 0},2:{19.1: 1.,19.15: 0., 19.2: 0., 19.25: 0., 19.3: 1.,19.35: 1.},4:{19.1: 0.,19.15: 0., 19.2: 0.,19.25: 0., 19.3: 0., 19.35: 0.},5:{19.1: 1.,19.15: 0., 19.2: 1., 19.25: 1., 19.3: 0., 19.35: 0.0}}
        self.donlynoise={1:{},2:{19.1: 1., 19.3: 1.,19.35: 1.},4:{},5:{19.1: 1., 19.2: 1., 19.25: 1.}}
        
        


    def test_nesteddicts(self):
        CombDict=smth.CombineDictionaries(Dictinonary_List=self.dictlist)
        SumDict=smth.summedmeasurementdictionary(Dictionary=self.combineddict,startofcycles=[1,4],endofcycles=[2,5])
        NDiffDict, NDiffDictNoise, NDiffDictonlyNoise=smth.Noise_Over_Cycles(Number_Of_Load_Steps=2,Start_Of_Cycles=[1,4],End_Of_Cycles=[2,5],Data=self.combineddict,Max_Difference_Between_Cycles=9.,Number_Of_Gap_Mesaurements=1)
        MDiffDict, MDiffDictNoise, MDiffDictonlyNoise=smth.Noise_Over_One_Measurement(Number_Of_Cycles=2,Start_Of_Cycles=[1,4],End_Of_Cycles=[2,5],Data=self.combineddict,Max_Difference=12.)
        DispDiffDict, DispDiffDictNoise, DispDiffDictonlyNoise=smth.Noise_Over_Load_Steps(Number_Of_Cycles=2,Start_Of_Cycles=[1,4],End_Of_Cycles=[2,5],Data=self.combineddict,Max_Difference_Between_Load_Steps=4.)
        
        InterpolatedDict=smth.rbfidict(Dict=self.dictremoved,lengthlist=[19.1,19.2,19.3],measurementlist=[1,2,4,5])
        
        for measurement in self.combineddict.keys():

            self.assertDictEqual(CombDict[measurement],self.combineddict[measurement])
            self.assertDictEqual(SumDict[measurement],self.summeddict[measurement])
            
            self.assertDictEqual(NDiffDictNoise[measurement],self.nnoise[measurement])
            self.assertDictEqual(NDiffDict[measurement],self.ndiff[measurement])
            self.assertDictEqual(NDiffDictonlyNoise[measurement],self.nonlynoise[measurement])

            self.assertDictEqual(MDiffDictNoise[measurement],self.mnoise[measurement])
            self.assertDictEqual(MDiffDict[measurement],self.mdiff[measurement])
            self.assertDictEqual(MDiffDictonlyNoise[measurement],self.monlynoise[measurement])            
            
            self.assertDictEqual(DispDiffDictNoise[measurement],self.dnoise[measurement])
            self.assertDictEqual(DispDiffDict[measurement],self.ddiff[measurement])
            self.assertDictEqual(DispDiffDictonlyNoise[measurement],self.donlynoise[measurement])            
                        
            self.assertDictEqual(InterpolatedDict[measurement],self.dictinterpolated[measurement])
       


if __name__ == '__main__':
    unittest.main()