using System.Windows;

namespace menu
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Home_Click(object sender, RoutedEventArgs e)
        {
            // Здесь создаем и устанавливаем UserControl для Главной страницы
            MainContent.Content = new HomePage();
        }

        private void Rating_Click(object sender, RoutedEventArgs e)
        {
            // Здесь создаем и устанавливаем UserControl для страницы Рейтинга
            MainContent.Content = new RatingPage();
        }

        private void Deal_Click(object sender, RoutedEventArgs e)
        {
            // Здесь создаем и устанавливаем UserControl для страницы Сделок
            MainContent.Content = new DealPage();
        }

        private void Salary_Click(object sender, RoutedEventArgs e)
        {
            // Здесь создаем и устанавливаем UserControl для страницы Зарплаты
            MainContent.Content = new SalaryPage();
        }
    }
}