# Create your views here.
from agree_stocksheet.views_app.ChoseStocktakingView import ChoseStocktakingView
from agree_stocksheet.views_app.ChoseStocksheetView import ChoseStocksheetView
#from agree_stocksheet.views_app.AgreeDataView import AgreeDataView

chosestocktaking = ChoseStocktakingView.as_view()
chosestocksheet = ChoseStocksheetView.as_view()
#agreestocksheet = AgreeDataView.as_view()
