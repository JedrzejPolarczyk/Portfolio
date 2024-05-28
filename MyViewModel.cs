using DocumentsArchive;
using Microsoft.Data.SqlClient;
using System;
using System.Collections.ObjectModel;


public class DataService
{
    private string connectionString = "Data Source=mestools2;Initial Catalog=InternTestDB;User ID=intern;Password=InternAmica123; Trust Server Certificate=true;";

    public ObservableCollection<BookshelfMain> GetBookshelfData()
    {
        var bookshelfData = new ObservableCollection<BookshelfMain>();

        string query = @"
            SELECT 
                m.Id,
                m.Stand, 
                m.Shelf, 
                m.MainItemName, 
                s.Id AS SubItemId,
                s.SubItemName, 
                s.IsTaken, 
                s.LoginName,
                s.BookshelfMainId
            FROM 
                dbo.tbBookshelfMain m
            JOIN 
                dbo.tbBookshelfSub s 
                ON m.id = s.BookshelfMainId;";

        using (SqlConnection connection = new SqlConnection(connectionString))
        {
            SqlCommand command = new SqlCommand(query, connection);
            connection.Open();

            SqlDataReader reader = command.ExecuteReader();
            while (reader.Read())
            {
                int mainId = (int)reader.GetInt64(reader.GetOrdinal("Id"));
                var mainItem = bookshelfData.FirstOrDefault(b => b.Id == mainId);
                if (mainItem == null)
                {
                    mainItem = new BookshelfMain
                    {
                        Id = mainId,
                        Stand = reader.GetString(reader.GetOrdinal("Stand")),
                        Shelf = reader.GetString(reader.GetOrdinal("Shelf")),
                        MainItemName = reader.GetString(reader.GetOrdinal("MainItemName")),
                        SubItems = new List<BookshelfSub>()
                    };
                    bookshelfData.Add(mainItem);
                }

                mainItem.SubItems.Add(new BookshelfSub
                {
                    SubItemName = "123",
                    BookshelfMainId = mainId
                });
            }
            reader.Close();
        }

        return bookshelfData;
    }
}
