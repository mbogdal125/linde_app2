# Create your views here.
from approve_stocksheet.views_app.ChoseStocktakingView import ChoseStocktakingView
from approve_stocksheet.views_app.ChoseStocksheetView import ChoseStocksheetView
#from approve_stocksheet.views_app.AgreeDataView import AgreeDataView

chosestocktaking = ChoseStocktakingView.as_view()
chosestocksheet = ChoseStocksheetView.as_view()
#approvestocksheetdata = ApproveDataView.as_view()
