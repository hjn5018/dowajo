from flask import Flask, render_template, request, redirect, url_for
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
    username = db.Column(db.String, nullable=False) #<-이거 디폴트 값이 'reader'가 아니라 입력한 페이지에 맞게 들어가게 해야함
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
    help_list = Help.query.filter_by(username="leader").all()

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
    help_list = Help.query.filter_by(username="member1").all()

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
    help_list = Help.query.filter_by(username="member2").all()

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
    help_list = Help.query.filter_by(username="member3").all()

    context = {
        "name": name,
        "profile": profile,
        "tag": tag
    }
    return render_template("member3.html", data=context, dowajo=help_list)

# @app.route('/help/create', methods=['GET', 'POST'])
# def helplist_create():
#     if request.method == 'GET':
#         helptitle_receive = request.args.get("helptitle")
#         helpcontent_receive = request.args.get("helpcontent")
        
#         # 현재 URL을 분석하여 username을 가져옵니다.
#         username_receive = request.url.split('/')[-1]

#         # 데이터를 DB에 저장하기
#         help = Help(title=helptitle_receive, content=helpcontent_receive, username=username_receive)
#         db.session.add(help)
#         db.session.commit()

#         # 각 페이지로 리다이렉트합니다.
#         if username_receive == 'leader':
#             return redirect(url_for('leader'))
#         elif username_receive == 'member1':
#             return redirect(url_for('member1'))
#         elif username_receive == 'member2':
#             return redirect(url_for('member2'))
#         elif username_receive == 'member3':
#             return redirect(url_for('member3'))

#     return redirect(url_for('home'))

# leader HELP ME 버튼 db 적용 
@app.route('/help/create/leader')
def helplist_create():
    # form으로 데이터 입력 받기
    helptitle_receive = request.args.get("helptitle")
    helpcontent_receive = request.args.get("helpcontent")
    username_receivee = request.url.split('/')[-1] # 현재 URL을 분석하여 username을 가져옴 여기선 leader -> 라고 기대했지만 "leader?helptitle=test&helpcontent=test" 이런 값을 가져와서
    username_receive = username_receivee.split('?')[0]  # 여기서 ? 기준으로 한번 더 나눴음 이제 username leader로 잘나옴

    # 데이터를 DB에 저장하기
    help = Help(title=helptitle_receive, content=helpcontent_receive, username=username_receive)
    db.session.add(help)
    db.session.commit()

    return redirect(url_for('leader'))

# # member1 HELP ME 버튼 db 적용 
@app.route('/help/create/member1')
def helplist_create_one():
    # form으로 데이터 입력 받기
    helptitle_receive = request.args.get("helptitle")
    helpcontent_receive = request.args.get("helpcontent")
    username_receivee = request.url.split('/')[-1]        # 위에 leader페이지 라우트 참고
    username_receive = username_receivee.split('?')[0]

    # 데이터를 DB에 저장하기
    help = Help(title=helptitle_receive, content=helpcontent_receive, username=username_receive)
    db.session.add(help)
    db.session.commit()

    return redirect(url_for('member1'))

# # member2 HELP ME 버튼 db 적용 
@app.route('/help/create/member2')
def helplist_create_two():
    # form으로 데이터 입력 받기
    helptitle_receive = request.args.get("helptitle")
    helpcontent_receive = request.args.get("helpcontent")
    username_receivee = request.url.split('/')[-1]         # 위에 leader페이지 라우트 참고
    username_receive = username_receivee.split('?')[0]

    # 데이터를 DB에 저장하기
    help = Help(title=helptitle_receive, content=helpcontent_receive, username=username_receive)
    db.session.add(help)
    db.session.commit()

    return redirect(url_for('member2'))

# # member3 HELP ME 버튼 db 적용 
@app.route('/help/create/member3')
def helplist_create_three():
    # form으로 데이터 입력 받기
    helptitle_receive = request.args.get("helptitle")
    helpcontent_receive = request.args.get("helpcontent")
    username_receivee = request.url.split('/')[-1]        # 위에 leader페이지 라우트 참고
    username_receive = username_receivee.split('?')[0]

    # 데이터를 DB에 저장하기
    help = Help(title=helptitle_receive, content=helpcontent_receive, username=username_receive)
    db.session.add(help)
    db.session.commit()

    return redirect(url_for('member3'))

# #Helping 버튼 db에 데이터 추가하기 (수정중)
# @app.route('/help/update', methods=['POST'])
# def update_help():
#     if request.method == 'POST':
#         # 폼에서 받은 데이터 추출
#         help_id = request.form['help_id']
#         answer = request.form['helpanswer']

#         # 데이터베이스에서 해당 항목 찾기
#         help_item = Help.query.get(help_id)

#         if help_item:
#             # 데이터베이스 항목 업데이트
#             help_item.answer = answer
#             db.session.commit()
#             return 'Help item updated successfully'
#         else:
#             return 'Help item not found'
#     else:
#         return 'Invalid request method'

if __name__ == "__main__":
    app.run(debug=True)
