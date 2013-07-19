# Create your views here.
from insert_stocksheet.views_app.InsertStockdataView import InsertStockdataView
from insert_stocksheet.views_app.ChoseStocksheetView import ChoseStocksheetView

insertstockdata = InsertStockdataView.as_view()
chosestocksheet = ChoseStocksheetView.as_view()
