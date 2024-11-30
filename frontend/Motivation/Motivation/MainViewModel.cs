using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using Motivation.model;
namespace Motivation
{
    public class MainViewModel : INotifyPropertyChanged
    {
        Sotrudnik id;
        Http http=new Http();
        public MainViewModel(Sotrudnik idsotr)
        {
           id = idsotr;
        }

        private string firstname;
        public string Firstname
        {
            get
            {
                firstname = id.firstname;
                return firstname;
            }
            set
            {
                firstname = value;
                OnPropertyChanged(nameof(firstname));
            }
        }
        private string lastname;
        public string Lastname
        {
            get
            {
                lastname = id.lastname;
                return lastname;
            }
            set
            {
                lastname = value;
                OnPropertyChanged(nameof(lastname));
            }
        }
        private string surname;
        public string Surname
        {
            get
            {
                surname = id.surname;
                return surname;
            }
            set
            {
                surname = value;
                OnPropertyChanged(nameof(surname));
            }
        }
        int year = DateTime.Now.Year;
        public int Year
        {
            get
            {   
                return year;
            }
            set
            {
                year = value;
                OnPropertyChanged(nameof(year));
            }
        }
        static string [] month  = { "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь" };

        int selectedmonth;
        private RelayCommand salaryCommand;
        public RelayCommand SalaryCommand
        {
            get
            {
                return salaryCommand ??
                  (salaryCommand = new RelayCommand(async obj =>
                  {
                      try
                      {
                          deals = await http.HttpDeals(id.id);
                      }
                      catch (Exception ex)
                      {
                          MessageBox.Show(ex.ToString(), "Ошибка", MessageBoxButton.OK, MessageBoxImage.Error);
                      }
                  }));
            }
        }
        OutputSalary salary;
        OutputSalary Salary
        {
            get
            {
                return salary;
            }
            set
            {
                salary = value;
                OnPropertyChanged(nameof(salary));
            }
        }
        int SelectedMonth
        {
            get
            {
                return selectedmonth;
            }
            set
            {
                selectedmonth = value;
                OnPropertyChanged(nameof(selectedmonth));
            }
        }
        private RelayCommand dealsCommand;
        public RelayCommand DealsCommand
        {
            get
            {
                return dealsCommand ??
                  (dealsCommand = new RelayCommand(async obj =>
                  {
                      try
                      {
                          salary = await http.HttpMonthSalary(id.id, new DateTime(year, selectedmonth + 1, DateTime.DaysInMonth(year, selectedmonth + 1)));
                      }
                      catch (Exception ex)
                      {
                          MessageBox.Show(ex.ToString(), "Ошибка", MessageBoxButton.OK, MessageBoxImage.Error);
                      }
                  }));
            }
        }
        ObservableCollection<Deal> deals;
        ObservableCollection<Deal> Deals
        {
            get
            {
                return deals;
            }
            set
            {
                deals = value;
                OnPropertyChanged(nameof(deals));
            }
        }
        RelayCommand ratingCommand;
        public RelayCommand RatingCommand
        {
            get
            {
                return ratingCommand ??
                  (ratingCommand = new RelayCommand(async obj =>
                  {
                      try
                      {
                          rating = await http.HttpRating(id.id);
                      }
                      catch (Exception ex)
                      {
                          MessageBox.Show(ex.ToString(), "Ошибка", MessageBoxButton.OK, MessageBoxImage.Error);
                      }
                  }));
            }
        }
        ObservableCollection<Rating> rating;
        ObservableCollection<Rating> Rating
        {
            get
            {
                return rating;
            }
            set
            {
                rating = value;
                OnPropertyChanged(nameof(rating));
            }
        }

        public event PropertyChangedEventHandler PropertyChanged;
        public void OnPropertyChanged([CallerMemberName] string prop = "")
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(prop));
        }
    }
}
