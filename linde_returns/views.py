# Create your views here.
from linde_returns.views_app.ChoseStocktakingView import ChoseStocktakingView
from linde_returns.views_app.ChoseStocksheetView import ChoseStocksheetView
from linde_returns.views_app.ReturnStocksheetView import ReturnStocksheetView

chosestocktaking = ChoseStocktakingView.as_view()
chosestocksheet = ChoseStocksheetView.as_view()
returnstocksheet = ReturnStocksheetView.as_view()
