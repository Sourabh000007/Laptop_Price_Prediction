import pandas as pd
import numpy as np
import json
import pickle
import warnings
import math
warnings.filterwarnings("ignore")
import config


class Laptop_Price():

    def __init__(self,Ram,Weight,Touchscreen,Ips,resolution, inches,HDD,SSD,Company,TypeName,Cpu_brand,Gpu_brand,os):

        self.Ram                      = Ram
        self.Weight                   = Weight
        self.Touchscreen              = Touchscreen
        self.Ips                      = Ips
        self.ppi                      = self.calculate_ppi(resolution, inches)
        self.HDD                      = HDD
        self.SSD                      = SSD
        self.Company                  = "Company_" + Company
        self.TypeName                 = "TypeName_" + TypeName
        self.Cpu_brand                = "Cpu_brand_" + Cpu_brand
        self.Gpu_brand                = "Gpu_brand_" + Gpu_brand
        self.os                       = "os_" + os

    def load_models(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.load_model = pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.load_json = json.load(f)

    def calculate_ppi(self, resolution, inches):
        width, height = map(int,resolution.split('x'))
        diagonal_resolution = math.sqrt(width ** 2 + height ** 2)
        ppi = diagonal_resolution / inches

        return ppi

    def get_predicted_price(self):

        self.load_models()

        company_index = list(self.load_json["columns"]).index(self.Company)
        TypeName_index = list(self.load_json["columns"]).index(self.TypeName)
        Cpu_brand_index = list(self.load_json["columns"]).index(self.Cpu_brand)
        Gpu_brand_index = list(self.load_json["columns"]).index(self.Gpu_brand)
        os_index = list(self.load_json["columns"]).index(self.os)

        test_array = np.zeros(len(self.load_json["columns"]))

        test_array[0] = self.Ram
        test_array[1] = self.Weight
        test_array[2] = self.load_json["Touchscreen"][self.Touchscreen]
        test_array[3] = self.load_json["Ips"][self.Ips]
        test_array[4] = self.ppi
        test_array[5] = self.HDD
        test_array[6] = self.SSD
        test_array[company_index] = 1
        test_array[TypeName_index] = 1
        test_array[Cpu_brand_index] = 1
        test_array[Gpu_brand_index] = 1
        test_array[os_index] = 1

        price = round(np.exp(self.load_model.predict([test_array])[0]))

        return price