from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pdfs.db'
#db = SQLAlchemy(app)
#ma = Marshmallow(app)

""""
class Pdf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    psw = db.Column(db.String(50))
    ip = db.Column(db.String(50))
    so = db.Column(db.String(50))
    ver = db.Column(db.String(50))

    def __init__(self, psw, ip, so, ver):
        self.psw = psw
        self.ip = ip
        self.so = so
        self.ver = ver


db.create_all()


class PdfSchema(ma.Schema):
    class Meta:
        fields = ('id', 'psw', 'ip', 'so', 'ver')


pdf_schema = PdfSchema()
pdfs_schema = PdfSchema(many=True)

"""

@app.route('/')
def table():

    return("Funciona, lol")

#Admin

#Company
#POST params: admin, name
@app.route('/api/v1/create_company', methods=['Post'])
def acreate_company():
    admin = request.args.get("admin")
    name = request.args.get("name") #New Company Name
    res = ""
    company_api_key = ''

    if admin == 'admin':
        #crear company_api_key
        company_api_key = '.'

        return str(res) + " " + str(name) + " key:" + company_api_key, 201
    else:
        res = res + "0"
        
        return str(name) + " err: No se cuenta con permisos de Admin", 401



#Location
#POST params: company_api_key, name, country, city,meta, company_id
@app.route('/api/v1/create_location', methods=['Post'])
def create_location():
    company_api_key = request.args.get("admin")
    name = request.args.get("name") #New Company Name
    country = request.args.get("country")
    city = request.args.get("city")
    meta = request.args.get("meta")
    company_id = request.args.get("company_id")

    res = ""
    companykey = ''

    if company_api_key == 'admin':
        #crear key
        companykey = '.'

        return str(res) + " " + str(name) + " key:" + companykey, 201
    else:
        res = res + "0"
        
        return str(name) + " err: No se cuenta con permisos de Admin", 401

#GET All company_api_key
@app.route('/api/v1/get_all_location', methods=['Get'])
def get_all_location():
    company_api_key = request.args.get("company_api_key")


    if company_api_key == 'admin':
        #crear key
        companykey = '.'

        return str(res) + " " + str(name) + " key:" + companykey, 201
    else:
        res = res + "0"
        
        return str(name) + " err: No se cuenta con permisos de Admin", 401



#GET location_id
@app.route('/api/v1/get_location', methods=['Get'])
def get_location():
    admin = request.args.get("admin")

    if admin == 'admin':
        #crear key
        companykey = '.'

        return "key:" + companykey, 201
    else:
        res = res + "0"
        
        return str(name) + " err: No se cuenta con permisos de Admin", 401


#PUT params: company_api_key, name, country, city,meta, company_id, location_id
@app.route('/api/v1/update_location', methods=['Put'])
def update_location():
    company_api_key = request.args.get("company_api_key")
    data = ['']*5
    data[0] = request.args.get("name") #New Company Name
    data[1] = request.args.get("country")
    data[2] = request.args.get("city")
    data[3] = request.args.get("meta")
    company_id = request.args.get("company_id")
    location_id = request.args.get("location_id")



    if company_api_key == 'admin':
        #crear key
        for i in data:
            if i == '':
                print("lol")
            else:
                print(i)
                continue
        return " key: updated", 201
    else:
        res = res + "0"
        
        return " err: No se cuenta con permisos de Admin", 401


#DELETE params: admin, location_id
@app.route('/api/v1/delete_location', methods=['Delete'])
def delete_location():
    admin = request.args.get("admin")
    name = request.args.get("name") #New Company Name
    country = request.args.get("country")
    city = request.args.get("city")
    meta = request.args.get("meta")
    company_id = request.args.get("company_id")

    res = ""
    companykey = ''

    if admin == 'admin':
        #crear key
        companykey = '.'

        return str(res) + " " + str(name) + " key:" + companykey, 201
    else:
        res = res + "0"
        
        return str(name) + " err: No se cuenta con permisos de Admin", 401





@app.route('/pdfs', methods=['GET'])
def get_pdfs():

    return "0"


@app.route('/pdfs/<id>', methods=['DELETE'])
def delete_pdf(id):

    return "0"


if __name__ == "__main__":
    app.run(debug=True)