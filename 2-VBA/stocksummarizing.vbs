Sub summarizeStocks()
    
    For Each year_ws In Worksheets
        Dim ticker As String
        Dim total_stock_volume As Double
        total_stock_volume = 0
        year_ws.Cells(1, 9).Value = "Ticker"
        year_ws.Cells(1, 10).Value = "Total Stock Volume"
        LastRow = year_ws.Cells(Rows.Count, 1).End(xlUp).Row
        Dim i As Double
        
        ' Keep track of the location for each credit card brand in the summary table
        Dim Summary_Table_Row As Integer
        Summary_Table_Row = 2
              
        For i = 2 To LastRow
                
            ' Check if we are still within the same ticker name, if it is not...
            If year_ws.Cells(i + 1, 1).Value <> year_ws.Cells(i, 1).Value Then
            
              ' Set the ticker name
                ticker = year_ws.Cells(i, 1).Value
        
              ' Add to the total stock volume
                total_stock_volume = total_stock_volume + year_ws.Cells(i, 7).Value
        
              ' Print the ticker name in the Summary Table
                year_ws.Range("I" & Summary_Table_Row).Value = ticker
        
              ' Print the Brand Amount to the Summary Table
                year_ws.Range("J" & Summary_Table_Row).Value = total_stock_volume
        
              ' Add one to the summary table row
                Summary_Table_Row = Summary_Table_Row + 1
              
              ' Reset the Brand Total
                total_stock_volume = 0
        
            ' If the cell immediately following a row is the same brand...
            Else
            
        
              ' Add to the Brand Total
                total_stock_volume = total_stock_volume + year_ws.Cells(i, 7).Value
        
            End If
        
        Next i

    Next year_ws


End Sub

