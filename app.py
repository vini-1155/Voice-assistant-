from flask import Flask,render_template,request
import lanhindi

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        query = request.form['s']
        # lang = request.form['language']
        # print(lang)
        print('user asked: ',query)
        result = lanhindi.ai(query)
        result = result.replace('\n',' ')
        results = []
        results.append(result)

        return render_template('speak.html',result=result)
    return render_template('index.html')

if __name__ == "__main__":
    app.run()


