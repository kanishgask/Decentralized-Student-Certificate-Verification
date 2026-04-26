from flask import Flask,render_template,request
from connect_blockchain import add_certificate
from connect_blockchain import verify_certificate

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add',methods=['POST'])
def add():

    cert_id=request.form['id']
    name=request.form['name']
    course=request.form['course']
    university=request.form['university']
    hash_val=request.form['hash']

    add_certificate(
        cert_id,
        name,
        course,
        university,
        hash_val
    )

    return "Certificate Stored on Blockchain"


@app.route('/verify',methods=['POST'])
def verify():

    cert_id=request.form['id']

    data=verify_certificate(cert_id)

    return render_template(
        'index.html',
        result=data
    )


if __name__=="__main__":
    app.run(debug=True)
