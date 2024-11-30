using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using Motivation.model;
namespace Motivation
{
    //логика для окна авторизации
    class ViewModel: INotifyPropertyChanged
    {
        Http http = new Http();
        string idsotr;
        Sotrudnik sotrudnik;
        private RelayCommand loginCommand;
        public RelayCommand LoginCommand
        {
            get
            {
                return loginCommand ??
                  (loginCommand = new  RelayCommand (async obj =>
                  {
                      try
                      {
                          sotrudnik = await http.HttpLogin(new Login(login, password));
                      }
                      catch(Exception ex)
                      {
                          MessageBox.Show(ex.ToString(),"Ошибка", MessageBoxButton.OK,MessageBoxImage.Error);
                      }
                      PageSotrudnik mw = new PageSotrudnik(sotrudnik);
                      mw.Show(); }));
            }
        }
        private string login;
        public string Login
        {
            get
            {
                return login;
            }
            set
            {
                login = value;
                OnPropertyChanged(nameof(login));
            }
        }
        private string password;
        public string Password
        {
            get
            {
                return password;
            }
            set
            {
                password = value;
                OnPropertyChanged(nameof(password));
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
