using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Motivation.model;
namespace Motivation
{
    public partial class MainWindow : Window
    {
        MainViewModel vm;
        public MainWindow(Sotrudnik sotrudnik)
        {
            InitializeComponent();
            vm = new MainViewModel(sotrudnik);
        }

        private void Sotrudnik_S(object sender, RoutedEventArgs e)
        {
            //Главная страница
            MainContent.Content = new PageSotrudnik(vm);
        }

        private void Rating_S(object sender, RoutedEventArgs e)
        {
            //страница Рейтинга
            MainContent.Content = new PageRating(vm);
        }

        private void Deal_S(object sender, RoutedEventArgs e)
        {
            //страница Сделок
            MainContent.Content = new PageDeal(vm);
        }

        private void Salary_S(object sender, RoutedEventArgs e)
        {
            //страница Зарплаты
            MainContent.Content = new PageSalary(vm);

        }
    }
}
