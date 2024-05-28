using System.Windows;

namespace YourNamespace
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            LoadData();
        }

        private void LoadData()
        {
            DataService dataService = new DataService();
            var data = dataService.GetBookshelfData();
            BookshelfGrid.ItemsSource = data;
        }
    }
}

