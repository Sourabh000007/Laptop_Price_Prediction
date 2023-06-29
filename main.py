from flask import Flask,jsonify,render_template,request

from project_app.utils import Laptop_Price

app = Flask(__name__)
app.debug=True

@app.route("/")
def hello():
    return render_template("test.html")

@app.route("/predict_price", methods = ["POST","GET"])

def get_Laptop_price():
    if request.method == "GET":

        Ram                      = request.args.get("Ram")
        Weight                   = request.args.get("Weight")
        Touchscreen              = request.args.get("Touchscreen")
        Ips                      = request.args.get("Ips")
        resolution               = request.args.get("resolution")
        inches                   = float(request.args.get("inches"))
        HDD                      = request.args.get("HDD")
        SSD                      = int(request.args.get("SSD"))
        Company                  = request.args.get("Company")
        TypeName                 = request.args.get("TypeName")
        Cpu_brand                = request.args.get("Cpu_brand")
        Gpu_brand                = request.args.get("Gpu_brand")
        os                       = request.args.get("os")

        print(Ram)
        print(Weight)
        print(Touchscreen)
        print(Ips)
        print(resolution)
        print(inches)
        print(HDD)
        print(SSD)
        print(Company)
        print(TypeName)
        print(Cpu_brand)
        print(Gpu_brand)
        print(os)



        laptop = Laptop_Price(Ram,Weight,Touchscreen,Ips,resolution, inches,HDD,SSD,Company,TypeName,Cpu_brand,Gpu_brand,os)
        price = laptop.get_predicted_price()

        return render_template("test.html",prediction = price)
    
if __name__ == "__main__":
    app.run()