from flask import Flask, render_template, request
app = Flask(__name__)
# DB 기본 코드
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class Help(db.Model):
    listnum = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, default="leader")
    answer = db.Column(db.String, nullable=False, default="")

    def __repr__(self):
        return f'{self.title} Help {self.username}'

with app.app_context():
    db.create_all()

   
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/leader")
def leader():

    name = "Han"
    profile = "Who i am"
    tag = "Leader"
    help_list = Help.query.all()

    context = {
        "name": name,
        "profile": profile,
        "tag": tag,
    }
    return render_template("leader.html", data=context, dowajo=help_list)


@app.route("/member1")
def member1():

    name = "Shin"
    profile = "Who i am"
    tag = "Member"
    help_list = Help.query.all()

    context = {
        "name": name,
        "profile": profile,
        "tag": tag
    }
    return render_template("member1.html", data=context, dowajo=help_list)


@app.route("/member2")
def member2():

    name = "Kim"
    profile = "Who i am"
    tag = "Member"
    help_list = Help.query.all()

    context = {
        "name": name,
        "profile": profile,
        "tag": tag
    }
    return render_template("member2.html", data=context, dowajo=help_list)


@app.route("/member3")
def member3():

    name = "Kang"
    profile = "Who i am"
    tag = "Member"
    help_list = Help.query.all()

    context = {
        "name": name,
        "profile": profile,
        "tag": tag
    }
    return render_template("member3.html", data=context, dowajo=help_list)

# db 적용 
@app.route('/help/create')
def helplist_create():
    # form으로 데이터 입력 받기
    helptitle_receive = request.args.get("helptitle")
    helpcontent_receive = request.args.get("helpcontent")

    # 데이터를 DB에 저장하기
    help = Help(title=helptitle_receive, content=helpcontent_receive)
    db.session.add(help)
    db.session.commit()

    return render_template("leader.html")


if __name__ == "__main__":
    app.run(debug=True)
