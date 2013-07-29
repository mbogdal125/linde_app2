#-*- coding: utf-8 -*
# Create your views here.
from linde_app2.views_app.HomeView import HomeView
from linde_app2.views_app.StocktakingView import StocktakingView
from linde_app2.views_app.StocksheetView import StocksheetView

home_page = HomeView.as_view()
stocktaking = StocktakingView.as_view()
stocksheet = StocksheetView.as_view()
