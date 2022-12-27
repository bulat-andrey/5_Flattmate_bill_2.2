from flask.views import MethodView
from wtforms import Form
from flask import Flask


app = Flask(__name__)


class HomePage(MethodView):
    pass


class BillFromPage(MethodView):
    pass


class ResultsPage(MethodView):
    pass


class BillForm(Form):
    pass


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFromPage.as_view('bill_form_page'))

app.run()