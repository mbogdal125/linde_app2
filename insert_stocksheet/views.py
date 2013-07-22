# Create your views here.
from insert_stocksheet.views_app.ChoseStocktakingView import ChoseStocktakingView
from insert_stocksheet.views_app.ChoseStocksheetView import ChoseStocksheetView
from insert_stocksheet.views_app.InsertDataView import InsertDataView

chosestocktaking = ChoseStocktakingView.as_view()
chosestocksheet = ChoseStocksheetView.as_view()
insertstocksheetdata = InsertDataView.as_view()
