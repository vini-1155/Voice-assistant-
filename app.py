from flask import Flask,render_template,request
import lanhindi

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    try:
        if request.method == 'POST':
            query = request.form['s']
            lang = request.form['language']
            print(lang)
            print('user asked: ',query)
            result = lanhindi.ai(query)
            result = result.replace('\n',' ')
            results = []
            results.append(result)
            results.append(lang)
            print(results)
            return render_template('speak.html',result=results)
        return render_template('index.html')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run()